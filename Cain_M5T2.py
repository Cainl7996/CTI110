#Larissa Cain
#CTi 110
#10/9/2017
#M5T2_Bug Collector

def main():

#Initialize the accumulator
    totalBugs = 0
    days = 7

#Get bugs collected each day
    for days in range(1,8):
        print('Enter bugs collected', days)
        bugs = int(input())
        totalBugs += bugs

#Display total amount of bugs
    print('You have collected a total of ', totalBugs, 'bugs.')

main()
