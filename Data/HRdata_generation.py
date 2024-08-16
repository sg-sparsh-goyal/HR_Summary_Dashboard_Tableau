import pandas as pd
import numpy as np
from faker import Faker
from datetime import datetime, timedelta
import random

# Initialize Faker
fake = Faker('en_IN')
Faker.seed(42)
np.random.seed(42)
random.seed(42)

# Configuration
num_records = 8950

# States & Cities
states_cities = {
    'Maharashtra': ['Mumbai', 'Pune', 'Nagpur'],
    'Tamil Nadu': ['Chennai', 'Coimbatore', 'Madurai'],
    'Karnataka': ['Bangalore', 'Mysore', 'Mangalore'],
    'Gujarat': ['Ahmedabad', 'Surat', 'Vadodara'],
    'Rajasthan': ['Jaipur', 'Jodhpur', 'Udaipur'],
    'West Bengal': ['Kolkata', 'Howrah', 'Durgapur'],
    'Uttar Pradesh': ['Lucknow', 'Kanpur', 'Varanasi'],
    'Punjab': ['Chandigarh', 'Ludhiana', 'Amritsar']
}
states = list(states_cities.keys())
state_prob = [0.7, 0.02, 0.01, 0.03, 0.05, 0.03, 0.05, 0.11]
assigned_states = np.random.choice(states, size=num_records, p=state_prob)
assigned_cities = [np.random.choice(states_cities[state]) for state in assigned_states]

# Departments & Jobtitles
departments = ['HR', 'IT', 'Sales', 'Marketing', 'Finance', 'Operations', 'Customer Service']
departments_prob = [0.02, 0.15, 0.21, 0.08, 0.05, 0.30, 0.19]
jobtitles = {
    'HR': ['HR Manager', 'HR Coordinator', 'Recruiter', 'HR Assistant'],
    'IT': ['IT Manager', 'Software Developer', 'System Administrator', 'IT Support Specialist'],
    'Sales': ['Sales Manager', 'Sales Consultant', 'Sales Specialist', 'Sales Representative'],
    'Marketing': ['Marketing Manager', 'SEO Specialist', 'Content Creator', 'Marketing Coordinator'],
    'Finance': ['Finance Manager', 'Accountant', 'Financial Analyst', 'Accounts Payable Specialist'],
    'Operations': ['Operations Manager', 'Operations Analyst', 'Logistics Coordinator', 'Inventory Specialist'],
    'Customer Service': ['Customer Service Manager', 'Customer Service Representative', 'Support Specialist', 'Help Desk Technician']
}
jobtitles_prob = {
    'HR': [0.03, 0.3, 0.47, 0.2],  # HR Manager, HR Coordinator, Recruiter, HR Assistant
    'IT': [0.02, 0.47, 0.2, 0.31],  # IT Manager, Software Developer, System Administrator, IT Support Specialist
    'Sales': [0.03, 0.25, 0.32, 0.4],  # Sales Manager, Sales Consultant, Sales Specialist, Sales Representative
    'Marketing': [0.04, 0.25, 0.41, 0.3],  # Marketing Manager, SEO Specialist, Content Creator, Marketing Coordinator
    'Finance': [0.03, 0.37, 0.4, 0.2],  # Finance Manager, Accountant, Financial Analyst, Accounts Payable Specialist
    'Operations': [0.02, 0.2, 0.4, 0.38],  # Operations Manager, Operations Analyst, Logistics Coordinator, Inventory Specialist
    'Customer Service': [0.04, 0.3, 0.38, 0.28]  # Customer Service Manager, Customer Service Representative, Support Specialist, Help Desk Technician
}

# Educations
educations = ['High School', "Bachelor", "Master", 'PhD']

education_mapping = {
    'HR Manager': ["Master", "PhD"],
    'HR Coordinator': ["Bachelor", "Master"],
    'Recruiter': ["High School", "Bachelor"],
    'HR Assistant': ["High School", "Bachelor"],
    'IT Manager': ["PhD", "Master"],
    'Software Developer': ["Bachelor", "Master"],
    'System Administrator': ["Bachelor", "Master"],
    'IT Support Specialist': ["High School", "Bachelor"],
    'Sales Manager': ["Master","PhD"],
    'Sales Consultant': ["Bachelor", "Master", "PhD"],
    'Sales Specialist': ["Bachelor", "Master", "PhD"],
    'Sales Representative': ["Bachelor"],
    'Marketing Manager': ["Bachelor", "Master","PhD"],
    'SEO Specialist': ["High School", "Bachelor"],
    'Content Creator': ["High School", "Bachelor"],
    'Marketing Coordinator': ["Bachelor"],
    'Finance Manager': ["Master", "PhD"],
    'Accountant': ["Bachelor"],
    'Financial Analyst': ["Bachelor", "Master", "PhD"],
    'Accounts Payable Specialist': ["Bachelor"],
    'Operations Manager': ["Bachelor", "Master"],
    'Operations Analyst': ["Bachelor", "Master"],
    'Logistics Coordinator': ["Bachelor"],
    'Inventory Specialist': ["High School", "Bachelor"],
    'Customer Service Manager': ["Bachelor", "Master", "PhD"],
    'Customer Service Representative': ["High School", "Bachelor"],
    'Support Specialist': ["High School", "Bachelor"],
    'Customer Success Manager': ["Bachelor", "Master", "PhD"],
    'Help Desk Technician': ["High School", "Bachelor"]
}

