# Image Enhancer Library

## 🚀 Overview
**Image Enhancer** is a Python library that provides AI-powered image processing capabilities, including:
- **Background Removal** (using `rembg`)
- **Image Enhancement** (brightness & contrast adjustment with OpenCV)

This package is designed for developers who need quick and efficient image processing in their Python projects.

---

## 📦 Installation

Install the package using `pip`:
```bash
pip install image_enhancer
```

Or install the latest development version:
```bash
git clone https://github.com/yourusername/image_enhancer.git
cd image_enhancer
pip install .
```

---

## 🎯 Features
✅ **Remove Backgrounds** - Automatically remove backgrounds from images.
✅ **Enhance Images** - Adjust brightness and contrast for better clarity.
✅ **Easy to Use** - Simple functions for quick integration into projects.
✅ **Lightweight** - Optimized for fast performance.

---

## 🛠️ Usage

### **1️⃣ Remove Background from an Image**
```python
from image_enhancer.processing import remove_background

remove_background("input.jpg", "output.png")
```

### **2️⃣ Enhance Image (Brightness & Contrast Adjustments)**
```python
from image_enhancer.processing import enhance_image

enhance_image("input.jpg", "enhanced.jpg")
```

---

## 🏗️ Project Structure
```
image_enhancer/
│── image_enhancer/       # Library Code
│   │── __init__.py       # Package Initialization
│   │── processing.py      # Image Processing Functions
│── tests/                # Unit Tests
│── setup.py              # Package Metadata
│── pyproject.toml        # Build System
│── README.md             # Documentation
│── LICENSE               # License Information
│── .gitignore            # Ignore Unnecessary Files
```

---

## ⚡ Development & Contribution

### **Setup a Local Development Environment**
```bash
git clone https://github.com/yourusername/image_enhancer.git
cd image_enhancer
pip install -r requirements.txt
```

### **Run Tests**
```bash
pytest tests/
```

### **Contribute**
1. Fork the repository 🍴
2. Create a new feature branch (`git checkout -b feature-name`)
3. Make changes and commit (`git commit -m "Add feature"`)
4. Push changes (`git push origin feature-name`)
5. Create a Pull Request 🚀

---

## 📜 License
This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

## 💬 Support
For any issues or feature requests, open an [issue on GitHub](https://github.com/yourusername/image_enhancer/issues).

---

## 🌟 Acknowledgments
- Built with **FastAPI, OpenCV, and rembg** for AI-powered image processing.
- Inspired by modern AI-driven photo editors.

⭐ **Give the project a star on GitHub if you find it useful!** ⭐


