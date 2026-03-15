import numpy as np
import time

# Simulation parameters
screen_size = 40
theta_spacing = 0.07
phi_spacing = 0.02
illumination = np.fromiter(".,-~:;=!*#$@", dtype="<U1")
A, B = 1.0, 1.0  # Rotation angles
R1, R2 = 1, 2   # Donut radii
K2 = 5
K1 = screen_size * K2 * 3 / (8 * (R1 + R2))

def render_frame(A: float, B: float) -> np.ndarray:
    """Generates one frame of the spinning 3D donut using numpy."""
    cos_A, sin_A = np.cos(A), np.sin(A)
    cos_B, sin_B = np.cos(B), np.sin(B)
    output = np.full((screen_size, screen_size), " ")
    zbuffer = np.zeros((screen_size, screen_size))

    # Calculate angles
    phi = np.arange(0, 2 * np.pi, phi_spacing)
    theta = np.arange(0, 2 * np.pi, theta_spacing)
    cos_phi, sin_phi = np.cos(phi), np.sin(phi)
    cos_theta, sin_theta = np.cos(theta), np.sin(theta)

    circle_x = R2 + R1 * cos_theta[:, np.newaxis]
    circle_y = R1 * sin_theta[:, np.newaxis]

    # 3D projection calculations
    x = (np.outer(cos_B * cos_phi + sin_A * sin_B * sin_phi, circle_x) - circle_y * cos_A * sin_B).T
    y = (np.outer(sin_B * cos_phi - sin_A * cos_B * sin_phi, circle_x) + circle_y * cos_A * cos_B).T
    z = (K2 + cos_A * np.outer(sin_phi, circle_x) + circle_y * sin_A).T
    ooz = np.where(z != 0, 1 / z, 0) # One over z

    # Projection to 2D
    xp = (screen_size / 2 + K1 * ooz * x).astype(int)
    yp = (screen_size / 2 - K1 * ooz * y).astype(int)

    # Lighting calculation
    L = np.around((( (np.outer(cos_phi, cos_theta) * sin_B - cos_A * np.outer(sin_phi, cos_theta) - sin_A * sin_theta[:, np.newaxis]) + (cos_B * (cos_A * sin_theta[:, np.newaxis] - np.outer(sin_phi, cos_theta * sin_A))) ) * 8)).astype(int).T
    
    # Render characters based on lighting and Z-buffer
    mask_L = L >= 0
    chars = illumination[L]
    for i in range(len(theta)):
        mask = mask_L[i] & (ooz[i] > zbuffer[xp[i], yp[i]])
        zbuffer[xp[i], yp[i]] = np.where(mask, ooz[i], zbuffer[xp[i], yp[i]])
        output[xp[i], yp[i]] = np.where(mask, chars[i], output[xp[i], yp[i]])
    
    return output

if __name__ == "__main__":
    while True:
        print("\x1b[H") # Clear screen
        print('\n'.join([' '.join(row) for row in render_frame(A, B)]))
        A += 0.08
        B += 0.04
        time.sleep(0.03)