# Hiring Date
# Define custom probability weights for each year
year_weights = {
    2015: 5,   # 15% probability
    2016: 8,   # 15% probability
    2017: 17,   # 20% probability
    2018: 9,  # 15% probability
    2019: 10,  # 10% probability
    2020: 11,  # 10% probability
    2021: 5,  # 8% probability
    2022: 12,  # 5% probability
    2023: 14,  # 2% probability
    2024: 9   # 2% probability
}


# Generate a random date based on custom probabilities
def generate_custom_date(year_weights):
    year = random.choices(list(year_weights.keys()), weights=list(year_weights.values()))[0]
    month = random.randint(1, 12)
    day = random.randint(1, 28)  # Assuming all months have 28 days for simplicity
    return fake.date_time_between(start_date=datetime(year, 1, 1), end_date=datetime(year, 12, 31))

def generate_salary(department, job_title):
    salary_dict = {
            'HR': {
                'HR Manager': np.random.randint(60000, 90000),
                'HR Coordinator': np.random.randint(50000, 60000),
                'Recruiter': np.random.randint(50000, 70000),
                'HR Assistant': np.random.randint(50000, 60000)
            },
            'IT': {
                'IT Manager': np.random.randint(80000, 120000),
                'Software Developer': np.random.randint(70000, 95000),
                'System Administrator': np.random.randint(60000, 90000),
                'IT Support Specialist': np.random.randint(50000, 60000)
            },
            'Sales': {
                'Sales Manager': np.random.randint(70000, 110000),
                'Sales Consultant': np.random.randint(60000, 90000),
                'Sales Specialist': np.random.randint(50000, 80000),
                'Sales Representative': np.random.randint(50000, 70000)
            },
            'Marketing': {
                'Marketing Manager': np.random.randint(70000, 100000),
                'SEO Specialist': np.random.randint(50000, 80000),
                'Content Creator': np.random.randint(50000, 60000),
                'Marketing Coordinator': np.random.randint(50000, 70000)
            },
            'Finance': {
                'Finance Manager': np.random.randint(80000, 120000),
                'Accountant': np.random.randint(50000, 80000),
                'Financial Analyst': np.random.randint(60000, 90000),
                'Accounts Payable Specialist': np.random.randint(50000, 60000)
            },
            'Operations': {
                'Operations Manager': np.random.randint(70000, 100000),
                'Operations Analyst': np.random.randint(50000, 80000),
                'Logistics Coordinator': np.random.randint(50000, 60000),
                'Inventory Specialist': np.random.randint(50000, 60000)
            },
            'Customer Service': {
                'Customer Service Manager': np.random.randint(60000, 90000),
                'Customer Service Representative': np.random.randint(50000, 60000),
                'Support Specialist': np.random.randint(50000, 60000),
                'Help Desk Technician': np.random.randint(50000, 80000)
            }
        }
    return salary_dict[department][job_title]

# Generate the dataset
data = []

for _ in range(num_records):
    employee_id = f"00-{random.randint(10000000, 99999999)}"
    first_name = fake.first_name()
    last_name = fake.last_name()
    dob = fake.date_of_birth(minimum_age=18, maximum_age=60)
    state = np.random.choice(states, p=state_prob)
    city = np.random.choice(states_cities[state])
    department = np.random.choice(departments, p=departments_prob)
    job_title = np.random.choice(jobtitles[department], p=jobtitles_prob[department])
    education = np.random.choice(education_mapping[job_title])
    hiring_date = generate_custom_date(year_weights)
    salary = generate_salary(department, job_title)

    data.append([
        employee_id,
        first_name,
        last_name,
        dob,
        state,
        city,
        department,
        job_title,
        education,
        hiring_date,
        salary
    ])

# Create DataFrame
columns = [
    "EmployeeID",
    "FirstName",
    "LastName",
    "DOB",
    "State",
    "City",
    "Department",
    "JobTitle",
    "Education",
    "HiringDate",
    "Salary"
]
df = pd.DataFrame(data, columns=columns)

# Save to CSV
df.to_csv("synthetic_employee_data_india.csv", index=False)
print("Data generation complete.")
