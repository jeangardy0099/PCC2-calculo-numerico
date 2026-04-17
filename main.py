import numpy as np
import matplotlib.pyplot as plt

# =========================
# MÉTODO DE BAIRSTOW
# =========================
def bairstow(a, r, s, tol=1e-6, max_iter=100):
    n = len(a) - 1

    for _ in range(max_iter):
        b = np.zeros(n+1, dtype=complex)
        c = np.zeros(n+1, dtype=complex)

        b[n] = a[n]
        b[n-1] = a[n-1] + r*b[n]

        for i in range(n-2, -1, -1):
            b[i] = a[i] + r*b[i+1] + s*b[i+2]

        c[n] = b[n]
        c[n-1] = b[n-1] + r*c[n]

        for i in range(n-2, 0, -1):
            c[i] = b[i] + r*c[i+1] + s*c[i+2]

        det = c[2]*c[2] - c[3]*c[1]

        if abs(det) < 1e-12:
            r += 1
            s += 1
            continue

        dr = (-b[1]*c[2] + b[0]*c[3]) / det
        ds = (-b[0]*c[2] + b[1]*c[1]) / det

        r += dr
        s += ds

        if abs(dr) < tol and abs(ds) < tol:
            return r, s, b

    return None, None, None


def bairstow_roots(coeffs):
    a = np.array(coeffs, dtype=complex)
    roots = []

    while len(a) > 3:
        r, s, b = bairstow(a, r=1.0, s=1.0)

        if r is None:
            raise ValueError("Bairstow não convergiu")

        delta = r*r + 4*s
        roots.append((r + np.sqrt(delta)) / 2)
        roots.append((r - np.sqrt(delta)) / 2)

        a = b[2:]

    if len(a) == 3:
        delta = a[1]**2 - 4*a[2]*a[0]
        roots.append((-a[1] + np.sqrt(delta)) / (2*a[2]))
        roots.append((-a[1] - np.sqrt(delta)) / (2*a[2]))

    elif len(a) == 2:
        roots.append(-a[0]/a[1])

    return roots


# =========================
# FRACTAL
# =========================
def fractal(coeffs, grid=80):
    R = np.linspace(-3, 3, grid)
    S = np.linspace(-3, 3, grid)
    Z = np.zeros((grid, grid))

    for i in range(grid):
        for j in range(grid):
            r, s = R[i], S[j]
            count = 0

            for _ in range(30):
                res = bairstow(coeffs, r, s, max_iter=1)
                if res[0] is None:
                    break
                r, s = res[0], res[1]
                count += 1

            Z[j, i] = count

    return Z


# =========================
# 1. VALIDAÇÃO
# =========================
print("=== VALIDAÇÃO ===")
roots_true = [1, -2, 3, -4, 5, -6, 7]
poly_test = np.poly(roots_true)

roots_calc = bairstow_roots(poly_test)

print("Raízes encontradas:")
for r in roots_calc:
    print(r)


# =========================
# 2. APC2
# =========================
print("\n=== APC2 ===")
poly_apc = [1, 4, 11, 12, 12]

roots_apc = bairstow_roots(poly_apc)

print("Raízes do sistema:")
for r in roots_apc:
    print(r)


# =========================
# 3. FRACTAL
# =========================
print("\nGerando fractal...")

Z = fractal(poly_apc)

plt.imshow(Z, extent=[-3, 3, -3, 3], origin='lower')
plt.colorbar(label="Iterações")
plt.xlabel("r0")
plt.ylabel("s0")
plt.title("Fractal de Bairstow")
plt.show()
