# Josephus-Problem
Solution to the Josephus problem using the binary method with lists, strings and int convertions in python

## What is the Josephus problem?
[![Josephus Problem](https://img.youtube.com/vi/uCsD3ZGzMgE/0.jpg)](https://www.youtube.com/watch?v=uCsD3ZGzMgE "Josephus Problem")
> All the credits to the owner of the video and to the Youtube channel "Numberphile"

### How it works?
I know it could be better, but as a first try to code and search in stackoverflow for understand basics of Computer Science, I did this, know, how it works, at the first the console request the user an integer number that is going to represent the amount of persons in the circle, then we start with the main function, we have the "binary_int" variable that converts our number of persons into a binary number, and then convert it into a string into the "binary_string" variable, we create an empty list becase we need to modify the binary number, and we can't change a string, but a list is perfect for this, and we fill our "list" with the string containing the binary number, we create a copy of our list called "answer_list" and create a variable called "first_element" containing the first term of our binary number, we delete the first number of our "answer_list" and append the first element we just saved into "first_elemet", now we just convert it into a string and this string into a decimal number, changing the binary code to our last standing person in the circle ;)
