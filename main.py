
import tkinter as tk
import math

# SMART ROBOTIC ARM
root = tk.Tk()
root.title("Smart_Robotic_Arm - Advanced Control")
root.geometry("1000x760")
root.configure(bg="#111827")
root.resizable(False, False)

angle1 = -60
angle2 = 30
gripper_open = True
servo_on = True

ARM1 = 160
ARM2 = 130

# Title
tk.Label(
    root,
    text="SMART ROBOTIC ARM",
    font=("Arial", 25, "bold"),
    bg="#111827",
    fg="#38bdf8"
).pack(pady=12)

tk.Label(
    root,
    text="Advanced Robotic Arm Control System",
    font=("Arial", 11),
    bg="#111827",
    fg="white"
).pack()

# Drawing area
canvas = tk.Canvas(
    root,
    width=950,
    height=450,
    bg="#0b1220",
    highlightthickness=1,
    highlightbackground="#334155"
)
canvas.pack(pady=15)

def draw_robot():
    canvas.delete("all")

    # Background grid
    for x in range(0, 950, 40):
        canvas.create_line(x, 0, x, 450, fill="#1e293b")

    for y in range(0, 450, 40):
        canvas.create_line(0, y, 950, y, fill="#1e293b")

    bx, by = 475, 355

    # First joint position
    a1 = math.radians(angle1)
    x1 = bx + ARM1 * math.cos(a1)
    y1 = by + ARM1 * math.sin(a1)

    # Second joint position
    a2 = math.radians(angle1 + angle2)
    x2 = x1 + ARM2 * math.cos(a2)
    y2 = y1 + ARM2 * math.sin(a2)

    # Robot base
    canvas.create_rectangle(
        bx - 65, by + 5, bx + 65, by + 35,
        fill="#475569", outline="#cbd5e1", width=2
    )

    canvas.create_oval(
        bx - 35, by - 15, bx + 35, by + 20,
        fill="#64748b", outline="white", width=2
    )

    # First arm
    canvas.create_line(
        bx, by, x1, y1,
        fill="#06b6d4", width=27,
        capstyle=tk.ROUND
    )

    # Second arm
    canvas.create_line(
        x1, y1, x2, y2,
        fill="#2563eb", width=23,
        capstyle=tk.ROUND
    )

    # Joints
    for x, y in [(bx, by), (x1, y1), (x2, y2)]:
        canvas.create_oval(
            x-17, y-17, x+17, y+17,
            fill="#facc15", outline="white", width=2
        )

    # Gripper
    gap = 17 if gripper_open else 4
    ux = math.cos(a2)
    uy = math.sin(a2)

    px = -uy
    py = ux

    for side in [-1, 1]:
        sx = x2 + px * side * gap
        sy = y2 + py * side * gap

        ex = sx + ux * 35 + px * side * 12
        ey = sy + uy * 35 + py * side * 12

        canvas.create_line(
            x2, y2, sx, sy,
            fill="#22c55e", width=7
        )

        canvas.create_line(
            sx, sy, ex, ey,
            fill="#22c55e", width=7,
            capstyle=tk.ROUND
        )

    # Information panel
    canvas.create_text(
        125, 35,
        text="ROBOT STATUS",
        fill="#38bdf8",
        font=("Arial", 15, "bold")
    )

    canvas.create_text(
        125, 70,
        text=f"Servo: {'ON' if servo_on else 'OFF'}",
        fill="#22c55e" if servo_on else "#ef4444",
        font=("Arial", 12, "bold")
    )

    canvas.create_text(
        125, 100,
        text=f"Joint 1: {angle1} deg",
        fill="white", font=("Arial", 11)
    )

    canvas.create_text(
        125, 125,
        text=f"Joint 2: {angle2} deg",
        fill="white", font=("Arial", 11)
    )

    canvas.create_text(
        125, 150,
        text=f"Gripper: {'OPEN' if gripper_open else 'CLOSED'}",
        fill="#facc15", font=("Arial", 11)
    )

    canvas.create_text(
        475, 420,
        text="SMART ROBOTIC ARM SIMULATION",
        fill="#38bdf8",
        font=("Arial", 13, "bold")
    )


