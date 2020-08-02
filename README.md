# Nobel_Prize_Data_Mining_Python

PART 1:
Implement a function report(), which takes as input the json file loaded as a Python dictionary (which is the default data structure returned by the json.load() method). This
function should return a Pandas DataFrame, where you include the years and categories in which a Nobel Prize was awarded and those in which it was not. You are not expected to
infer any missing information, you should only include years and categories for which there is an explicit entry in the original dataset

PART 2:
Write a function get_laureates_and_motivation() which takes as input three arguments: the nobel prize dictionary , year (a string) and category (a
string). This function returns a Pandas DataFrame containing one row per laureate (i.e., a person who has won the Nobel prize).

PART 3:
Write a function plot_freqs() which generates six plots, one for each category. The xaxis should contain the 1st, 10th, 20th, 30th, 40th and 50th most frequent word across the
motivation sections for each category. The y-axis should refer to the frequency of each word in that category.
