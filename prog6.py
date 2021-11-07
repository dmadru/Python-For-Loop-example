"""
prog6.py                     CAIS 117               Author: Dylan Madru

This program reads all of the lines of the file, "WorldSeriesWinners.txt" into a
list. It then determines the number of elements in the list and strips the
trailing newline character using a for loop. It then asks the user to input the
name of a baseball team. The program then checks to see if the team hasn't won
a World Series or else determines how many times they have won the World Series.
The result is then printed to the screen. The program then asks the user if they
would like to search for another team.
"""

#Place the definition of the description to the user here
def describe_program():
    print("""This program will be able to tell you how many times a certain
team has won the World Series! Once a team name is entered, the program will
check the team name against the database and print to the screen the results!
When entering team, use city and team name. eg. Boston Red Sox 
""")

#I have given this function for you to call in the main() function below
def again():
    response = 'X'
    print()
    while response != 'Y' and response != 'N':
        response = input("Do you wish to search for another team(Y for Yes, N for No)")
        response = response.upper()
        if response != 'Y' and response != 'N':
            print("Illegal response!  Answer Y for Yes or N for No!\n")
    return response


#Complete the body of the main() function as indcated by the comments
def main():

    #Call the function that describes the program to the user here
    describe_program()
    
    response = 'Y'
    while response == 'Y':
        
        # Set up and initialize variables
        team = ''   #team is a variable to hold the complete name of the
                    #team (city and team name)
        win_count = 0  #represents the number of world series won by team
        
        # Open the file for reading from the "WorldSeriesWinners.txt" file into
        # a list, winners.
        # Your code goes here!
        winners_obj = open("WorldSeriesWinners.txt",'r')

        winners = winners_obj.readlines()

        
       
        
        
        # Strip trailing newline characters from the elements of the list.
        #You will need to use a for loop here!  Hint!  Use the len() function
        #to find the size of the list and then step through the list using a for
        #loop
        #Your code goes here!
        size = len(winners)
        for i in range(size):
            winners[i] = winners[i].rstrip('\n')
            
    

        # Prompt and read from the user theteam desired to search.
        # Your code goes here
        team = input("What team would you like to search for? :")
        
        

        # Check if the team hasn't won any world series.
        # Else for each entry in the list check if entry is the team
        # searched increment the win count and then print the number of
        # times that the team has won the world series between 1903 and 2017.
        #Your code goes here!
        if team not in winners:
            print("The team you have entered has not won a world series!")
        else:
            for i in range(size):
                if team == winners[i]:
                    win_count+=1
            print("The",team,"have won the World Series",win_count,"times!")
            

        
        #This is the last statement in the while loop body
        response = again()
       
    print("\nThank you for using the program!")
    
# Call the main function.
main()

