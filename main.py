"""
CSE 310 - Applied Programming
Module 1: Data Analysis

Author: Olanrewaju Adebayo

This program analyzes a public dataset containing
data science job salaries using Pandas and Matplotlib.
"""

import pandas as pd
import matplotlib.pyplot as plt


def load_dataset(file_path):
    """
    Load the CSV dataset into a Pandas DataFrame.
    """
    return pd.read_csv(file_path)


def clean_dataset(df):
    """
    Remove unnecessary columns from the dataset.
    """
    if "Unnamed: 0" in df.columns:
        df = df.drop(columns=["Unnamed: 0"])
    return df


def display_dataset_info(df):
    """
    Display basic information about the dataset.
    """
    print("\n========== FIRST FIVE ROWS ==========\n")
    print(df.head())

    print("\n========== DATASET INFORMATION ==========\n")
    df.info()

    print("\n========== DATASET SHAPE ==========\n")
    print(f"Rows: {df.shape[0]}")
    print(f"Columns: {df.shape[1]}")


def most_common_jobs(df):
    """
    Display the ten most common job titles.
    """
    print("\n========== TOP 10 JOB TITLES ==========\n")
    print(df["job_title"].value_counts().head(10))


def highest_paying_jobs(df):
    """
    Display the ten highest-paying job titles based on average salary.
    """
    print("\n========== HIGHEST PAYING JOB TITLES ==========\n")

    salaries = (
        df.groupby("job_title")["salary_in_usd"]
        .mean()
        .sort_values(ascending=False)
        .head(10)
    )

    print(salaries)

def plot_common_jobs(df):
    """
    Create a bar chart of the ten most common job titles.
    """
    jobs = df["job_title"].value_counts().head(10)

    plt.figure(figsize=(10, 6))
    jobs.plot(kind="bar")
    plt.title("Top 10 Most Common Data Science Job Titles")
    plt.xlabel("Job Title")
    plt.ylabel("Number of Jobs")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()

    plt.savefig("charts/top_job_titles.png")
    plt.show()


def plot_highest_paying_jobs(df):
    """
    Create a bar chart of the ten highest-paying job titles.
    """
    salaries = (
        df.groupby("job_title")["salary_in_usd"]
        .mean()
        .sort_values(ascending=False)
        .head(10)
    )

    plt.figure(figsize=(10, 6))
    salaries.plot(kind="bar")
    plt.title("Top 10 Highest Paying Job Titles")
    plt.xlabel("Job Title")
    plt.ylabel("Average Salary (USD)")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()

    plt.savefig("charts/highest_paying_jobs.png")
    plt.show()

def analyze_experience_levels(df):
    """
    Display the distribution of experience levels.
    """
    print("\n========== EXPERIENCE LEVEL DISTRIBUTION ==========\n")

    levels = {
        "EN": "Entry Level",
        "MI": "Mid Level",
        "SE": "Senior Level",
        "EX": "Executive Level"
    }

    experience = df["experience_level"].replace(levels).value_counts()

    print(experience)

    return experience

def plot_experience_levels(df):
    """
    Create a pie chart showing the distribution of experience levels.
    """
    levels = {
        "EN": "Entry Level",
        "MI": "Mid Level",
        "SE": "Senior Level",
        "EX": "Executive Level"
    }

    experience = df["experience_level"].replace(levels).value_counts()

    plt.figure(figsize=(8, 8))
    experience.plot(
        kind="pie",
        autopct="%1.1f%%",
        startangle=90
    )

    plt.ylabel("")
    plt.title("Distribution of Experience Levels")

    plt.tight_layout()
    plt.savefig("charts/experience_levels.png")
    plt.close()

def analyze_remote_work(df):
    """
    Display the distribution of remote work arrangements.
    """
    print("\n========== REMOTE WORK DISTRIBUTION ==========\n")

    remote = {
        0: "On-site",
        50: "Hybrid",
        100: "Remote"
    }

    remote_data = df["remote_ratio"].replace(remote).value_counts()

    print(remote_data)

    return remote_data

def plot_remote_work(df):
    """
    Create a bar chart of remote work arrangements.
    """
    remote = {
        0: "On-site",
        50: "Hybrid",
        100: "Remote"
    }

    remote_data = df["remote_ratio"].replace(remote).value_counts()

    plt.figure(figsize=(8, 5))
    remote_data.plot(kind="bar")

    plt.title("Remote Work Distribution")
    plt.xlabel("Work Arrangement")
    plt.ylabel("Number of Jobs")

    plt.xticks(rotation=0)

    plt.tight_layout()
    plt.savefig("charts/remote_work_distribution.png")
    plt.close()

def main():
    """
    Main program.
    """
    dataset = load_dataset("data/ds_salaries.csv")

    dataset = clean_dataset(dataset)

    display_dataset_info(dataset)

    most_common_jobs(dataset)

    highest_paying_jobs(dataset)

    plot_common_jobs(dataset)

    plot_highest_paying_jobs(dataset)

    analyze_experience_levels(dataset)

    plot_experience_levels(dataset)

    analyze_remote_work(dataset)

    plot_remote_work(dataset)

if __name__ == "__main__":
    main()