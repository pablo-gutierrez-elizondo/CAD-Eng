# Prompt to CAD File Generator
## Overview
The Promt to CAD File Generator is a tool designed to help individuals who are new to Computer-Aided Design (CAD) easily create entry-level designs. By simply providing a text prompt, users can generate 3D models in STL format. Additionally, the tool features a gallery where users can view and download STL files created by others, fostering a community of shared designs and inspiration. 
## Features
- *Text to CAD Conversion*: Generate 3D models from text prompts using the KittyCAD API.
- *STL File Viewer*: Visualize generated STL files directly within the application.
- *Gallery*: Browse and search through a gallery of STL files created by other users.
- *Download STL Files*: Download STL files for personal use or further modification.
- *Oski Integration*: Integrate with Anthropics latest model of Claude for a simple way to get assistance in your 3D modeling.
## Installation
To get started with the Prompt to CAD File Generator, follow these steps:
1. **Clone the repository**:
   ```
   git clone https://github.com/pablo-gutierrez-elizondo/CAD-Eng.git
   cd calhacks
   ```
2. **Install the required dependencies**:
   ```
   pip install -r requirements.txt
   ```
## Usage
1. **Run the Streamlit application**:
2. **Navigate to the application in your web browser**: Streamlit will provide a local URL (usually http://localhost:8501) where you can access the application.
3. **Generate a CAD File**:
   - Enter a text prompt in the input field.
   - Click the "Create CAD File" button.
   - The generated STL file will be displayed and can be downloaded.
4. **View the Gallery**:
   - Click the "Go to Gallery" button to navigate to the gallery page.
   - Use the search bar to filter creations by prompts.
   - View and download STL files created by other users.
## Project structure
```
my_app/
├── app.py # Main application file
├── helper.py # Helper functions (e.g., display_stl)
├── requirements.txt # Project dependencies
├── README.md # Project documentation
├── pages/ # Directory for different pages
│ ├── gallery.py # Gallery page
│ ├── home.py # Home page
│ └── prompt.py # Prompt page
├── generatedFiles/ # Directory for generated STL files and prompts
├── .venv/ # Virtual environment
├── pycache/ # Compiled Python files
└── myenv/ # Additional environment files
```
## Dependencies
The project relies on the following Python packages:
- streamlit: For building the webb application.
- kittycad: For the interacting with the KittyCad API.
- numpy: For numerical operations.
- matplotlib: For plotting and visualizing STL files.
- numpy-stl: For handling STL files.
  
## Acknowledgments
- **KittyCAD**: For providing the API to convert text prompts to CAD files.
- **Streamlit**: For making it wasy to build and share web applications. 
