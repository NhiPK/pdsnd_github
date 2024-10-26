import time
import pandas as pd
import numpy as np

"""Purpose: Use Python, Pandas, NumPy, to compare the system usage between three large cities: Chicago, New York City, and Washington, DC.
    by Pham Kha Nhi
    Project: Explore US Bikeshare Data
    Due Date: 22 Aug 2024
"""
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    
    valid_cities = ['chicago', 'new york city', 'washington']
    valid_months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
    valid_days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']

    while True:
        city = input("Please enter the city name (Chicago, New York City, Washington): ").lower()
        if city in valid_cities:
            break
        else:
            print("Invalid input. Please enter a valid city name.")
    
    # get user input for month (all, january, february, ... , june)    while True:
        month = input("Please enter the month (January to June) or 'all' for no filter: ").lower()
        if month in valid_months:
            break
        else:
            print("Invalid input. Please enter a month from January to June, or 'all'.")
    
    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Please enter the day of the week or 'all' for no filter: ").lower()
        if day in valid_days:
            break
        else:
            print("Invalid input. Please enter a valid day of the week or 'all'.")
    
    print('-'*40)
    return city, month, day

    # get user input for day of week (all, monday, tuesday, ... sunday)
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    filename = CITY_DATA[city]
    df = pd.read_csv(filename)

"""#1 Popular times of travel (i.e., occurs most often in the start time)
    most common month
    most common day of week
    most common hour of day"""

def get_popular_times(df):
    # Convert 'Start Time' to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Extract month, day of week, and hour
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # Define month names.
    month_names = ['January', 'February', 'March', 'April', 'May', 'June']

    # display the most common month
    most_common_month = df['month'].mode()[0]
    print(f"Most Common Month: {month_names[most_common_month - 1]}")


    # display the most common day of week
    most_common_day = df['day_of_week'].mode()[0]
    print(f"Most Common Day of Week: {most_common_day}")

    # display the most common start hour
    most_common_hour = df['hour'].mode()[0]
    print(f"Most Common Start Hour: {most_common_hour}:00")



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

"""#2 Popular stations and trip
    most common start station
    most common end station
    most common trip from start to end (i.e., most frequent combination of start station and end station)"""

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    most_common_start_station = df['Start Station'].mode()[0]
    print(f"Most Commonly Used Start Station: {most_common_start_station}")

    # display most commonly used end station
    most_common_end_station = df['End Station'].mode()[0]
    print(f"Most Commonly Used End Station: {most_common_end_station}")

    # display most frequent combination of start station and end station trip
    df['Trip Combination'] = df['Start Station'] + " to " + df['End Station']
    most_common_trip = df['Trip Combination'].mode()[0]
    print(f"Most Frequent Trip: {most_common_trip}")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

"""#3 Trip duration
    total travel time
    average travel time"""

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print(f"Total Travel Time: {total_travel_time} seconds")

    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print(f"Average Travel Time: {mean_travel_time} seconds")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

"""#4 User info

    counts of each user type
    counts of each gender (only available for NYC and Chicago)
    earliest, most recent, most common year of birth (only available for NYC and Chicago)"""

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_type_counts = df['User Type'].value_counts()
    print("Counts of each user type:")
    print(user_type_counts)

    # Display counts of gender
    if 'Gender' in df.columns:
        gender_counts = df['Gender'].value_counts()
        print("\nCounts of each gender:")
        print(gender_counts)
    else:
        print("\nGender data not available for this dataset.")

    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        earliest_year = int(df['Birth Year'].min())
        most_recent_year = int(df['Birth Year'].max())
        most_common_year = int(df['Birth Year'].mode()[0])
        print("\nEarliest year of birth:", earliest_year)
        print("Most recent year of birth:", most_recent_year)
        print("Most common year of birth:", most_common_year)
    else:
        print("\nBirth year data not available for this dataset.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
