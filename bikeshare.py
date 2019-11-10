import time
import pandas as pd
import numpy as np

#Sam Subbukumar
#Udacity Python project
#11/4/2019


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
    While True:   
        city = input("Enter the city: ").lower()
        if city not in ['chicago', 'new york city', 'washington']
            print('Please enter a valid city name')
        else:
            break
         


    # TO DO: get user input for month (all, january, february, ... , june)
While True:
    month = input("Enter the month").lower()
    if month not in ['all', 'january', 'february', 'march', 'april', 'may', 'june']
        print('Enter a valid month')
    else:
        break
  

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
While True: 
    weekday = input("Enter the weekday").lower()
    if weekday not in ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        print('Enter a valid weekday')
    else:
        break
 

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
        df - pandas DataFrame containing city data filtered by month and day
    """
    
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name


    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
    
        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    
   return df
    


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()
    print(popular_month)
    # TO DO: display the most common day of week
    popular_day = df['start_time'].dt.weekday_name.mode()
    print(popular_day)
    # TO DO: display the most common start hour
    popular_hour = df['start_time'].dt.hour.mode()[0]
    print(popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()
    print(popular_start_station)
    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()
    print(popular_end_station)
    # TO DO: display most frequent combination of start station and end station trip
    popular_combination = (df['Start Station'] + ", " + df['End Station']).mode()
    print(popular_combination)
   

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
#I learned about sum() and mean() from geeksforgeeks.com
    # TO DO: display total travel time
    tot_duration = df['Trip Duration'].sum()
    print(tot_duration)

    # TO DO: display mean travel time
    mean_duration = df['Trip Duration'].mean()
    print(mean_duration)
          
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)
    # TO DO: Display counts of gender
    # I got help here from https://knowledge.udacity.com/questions/55524
    if gender in df.columns:  
       gender_counts = df['Gender'].value_counts()
       print(gender_counts)
    else:
       print("Washington does not have gender data")
        
    # TO DO: Display earliest, most recent, and most common year of birth
    #I learned about min() and max() from geeksforgeeks.com
    earliest_year = df['year'].min()
    most_recent_year = df['year'].max()
    common_year = df['year'].mode()[0]
    print("Earliest year: ", earliest_year)
    print("Most recent year: ", most_recent_year)
    print("Most common year: " , common_year)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
#I got help here from this Knowledge Question: https://knowledge.udacity.com/questions/26261
five_rows = input("Would you like to see the first five rows of the data? Yes, or no?").lower()
    if five_rows in 'yes':
        i = 1
        While True:
            print(df.iloc[i:i+4])
            i = i + 5
            more_lines = input("Would you like to see the next five lines? Yes or no?").lower()
            if more_lines not in 'yes':
                break
                
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
