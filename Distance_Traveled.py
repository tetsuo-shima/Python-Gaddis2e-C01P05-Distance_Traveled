__author__ = 'dwight'

# A car is traveling at 60 miles per hour. Write a program that displays the following:
#   • The distance the car will travel in 5 hours
#   • The distance the car will travel in 8 hours
#   • The distance the car will travel in 12 hours


def main():
    display_distance(5)
    display_distance(8)
    display_distance(12)


def calc_distance_60mph(hours):
    miles_per_hour = 60
    return hours * miles_per_hour


def display_distance(hours):
    print(hours, 'hours =', calc_distance_60mph(hours), 'miles')


main()