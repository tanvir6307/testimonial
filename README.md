# Testimonial Generator for the Department of Physics, Jagannath University

This project provides a simple and efficient web-based tool to generate formatted testimonials for BSc and MSc students. Developed using HTML, CSS, and JavaScript, it streamlines the process of creating official documents by dynamically placing student information onto a predefined template.

---

## Features

* **Dual Program Support**: Separate, tailored forms and templates for both **B.Sc** and **M.Sc** students.
* **Dynamic Data Entry**: Intuitive forms for inputting student details such as name, ID, session, CGPA, and more.
* **Live Canvas Rendering**: Automatically renders the input data onto a high-quality testimonial template using the HTML Canvas API.
* **Custom Fonts**: Implements custom fonts to match the official document's typography for a professional finish.
* **PDF Export**: One-click download functionality to save the generated testimonial as a high-quality PDF, named using the student's ID for easy organization.
* **Responsive Design**: A clean, modern interface that is easy to navigate.

---

## How It Works

The workflow is straightforward:

1.  **Select Degree**: On the main page (`index.html`), the user chooses between "B.Sc" and "M.Sc".
2.  **Enter Information**: Based on the selection, the user is redirected to the appropriate data entry form (`page1.html` for B.Sc, `page3.html` for M.Sc).
3.  **Submit and Generate**: After filling out all fields and clicking "Submit," the form data is passed via URL parameters to a dedicated canvas page (`page2.html` for B.Sc, `page4.html` for M.Sc).
4.  **Render and Download**: This page uses JavaScript to draw the submitted information onto a background template image. The final testimonial is then displayed and ready for download as a PDF.

---

## Setup and Usage

This project runs entirely on the client-side, so no server is needed.

### Prerequisites
* A modern web browser (e.g., Google Chrome, Firefox).
---
## Technologies Used

* **HTML5**: For the structure and content of the web pages.
* **CSS3**: For styling the user interface with a clean, neumorphic design.
* **JavaScript (ES6)**: For form validation, data handling, and dynamic rendering on the HTML canvas.
* **jsPDF Library**: Used to convert the canvas output into a downloadable PDF document.

