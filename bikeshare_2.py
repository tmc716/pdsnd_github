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
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    city=input("\nWhich city would you like data for: Chicago, new york city, or washington?\n").lower()
    while city not in ['chicago', 'new york city', 'washington']:
        print('That\'s not a valid city')
        city=input("\nWhich city would you like data for: Chicago, new york city, or washington?\n").lower()


    # get user input for month (all, january, february, ... , june)
    month=input("\nWhich month would you like data for: all, january, february, march, april, may, or june\n").lower()
    while month not in ['all', 'january', 'february', 'march', 'april', 'may', 'june']:
        print('That\'s not a valid month')
        month=input("\nWhich month would you like data for: all, january, february, march, april, may, or june\n").lower()


        # get user input for day of week (all, monday, tuesday, ... sunday)
    day=input("\nWhich day would you like data for: all, monday, tuesday, ...sunday\n").title()
    while day not in ['All', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']:
            print('That\'s not a valid day')
            day=input("\nWhich day would you like data for: all, monday, tuesday, ...sunday\n").title()
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
        month_in = months.index(month) + 1

       # filter by month to create the new dataframe
        df = df[df['month']==month_in]

   # filter by day of week if applicable
    if day != 'All':
       # filter by day of week to create the new dataframe
        df = df[df['day_of_week']==day]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print("Most common month: ", df['month'].mode()[0])

    # TO DO: display the most common day of week
    print("Most common day of the week: ", df['day_of_week'].mode()[0])

    # TO DO: display the most common start hour
    df['hour']=df['Start Time'].dt.hour
    print("Most common start hour: ", df['hour'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("Most popular start station: ", df['Start Station'].mode()[0])

    # TO DO: display most commonly used end station
    print("Most popular end station: ", df['End Station'].mode()[0])

    # TO DO: display most frequent combination of start station and end station trip
    df['Trip']=df['Start Station'] + " to " + df['End Station']
    print("Most popular combination of start and end station: ", df['Trip'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print("Total travel time: ", df['Trip Duration'].sum())

    # TO DO: display mean travel time
    print("Average travel time: ", df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print("Counts of user types: ")
    print(df['User Type'].value_counts())

    # TO DO: Display counts of gender
    if 'Gender' in df:
        print("Gender breakdown: ")
        print(df['Gender'].value_counts())
    else:
        print("Gender data is not available for this city")

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        print("Earliest year of birth: ", int(df['Birth Year'].min()))
        print("Most recent year of birth: ", int(df['Birth Year'].max()))
        print("Most common year of birth: ", int(df['Birth Year'].mode()))
    else:
        print("Birth year data is not available for this city")

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

        raw_data = input('\nWould you like to display 5 rows of data? Enter yes or no.\n')
        i = 0
        while raw_data.lower() == 'yes':
            print(df[i:i+5])
            raw_data = input('\nWould you like to display 5 more rows of data? Enter yes or no.\n')
            i += 5

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
