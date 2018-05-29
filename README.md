# sports-search-engine

1. Design a database structure (schema) that will fit your data model. Your data model is how the statistics for your sport are organized. If you can't think of a sport to analyze - give american football a try. Here is a link to the Nebraska Cornhuskers stats from 1983 (http://www.sports-reference.com/cfb/schools/nebraska/1983.html). Find the Rushing and Receiving table and create a database table structure that allows you to store that data inside of it.
2. Create a python file that will insert a sample of data (no more than 20 rows) into your database using the cursor.execute method with some INSERT statements. This .py file does not also need to contain the logic for your main program. Just allow it to be run by itself to create data.
3. Write a program that connects to the database and asks the user to search for a player. Start with just the name but think about further criteria you could include (position? age?). For a given result set, have the program display the results in a clean manner to the user.
4. Add a feature to your program that allows a user to insert new players into the database. Prompt the user for every column that you will need them to provide custom information on. Name?, Age?, etc.