# Control panel
panel = tk.Frame(root, bg="#111827")
panel.pack(pady=5)

# Servo controls
def toggle_servo():
    global servo_on
    servo_on = not servo_on

    state = tk.NORMAL if servo_on else tk.DISABLED
    scale1.config(state=state)
    scale2.config(state=state)
    open_button.config(state=state)
    close_button.config(state=state)

    servo_button.config(
        text="SERVO OFF" if servo_on else "SERVO ON",
        bg="#ef4444" if servo_on else "#16a34a"
    )

    draw_robot()


servo_button = tk.Button(
    panel,
    text="SERVO OFF",
    command=toggle_servo,
    bg="#ef4444",
    fg="white",
    font=("Arial", 11, "bold"),
    width=15
)
servo_button.grid(row=0, column=0, padx=10, pady=8)


def update_angle1(value):
    global angle1
    if servo_on:
        angle1 = int(float(value))
        draw_robot()


def update_angle2(value):
    global angle2
    if servo_on:
        angle2 = int(float(value))
        draw_robot()


# Joint 1 control
tk.Label(
    panel, text="JOINT 1 SERVO",
    bg="#111827", fg="#38bdf8",
    font=("Arial", 11, "bold")
).grid(row=1, column=0)

scale1 = tk.Scale(
    panel,
    from_=-170,
    to=0,
    orient=tk.HORIZONTAL,
    length=260,
    bg="#111827",
    fg="white",
    troughcolor="#2563eb",
    highlightthickness=0,
    command=update_angle1
)
scale1.set(angle1)
scale1.grid(row=2, column=0, padx=10)


# Joint 2 control
tk.Label(
    panel, text="JOINT 2 SERVO",
    bg="#111827", fg="#38bdf8",
    font=("Arial", 11, "bold")
).grid(row=1, column=1)

scale2 = tk.Scale(
    panel,
    from_=-120,
    to=120,
    orient=tk.HORIZONTAL,
    length=260,
    bg="#111827",
    fg="white",
    troughcolor="#2563eb",
    highlightthickness=0,
    command=update_angle2
)
scale2.set(angle2)
scale2.grid(row=2, column=1, padx=10)


# Gripper controls
def open_gripper():
    global gripper_open
    if servo_on:
        gripper_open = True
        draw_robot()


def close_gripper():
    global gripper_open
    if servo_on:
        gripper_open = False
        draw_robot()


open_button = tk.Button(
    panel,
    text="OPEN GRIPPER",
    command=open_gripper,
    bg="#16a34a",
    fg="white",
    font=("Arial", 11, "bold"),
    width=17
)
open_button.grid(row=3, column=0, pady=15)

close_button = tk.Button(
    panel,
    text="CLOSE GRIPPER",
    command=close_gripper,
    bg="#dc2626",
    fg="white",
    font=("Arial", 11, "bold"),
    width=17
)
close_button.grid(row=3, column=1, pady=15)


# Reset
def reset_robot():
    global angle1, angle2, gripper_open, servo_on

    angle1 = -60
    angle2 = 30
    gripper_open = True
    servo_on = True

    scale1.config(state=tk.NORMAL)
    scale2.config(state=tk.NORMAL)
    open_button.config(state=tk.NORMAL)
    close_button.config(state=tk.NORMAL)

    servo_button.config(
        text="SERVO OFF",
        bg="#ef4444"
    )

    scale1.set(angle1)
    scale2.set(angle2)

    draw_robot()


reset_button = tk.Button(
    root,
    text="RESET ROBOT",
    command=reset_robot,
    bg="#7c3aed",
    fg="white",
    font=("Arial", 12, "bold"),
    width=22
)
reset_button.pack(pady=10)

tk.Label(
    root,
    text="Python 3.14 | Smart Robotic Arm Project",
    bg="#111827",
    fg="#94a3b8",
    font=("Arial", 10)
).pack(pady=5)

draw_robot()
root.mainloop()
