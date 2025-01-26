# TASK 2
import pandas as pd

def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv("adult.data.csv", sep=',')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    races = df.groupby("race").count()
    races_list = list(df.groupby("race").count().index)
    race_count = pd.Series(data=list(races['age']), index=races_list)

    # What is the average age of men?
    average_age_men = df[df['sex']=='Male']['age'].mean()
    average_age_men = round(average_age_men, 1)

    # What is the percentage of people who have a Bachelor's degree?
    total_people = df.shape[0]
    bsc_holders = df[df['education']=='Bachelors'].count()['age']
    percentage_bachelors = round((bsc_holders / total_people * 100), 1)


    # What percentage of people have advanced education (`Bachelors`, `Masters`, or `Doctorate`)?
    higher_education = df[(df['education'] == 'Bachelors') | (df['education'] == 'Masters') | (df['education'] == 'Doctorate')]
    total_higher_ed = higher_education.shape[0]
    # What percentage of people without advanced education?
    lower_education = df[(df['education']!='Bachelors') & (df['education']!='Masters') & (df['education']!='Doctorate')]
    total_lower_ed = lower_education.shape[0]

    # percentage with salary >50K
    higher_education_rich = higher_education[higher_education['salary']=='>50K'].groupby('education').count()['age'].sum()
    higher_education_rich = round(((higher_education_rich / total_higher_ed) * 100), 1)

    lower_education_rich = lower_education[lower_education['salary']=='>50K'].groupby('education').count()['age'].sum()
    lower_education_rich = round(((lower_education_rich / total_lower_ed) * 100), 1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()
    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = df[df['hours-per-week'] == min_work_hours].count()['age']
    num_high_pay_min_workers = df[(df['hours-per-week'] == min_work_hours) & (df['salary'] == '>50K')].count()['age']
    rich_percentage = round(((num_high_pay_min_workers / num_min_workers) * 100),1)

    # What country has the highest percentage of people that earn >50K?
    countries = df[['native-country','salary', 'occupation']]
    total_occ_per_country = countries.groupby('native-country').count()['salary']
    highest = countries[countries['salary'] == '>50K'].groupby('native-country').count()['salary']

    highes_earning_pc_country = (highest.index[0], round(((highest[0]/total_occ_per_country[0])*100),1))
    for i in highest.index:
        percent = round(((highest[i]/total_occ_per_country[i])*100),1)
        if percent >= highes_earning_pc_country[1]:
            highes_earning_pc_country = (i, percent)

    highest_earning_country = highes_earning_pc_country[0]
    highest_earning_country_percentage = highes_earning_pc_country[1]

    # Identify the most popular occupation for those who earn >50K in India.
    india_by_occupation = countries[(countries['native-country'] == 'India') & (countries['salary'] == '>50K')].groupby('occupation').count()
    top_IN_occupation = india_by_occupation[india_by_occupation['salary'] == india_by_occupation.max()['salary']].index[0]

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
