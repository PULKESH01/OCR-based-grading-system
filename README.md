OCR-Based Grading System Using Tesseract and OpenCV

This repository contains an OCR-based grading system designed to automate the grading process of handwritten or printed answer sheets. The system combines Tesseract OCR, OpenCV, and Python to process scanned images, extract answers, and compare them with a predefined answer key.


🚀 Features

Automated Grading: Processes answer sheets and assigns grades based on an answer key.

Handwriting Recognition: Leverages OCR and machine learning techniques to handle handwritten responses.

Image Preprocessing: Includes grayscale conversion, noise reduction, thresholding, and edge detection for better OCR performance.

Customizable: Supports multiple-choice, fill-in-the-blank, and descriptive answers.

Scalability: Capable of processing large volumes of answer sheets efficiently.

Performance Metrics: Provides accuracy, precision, recall, and F1 score to evaluate system performance.


📁 Repository Structure

OCR-Grading-System/
├── data/                  # Sample datasets (answer sheets, answer keys)  
├── src/                   # Source code  
│   ├── preprocessing.py   # Image preprocessing code  
│   ├── ocr_processing.py  # OCR integration with Tesseract  
│   ├── grading.py         # Grading logic implementation  
│   ├── report.py          # Report generation scripts  
├── models/                # Pre-trained models for handwriting recognition (optional)  
├── results/               # Example results and performance metrics  
├── README.md              # Documentation  
└── requirements.txt       # List of required Python libraries


📋 Prerequisites

Python 3.8+

Tesseract OCR (ensure it is installed and added to the system PATH)

OpenCV

Required Python libraries (install using requirements.txt)


🔧 Installation

1. Clone the repository:

git clone https://github.com/PULKESH01/OCR-Grading-System.git  
cd OCR-Grading-System


2. Install dependencies:

pip install -r requirements.txt


3. Install Tesseract OCR:

Download Tesseract OCR

Add the Tesseract executable path to your environment variables.



📖 Usage

1. Prepare Answer Sheets: Place scanned images in the data/ folder.


2. Define Answer Key: Specify the correct answers in the answer key file.


3. Run the System:

python src/main.py --input data/answersheet.png --key data/answer_key.txt


4. View Results: Generated results and reports will be saved in the results/ folder.



🛠️ Methodology

1. Image Preprocessing:

Grayscale conversion

Noise reduction

Thresholding and edge detection


2. OCR Processing:

Tesseract OCR extracts text from preprocessed images.

Handwriting recognition is supported using pre-trained models.

3. Grading Logic:

Extracted answers are compared with the predefined key.

Metrics such as partial matching and spelling corrections are incorporated.

4. Report Generation:

Generates detailed reports with scores and individual question analysis.


📊 Evaluation Metrics

The system's performance is evaluated using:

Accuracy

Precision

Recall

F1 Score


📈 Future Improvements

Deep learning integration for handwriting recognition.

Support for multilingual answer sheets.

Cloud-based grading platform for scalability.

📜 License

This project is licensed under the MIT License. See the LICENSE file for details.

🤝 Contributing

Contributions are welcome! Feel free to fork the repository and create pull requests for improvements.


📝 Author

Pulkesh Gautam

Email: pulkeshgautam.in@gmail.com
