from google.colab import drive
drive.mount('/content/drive')

#Install the necessary libraries
!apt-get update
!apt-get install -y tesseract-ocr
!pip install pytesseract opencv-python pandas matplotlib

# Import libraries
import cv2
import pytesseract
import pandas as pd
from PIL import Image
import matplotlib.pyplot as plt
from google.colab import files

# Configure Tesseract path for Colab
pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'

# Function to preprocess the scanned image
def preprocess_image(image_path):
    # Load the image
    image = cv2.imread(image_path)

    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur to reduce noise
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Apply binary thresholding
    _, thresh = cv2.threshold(blurred, 150, 255, cv2.THRESH_BINARY)

    # Save preprocessed image for debugging
    cv2.imwrite("preprocessed_image.jpg", thresh)

    return thresh



# Function to extract answers using OCR
def extract_answers(image_path):
    # Preprocess the image
    preprocessed_image = preprocess_image(image_path)

    # Use OCR to extract text
    text = pytesseract.image_to_string(preprocessed_image)

    # Extract answers from the text (assuming a simple format like Q1: A, Q2: C, etc.)
    lines = text.splitlines()
    answers = {}
    for line in lines:
        if ':' in line:
            question, answer = line.split(':')
            question = question.strip().replace("Q", "").strip()
            answer = answer.strip()
            answers[int(question)] = answer.upper()  # Ensure uppercase for consistency

    return answers


# Function to grade the answers
def grade_answers(extracted_answers, answer_key):
    score = 0
    total_questions = len(answer_key)
    report = []

    for question, correct_answer in answer_key.items():
        student_answer = extracted_answers.get(question, "N/A")  # Default to "N/A" if not found
        is_correct = student_answer == correct_answer
        score += is_correct
        report.append({
            "Question": question,
            "Correct Answer": correct_answer,
            "Student Answer": student_answer,
            "Correct": is_correct
        })

    return score, total_questions, report


# Function to generate and save a report
def generate_report(report, score, total_questions):
    # Create a DataFrame
    df = pd.DataFrame(report)
    print("\nScore Report:")
    print(df)

    # Save as CSV
    df.to_csv("score_report.csv", index=False)

    # Display score summary
    print(f"\nFinal Score: {score}/{total_questions}")
    print("Detailed report saved as 'score_report.csv'.")

    # Download the report as a CSV file
    files.download('score_report.csv')


# Main function to run the grading system
def main():
    # Define the correct answer key
    answer_key = {
        1: "A",
        2: "C",
        3: "B",
        4: "D",
        5: "A"
    }

    # Upload the scanned image file
    uploaded = files.upload()
    scanned_image_path = next(iter(uploaded))  # Get the first uploaded file name

    # Check if the image was loaded correctly
    image = cv2.imread(scanned_image_path)
    if image is None:
        print(f"Error: Could not load image '{scanned_image_path}'. Please check the file path and ensure it's a valid image.")
        return  # Exit the program if image loading fails

    print("Extracting answers from the scanned sheet...")
    extracted_answers = extract_answers(scanned_image_path)
    print("Extracted Answers:", extracted_answers)

    print("\nGrading the answers...")
    score, total_questions, report = grade_answers(extracted_answers, answer_key)

    print("\nGenerating the score report...")
    generate_report(report, score, total_questions)


# Run the program
if __name__ == "__main__":
    main()
