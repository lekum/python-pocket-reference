from enum import Enum

class Semaphore(Enum):
    Green = 0
    Red = 1
    Amber = 2


if __name__ == "__main__":

    for color in Semaphore:
        print(color.name, "=>", color.value)
    print()

    labor_days = Enum('labor_days', 'monday tuesday wednesday thursday friday')
    for day in labor_days:
        print(day.name, "=>", day.value)
