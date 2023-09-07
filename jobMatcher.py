import os
import csv
import PyPDF2
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def read_resume_text(file_path):
    with open(file_path, 'r') as reader:
        return reader.read()

def extract_job_data(csv_file_path):
    job_data = pd.read_csv(csv_file_path)
    return job_data

def create_job_description_files(job_data, output_directory):
    for i, row in job_data.iterrows():
        text = f"{row['titles']} {row['companys']} {row['jobDetail']} {row['descriptions']} {row['locations']}"
        with open(os.path.join(output_directory, f'job-{i}.txt'), 'w') as f:
            f.write(text)

def calculate_match_percentage(resume, job_description):
    text = [resume, job_description]
    cv = CountVectorizer()
    count_matrix = cv.fit_transform(text)
    match_percentage = cosine_similarity(count_matrix)[0][1] * 100
    return round(match_percentage, 2)

def main():
    job_data = extract_job_data('/home/aditya/Desktop/lead_gen/DATA/python-jobs.csv')
    resume_text = read_resume_text('/home/aditya/Desktop/lead_gen/DATA/resume.txt')

    job_description_directory = "/home/aditya/Desktop/lead_gen/DATA/JOBS"
    match_percentages = []

    for file in os.listdir(job_description_directory):
        text_file = os.path.join(job_description_directory, file)
        with open(text_file, 'r') as f:
            job_description = f.read()
        match_percentage = calculate_match_percentage(resume_text, job_description)
        print(f"Your resume matches about {match_percentage}% of the job description.")
        match_percentages.append(match_percentage)

    with open('/home/aditya/Desktop/lead_gen/DATA/JOBS.csv', 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['match_percent', 'titles', 'companys', 'jobDetails', 'descriptions', 'locations', 'companys_link', 'links'])
        for match_percentage, row in zip(match_percentages, job_data.iterrows()):
            _, data = row
            writer.writerow([match_percentage] + list(data))

    df = pd.read_csv("/home/aditya/Desktop/lead_gen/DATA/JOBS.csv")
    sorted_df = df.sort_values(by=["match_percent"], ascending=False)
    sorted_df.to_csv('/home/aditya/Desktop/lead_gen/DATA/JOBS_ANALYTICS.csv', index=False)

if __name__ == "__main__":
    main()
