import tkinter as tk
from tkinter import filedialog, colorchooser
import trimesh
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Create a Tkinter window
root = tk.Tk()
root.title("STL Viewer")

# Prompt the user to select an STL file
def open_file():
    global file_path, stl_mesh, vertices, faces, mesh, ax

    file_path = filedialog.askopenfilename(filetypes=[("STL files", "*.stl")])

    # Load the STL file using trimesh
    stl_mesh = trimesh.load(file_path)

    # Extract the mesh vertices and faces
    vertices = stl_mesh.vertices
    faces = stl_mesh.faces

    # Set the default color of the mesh
    color = (1, 0, 0)  # Red

    # Create a 3D plot of the mesh using matplotlib
    mesh = ax.plot_trisurf(vertices[:,0], vertices[:,1], vertices[:,2], triangles=faces, shade=False, color=color)

    canvas.draw()

open_file_button = tk.Button(root, text="Open File", command=open_file)
open_file_button.pack(side=tk.BOTTOM)

# Load the initial file
file_path = filedialog.askopenfilename(filetypes=[("STL files", "*.stl")])
stl_mesh = trimesh.load(file_path)
vertices = stl_mesh.vertices
faces = stl_mesh.faces
color = (1, 0, 0)  # Red

# Create a 3D plot of the mesh using matplotlib
fig = plt.figure(figsize=(5, 4), dpi=100)
ax = fig.add_subplot(111, projection='3d')
mesh = ax.plot_trisurf(vertices[:,0], vertices[:,1], vertices[:,2], triangles=faces, shade=False, color=color)

# Embed the plot in a Tkinter canvas
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

# Create a button to change the color of the mesh
def change_color():
    global mesh, ax

    # Prompt user to select a new color
    new_color = colorchooser.askcolor(color='white', parent=root)[0]
    if new_color is None:
        return

    # Convert the color from RGB to a tuple of floats
    color = tuple(np.array(new_color) / 255)

    # Set the facecolors property of the Poly3DCollection to the new color
    mesh.set_facecolor(color)
    ax.clear()
    ax.add_collection3d(mesh)
    canvas.draw()        
color_button = tk.Button(root, text="Change Color", command=change_color)
color_button.pack(side=tk.BOTTOM)

# Run the Tkinter event loop
root.mainloop()