# import all functions

import time
import pandas as pd
import numpy as np

# specify the scope of cities

CITY_SCOPE = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }

MONTHS = ['january', 'february', 'march', 'april', 'may', 'june']
CITIES = ['chicago', 'new york', 'washington']
DAYS = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

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
    while True:
      city = input('\nPlease, select city: Chicago, New York or Washington: ').lower()
      if city in CITIES:
         break
      else:
         print('\nPlease, try again')

    # get user input for month (all, january, february, ... , june)
    while True:
      month = input('\nPlease, select the month : All, January, February, March, April, May, June: ').lower()
      if month == "all":
         break
      elif month in MONTHS:
         break
      else:
         print('\nPlease, try again')

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
      day = input('\nPlease, select the day: All, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday: ').lower()
      if day.lower() == "all":
         break
      elif day in DAYS:
         break
      else:
         print('\nPlease, try again')

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
 # load data file into a dataframe
    df = pd.read_csv(CITY_SCOPE[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week and hour from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'all':
        month =  MONTHS.index(month) + 1
        df = df[ df['month'] == month ]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[ df['day_of_week'] == day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

     # display the most common month
    print("The most common month: {}".format(int(df['month'].mode().values[0])))

    # display the most common day of week
    print("The most common day of week: {}".format(str(df['day_of_week'].mode().values[0])))

    # display the most common start hour
    df['start_hour'] = df['Start Time'].dt.hour
    print("The most common start hour: {}".format(str(df['start_hour'].mode().values[0])))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print("The most common start station: {} ".format(df['Start Station'].mode().values[0]))

    # display most commonly used end station
    print("The most common end station: {}".format(df['End Station'].mode().values[0]))

    # display most frequent combination of start station and end station trip
    df['routes'] = df['Start Station']+ " " + df['End Station']
    print("The most common start and end station: {}".format(df['routes'].mode().values[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    
    # display total travel time
    print('Total Travel Time ',df['Trip Duration'].sum())

    # display mean travel time
    print('Mean Travel Time ',df['Trip Duration'].mean())


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
   

def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print("The counts of user types:")
    print(df['User Type'].value_counts())
    
    if 'Gender' in df.columns:
        # Display counts of gender
        print("Counts of gender:")
        print(df['Gender'].value_counts())

    
    if 'Birth Year' in df.columns:
        # Display earliest, most recent, and most common year of birth
        print("The earliest birth year: {}".format(str(int(df['Birth Year'].min()))))
        print("The latest birth year: {}".format(str(int(df['Birth Year'].max()))))
        print("The most common birth year: {}".format(str(int(df['Birth Year'].mode().values[0]))))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def display_result(df):
   
    start = 0
    end = 5

    display = input("Do you need the raw information (Yes or No)?: ").lower()

    if display == 'yes':
        while end <= df.shape[0] - 1:

            print(df.iloc[start:end,:])
            start += 5
            end += 5

            end_result = input("Do you want to continue (Yes or No)?: ").lower()
            if end_result == 'no':
                break

def main():

    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        display_result(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()