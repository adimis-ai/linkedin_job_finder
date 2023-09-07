# LinkedIn Job Finder

LinkedIn Job Finder is a Python project that helps you scrape job listings from LinkedIn, match them with your resume, and analyze the best job opportunities.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)

## Features

- **Job Link Scraper**: Scrape job listing links from LinkedIn based on your search criteria.
- **Resume Match**: Compare your resume with job descriptions to find the best match.
- **Job Analytics**: Analyze job matches and save the results in CSV format.
- **Modularized Code**: Organized codebase with modular functions for better maintainability.
- **Selenium Integration**: Utilizes Selenium for web scraping tasks.

## Prerequisites

Before using LinkedIn Job Finder, make sure you have the following prerequisites installed:

- Python 3.x: You can download it from the [official Python website](https://www.python.org/downloads/).
- Chrome Browser: LinkedIn Job Finder uses Selenium, which requires Chrome WebDriver. It's recommended to use Google Chrome.

## Installation

1. Clone the GitHub repository to your local machine:

   ```bash
   git clone https://github.com/yourusername/linkedin-job-finder.git
   ```

2. Change into the project directory:

   ```bash
   cd linkedin-job-finder
   ```

3. Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Configure your LinkedIn job search by modifying the `URL` variable in the `linkedin_job_scraper.py` file.

2. Run the LinkedIn Job Scraper:

   ```bash
   python linkedin_job_scraper.py
   ```

   This will scrape job listing links and save them to `./Job_Applier/DATA/links.txt`.

3. Prepare your resume in PDF format and save it as `./Job_Applier/DATA/resume.pdf`.

4. Convert your resume PDF to text:

   ```bash
   python pdf_to_text.py
   ```

   This will create `./Job_Applier/DATA/resume.txt`.

5. Run the Job Matcher and Analyzer:

   ```bash
   python job_matcher_analyzer.py
   ```

   This will calculate the match percentage of your resume with each job description, save the results in `./Job_Applier/DATA/JOBS_ANALYTICS.csv`, and display match percentages for each job.

## Project Structure

- `linkedin_job_scraper.py`: Script for scraping job listing links from LinkedIn.
- `pdf_to_text.py`: Script for converting a resume PDF to text.
- `job_matcher_analyzer.py`: Script for matching your resume with job descriptions and analyzing the results.
- `Job_Applier/DATA/`: Directory to store data files, including job links, resumes, and job descriptions.
- `requirements.txt`: List of Python packages required for the project.
- `README.md`: This file, providing project documentation.