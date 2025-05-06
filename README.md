# Protein Sorter App

## Overview
Protein Sorter App is a desktop application designed to analyze and categorize proteins based on their cellular localization and mitochondrial protein complex membership. The application specifically focuses on mitochondrial proteins and their sub-compartments, helping researchers to quickly sort and identify proteins from proteomics data.

## Purpose
This tool helps researchers to:
* Identify mitochondrial proteins in proteomics datasets using MitoCarta v3
* Categorize proteins by specific mitochondrial compartments (MIM, MOM, IMS, Matrix)
* Identify proteins belonging to specific respiratory complexes (Complex 1-5)
* Find proteins of interest including Mia40 substrates
* Process proteomics data files and generate annotated outputs

## Features
* **Multiple Sorting Options**:
   * Mitochondrial proteins (Human and Mouse)
   * Mitochondrial Inner Membrane (MIM) proteins
   * Mitochondrial Outer Membrane (MOM) proteins
   * Intermembrane Space (IMS) proteins
   * Matrix proteins
   * Respiratory complex components (Complex 1-5)
   * Mia40 substrates
   * Custom proteins of interest (you can include the list of Uniprot IDs of protein of interests. 
* **User-Friendly Interface**: Simple GUI with file selection and sorting options
* **Excel File Processing**: Reads and writes Excel files for seamless integration with existing workflows
* **Status Updates**: Real-time status updates during processing

## Requirements
* Python 3.x
* Required Python packages:
   * pandas
   * tkinter
   * threading

## Installation
1. Clone this repository:
   ```
   git clone https://github.com/science64/Protein-Sorter-App.git
   ```

2. Navigate to the project directory:
   ```
   cd Protein-Sorter-App
   ```

3. Make sure you have the required database file:
   * Place `database.xlsx` in the `files` folder
   * This database contains the reference protein lists for sorting

## How to Use
1. Run the application:
   ```
   python main.py
   ```

2. The application interface will appear with the following options:
   * Click "Browse" to select your proteomics data file (Excel format)
   * Choose a sorting category from the radio buttons
   * Click "RUN" to process your data
   * Status updates will appear in the text box
   * When processing is complete, click "Open" to view the results

3. The output file will be saved with "_MC3" appended to the original filename

## Input File Format
The application expects an Excel file with protein data that includes either:
* An "Accession" column containing protein accession numbers
* A "Master Protein Accessions" column containing protein accession numbers

## Output
The application generates an annotated Excel file with the original data plus additional columns indicating:
* Mitochondrial localization (YES/NO)
* Specific compartment localization (MIM, MOM, IMS, Matrix)
* Complex membership (Complex 1-5)
* Other protein classifications based on the selected sorting option

## Database Information
The application uses a reference database (`database.xlsx`) that contains lists of proteins categorized by:
* Mitochondrial localization
* Sub-mitochondrial compartments (MIM, MOM, IMS, Matrix)
* Respiratory complexes (Complex 1-5)
* Other cellular compartments (Golgi, ER)
* Functional categories (Kinases, Proteases, Autophagy, Apoptosis)

The respiratory complex data is sourced from HGNC: **https://www.broadinstitute.org/mitocarta/mitocarta30-inventory-mammalian-mitochondrial-proteins-and-pathways**

## License
MIT License

## Contact
bozkurt@med.uni-frankfurt.de

## Citation
If you use this software in your research, please cite: **https://www.sciencedirect.com/science/article/pii/S1097276521009540**

## Acknowledgments
* Developed by Süleyman Bozkurt

## Troubleshooting
* Ensure the `database.xlsx` file is in the `files` folder
* Make sure your input Excel file has the correct column names
* For any issues, check the status box for error messages
