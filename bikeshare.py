# US BIKESHARE PROJECT
#Exploration 

import time
import pandas as pd
import numpy as np

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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("Please enter the name of the city to analyze (Chicago, New York City, or Washington): ").strip().lower()
        if city in CITY_DATA:
            break
        else:
            print("Invalid city name. Please try again!")

    # TO DO: get user input for month (all, january, february, ... , june)
    # Make sure you include all months 
    while True:
        month = input("Please enter the name of the month to filter by, or 'all' to apply no month filter: ").strip().lower()
        months_list = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december', 'all']
        if month in months_list:
            break
        else:
            print("Invalid month input. Please try again.")
            
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Please enter the name of the day of the week to filter by, or 'all' to apply no day filter: ").strip().lower()
        days_list = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']
        if day in days_list:
            break
        else:
            print("Invalid day input. Please try again.")
        

    print('-'*40)
    return city, month, day

def display_data(df):
    """ask the user if they want to see 5 rows of data. 
    After showing all parts of the analysis, ask this question: 
    'Do you want to see 5 rows of data?'. 
    The data displayed should not be limited to the first 5 rows, 
    but should continue to show the next 5 rows each time 
    the user says 'yes'. For example, in the first step you might
    ask, 'Do you want to see the first 5 rows of data?'. 
    If the user says 'yes', show the first 5 rows, then ask, 
    'Do you want to see the next 5 rows of data?'. 
    If the user again says 'yes', show the next 5 rows. 
    Continue this until the user enters 'no'. 
    

    Args:
        df (_type_): _description_
    """
    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n').lower()
    start_loc = 0
    while view_data == 'yes':
        print(df.iloc[start_loc:start_loc+5])
        start_loc += 5
        view_data = input("Do you wish to continue?: ").lower()
    
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
    df = pd.read_csv(CITY_DATA[city])
    
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # extract month and day of week from Start Time to create new columns
    df['Month'] = df['Start Time'].dt.month
    df['Day of Week'] = df['Start Time'].dt.day_name()
    df['Hour'] = df['Start Time'].dt.hour
    # filter by month if applicable
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
        # use the index of the months list to get the corresponding int
        month = months.index(month) + 1
        # filter by month to create the new dataframe
        df = df[df['Month'] == month]
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['Day of Week'] == day.title()]  
        
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    # Most common month
    most_common_month = df['Month'].mode()[0]

    # TO DO: display the most common day of week
    most_common_day = df['Day of Week'].mode()[0]

    # TO DO: display the most common start hour
    most_common_hour = df['Hour'].mode()[0]

    print("-------------------------------------------------")
    print("Most common month:", most_common_month)
    print("Most common day of the week:", most_common_day)
    print("Most common start hour:", most_common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start_station = df['Start Station'].mode()[0]

    # TO DO: display most commonly used end station
    most_common_end_station = df['End Station'].mode()[0]

    # TO DO: display most frequent combination of start station and end station trip
    most_common_trip = df.groupby(['Start Station', 'End Station']).size().idxmax()
    
    print("-------------------------------------------------")
    print("Most common start station:", most_common_start_station)
    print("Most common end station:", most_common_end_station)
    print("Most common trip:", most_common_trip)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_trip_duration = df['Trip Duration'].sum()


    # TO DO: display mean travel time
    average_trip_duration = df['Trip Duration'].mean()
                  
    print("-------------------------------------------------")
    print("Total trip duration:", total_trip_duration)
    print("Average trip duration:", average_trip_duration)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types_count = df['User Type'].value_counts()
    print("Counts of User Types:", user_types_count)
    
    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        gender_count = df['Gender'].value_counts()
        print("Counts of Gender:", gender_count)
    else:
        gender_count = None
        print("Gender information not available for the selected city")

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
    # Earliest birth year
        earliest_birth_year = int(df['Birth Year'].min())
    # Most recent birth year
        most_recent_birth_year = int(df['Birth Year'].max())
    # Most common birth year
        most_common_birth_year = int(df['Birth Year'].mode()[0])
        
        print("Earliest birth year:", earliest_birth_year)
        print("Most recent birth year:", most_recent_birth_year)
        print("Most common birth year:", most_common_birth_year)
    else:
        print("Birth Year information not available for the selected city")
                     
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        
        display_data(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
