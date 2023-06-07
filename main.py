
import multiprocessing
import pytesseract
import os
from pdf2image import convert_from_path
import pandas as pd
import tempfile
import shutil


# Function to perform OCR on an image
def ocr_image(image, extracted_text,custom_config):

    
    text = pytesseract.image_to_string(image, lang='eng', config=custom_config)
    extracted_text.append(text)

#takes a directory and adds files to a list
def folder_iterate(folder_path):
    # Initialize empty lists to store PDF and non-PDF file paths
    pdf_lst = []
    non_pdf = []

    # Iterate over the files in the folder
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        
        # Get the file extension
        extension = os.path.splitext(filename)[1]

        if os.path.isfile(file_path) and extension == '.pdf':
            # If the file is a PDF, add the file path to the PDF list
            pdf_lst.append(file_path)
        else:
            # If the file is not a PDF, add the file path to the non-PDF list
            file_path = os.path.basename(file_path)
            non_pdf.append(file_path)

    # Return the lists of PDF and non-PDF file paths
    return pdf_lst, non_pdf


def pdf_to_csv(pdf_path,output_dir,image_dir):
    # Convert PDF to a list of images
    images = convert_from_path(pdf_path, output_folder=image_dir)

    # Get the base file name without extension
    file_name = os.path.splitext(os.path.basename(pdf_path))[0]
    output_path = os.path.join(output_dir,file_name + '.csv')

    # Set Tesseract OCR configuration
    custom_config = r'--psm 6'

    # Create a manager to handle the shared list

    manager = multiprocessing.Manager()
    extracted_text = manager.list()

    # Extract text from each image using Tesseract OCR
    processes = []
    
    for image in images:
        process = multiprocessing.Process(target = ocr_image, args = (image, extracted_text,custom_config))
        # Start the process
        process.start()
        # Add the process to the list
        processes.append(process)

    for process in processes:
        process.join()
        

    # Join extracted text with double newlines to create a single string
    cleaned_text = '\n\n'.join(extracted_text)

    # Split cleaned text into lines
    lines = cleaned_text.split('\n')

    # Create a DataFrame from the lines of text
    pdf_df = pd.DataFrame(lines, columns=['text'])

    # Split the 'text' column into multiple columns using space as separator
    pdf_df = pdf_df['text'].str.split(' ', expand=True)

    # Save the DataFrame as a CSV file with the base file name
    pdf_df.to_csv(output_path, index=False)


def process_pdf(index,pdf_lst,output_dir,image_dir):

    pdf_to_csv(pdf_lst[index], output_dir, image_dir)


def main(output_dir, folder_path):
        # Get input paths where pdfs are saved and the output folder. 
        #output_dir = input("Enter directory to save output: ").strip('"')
        #folder_path = input("Enter directory with pdfs: ").strip('"')

   
    image_dir = tempfile.mkdtemp()

    try:
        pdf_lst, non_pdf_lst = folder_iterate(folder_path)
        # Create a list to store processes
        processes = []

        # Iterate over the pdf_lst
        for i in range(len(pdf_lst)):
                # Create a new process for each iteration
            process = multiprocessing.Process(target=process_pdf, args=(i,pdf_lst,output_dir,image_dir))
            # Start the process
            process.start()
            # Add the process to the list
            processes.append(process)

        for process in processes:
            process.join()
    finally:
        # Remove the temporary directory
        shutil.rmtree(image_dir)

    non_pdfs = ', '.join(non_pdf_lst)

    non_pdfs_message = f'These files were not used: {non_pdfs}'

    return non_pdfs_message

if __name__ =="__main__":
    main()
