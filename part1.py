"""
Part 1: Data Processing in Pandas

=== Instructions ===

There are 22 questions in this part.
For each part you will implement a function (q1, q2, etc.)
Each function will take as input a data frame
or a list of data frames and return the answer
to the given question.

To run your code, you can run `python3 part1.py`.
This will run all the questions that you have implemented so far.
It will also save the answers to part1-answers.txt.

=== Dataset ===

In this part, we will use a dataset of world university rankings
called the "QS University Rankings".

The ranking data was taken 2019--2021 from the following website:
https://www.topuniversities.com/university-rankings/world-university-rankings/2021

=== Grading notes ===

- Once you have completed this part, make sure that
  your code runs, that part1-answers.txt is being re-generated
  every time the code is run, and that the answers look
  correct to you.

- Be careful about output types. For example if the question asks
  for a list of DataFrames, don't return a numpy array or a single
  DataFrame. When in doubt, ask on Piazza!

- Make sure that you remove any NotImplementedError exceptions;
  you won't get credit for any part that raises this exception
  (but you will still get credit for future parts that do not raise it
  if they don't depend on the previous parts).

- Make sure that you fill in answers for the parts
  marked "ANSWER ___ BELOW" and that you don't modify
  the lines above and below the answer space.

- Q6 has a few unit tests to help you check your work.
  Make sure that you removed the `@pytest.mark.skip` decorators
  and that all tests pass (show up in green, no red text!)
  when you run `pytest part3.py`.

- For plots: There are no specific requirements on which
  plotting methods you use; if not specified, use whichever
  plot you think might be most appropriate for the data
  at hand.
  Please ensure your plots are labeled and human-readable.
  For example, call .legend() on the plot before saving it!

===== Questions 1-6: Getting Started =====

To begin, let's load the Pandas library.
"""

import pandas as pd
import os

"""
1. Load the dataset into Pandas

Our first step is to load the data into a Pandas DataFrame.
We will also change the column names
to lowercase and reorder to get only the columns we are interested in.

Implement the rest of the function load_input()
by filling in the parts marked TODO below.

Return as your answer to q1 the number of dataframes loaded.
(This part is implemented for you.)
"""

os.makedirs('output', exist_ok=True)
ANSWER_FILE = "output/part1-answers.txt"
# Create the part1-answers.txt file if it doesn't exist
if not os.path.exists(ANSWER_FILE):
    with open(ANSWER_FILE, 'w') as f:
        pass

NEW_COLUMNS = ['rank', 'university', 'region', 'academic reputation', 'employer reputation', 'faculty student', 'citations per faculty', 'overall score']

def load_input():
    """
    Input: None
    Return: a list of 3 dataframes, one for each year.
    """

    # Load the input files and return them as a list of 3 dataframes.
    df_2019 = pd.read_csv('data/2019.csv', encoding='latin-1')
    df_2020 = pd.read_csv('data/2020.csv', encoding='latin-1')
    df_2021 = pd.read_csv('data/2021.csv', encoding='latin-1')

    # Standardizing the column names
    df_2019.columns = df_2019.columns.str.lower()
    df_2020.columns = df_2019.columns.str.lower()
    df_2021.columns = df_2019.columns.str.lower()

    # Restructuring the column indexes
    # Fill out this part. You can use column access to get only the
    # columns we are interested in using the NEW_COLUMNS variable above.
    # Make sure you return the columns in the new order.
    # TODO
    df_2019 = df_2019.drop(columns = ['international faculty', 'international students'])
    df_2020 = df_2020.drop(columns = ['international faculty', 'international students'])
    df_2021 = df_2021.drop(columns = ['international faculty', 'international students'])
    

    # When you are done, remove the next line...
    # raise NotImplementedError

    # ...and keep this line to return the dataframes.
    return [df_2019, df_2020, df_2021]

def q1(dfs):
    # As the "answer" to this part, let's just return the number of dataframes.
    # Check that your answer shows up in part1-answers.txt.
    return len(dfs)

"""
2. Input validation

Let's do some basic sanity checks on the data for Q1.

Check that all three data frames have the same shape,
and the correct number of rows and columns in the correct order.

As your answer to q2, return True if all validation checks pass,
and False otherwise.
"""

def q2(dfs):
    """
    Input: Assume the input is provided by load_input()

    Return: True if all validation checks pass, False otherwise.

    Make sure you return a Boolean!
    From this part onward, we will not provide the return
    statement for you.
    You can check that the "answers" to each part look
    correct by inspecting the file part1-answers.txt.
    """
    # Check:
    # - that all three dataframes have the same shape
    # remember that the dataframes have been loaded and placed into an array, dfs
    shape_check = dfs[0].shape == dfs[1].shape == dfs[2].shape
  
    # - the number of rows (0 in the brackets represents the rows)
    rows_check = dfs[0].shape[0] == dfs[1].shape[0] == dfs[2].shape[0]
  
    # - the number of columns (1 in the brackets represents the columns)
    columns_check = dfs[0].shape[1] == dfs[1].shape[1] == dfs[2].shape[1]
  
    # - the columns are listed in the correct order
    order_check = list(dfs[0].columns) == list(dfs[1].columns) == list(dfs[2].columns)

    # check that all the checks are true
    sanity_check = rows_check == columns_check == order_check

    # raise NotImplementedError

    return sanity_check

"""
===== Interlude: Checking your output so far =====

Run your code with `python3 part1.py` and open up the file
output/part1-answers.txt to see if the output looks correct so far!

You should check your answers in this file after each part.

You are welcome to also print out stuff to the console
in each question if you find it helpful.
"""

ANSWER_FILE = "output/part1-answers.txt"

def interlude():
    print("Answers so far:")
    with open(f"{ANSWER_FILE}") as fh:
        print(fh.read())

"""
===== End of interlude =====

3a. Input validation, continued

Now write a validate another property: that the set of university names
in each year is the same.
As in part 2, return a Boolean value.
(True if they are the same, and False otherwise)

Once you implement and run your code,
remember to check the output in part1-answers.txt.
(True if the checks pass, and False otherwise)
"""

def q3(dfs):
    # Check:
    # - that the set of university names in each year is the same
    # Return:
    # - True if they are the same, and False otherwise.

    # re-combine the data frames in the list into one dataframe
    # dfs = pd.concat(dfs, ignore_index = True)


    # create a reference set to compare the others to, take the first year
    reference_set = set(dfs[0]['university'].unique())

    # compare the reference set to the others through iteration
    for df in dfs [1:]:
      current_set = set(df['university'].unique())

      if current_set != reference_set:
        return False

    return True
    
    # raise NotImplementedError

"""
3b (commentary).
Did the checks pass or fail?
Comment below and explain why.

=== ANSWER Q3b BELOW ===

All the previous checks passed, except for this one. 
The check to see if each year had the same universities did not pass because it makes sense for rankings to change. 
Especially since there might bed different placements for the universities near the 100th ranking. 

=== END OF Q3b ANSWER ===
"""

"""
4. Random sampling

Now that we have the input data validated, let's get a feel for
the dataset we are working with by taking a random sample of 5 rows
at a time.

Implement q4() below to sample 5 points from each year's data.

As your answer to this part, return the *university name*
of the 5 samples *for 2021 only* as a list.
(That is: ["University 1", "University 2", "University 3", "University 4", "University 5"])

Code design: You can use a for for loop to iterate over the dataframes.
If df is a DataFrame, df.sample(5) returns a random sample of 5 rows.

Hint:
    to get the university name:
    try .iloc on the sample, then ["university"].
"""

def q4(dfs):
    # Sample 5 rows from 2021
    # Print out the samples
    # raise NotImplementedError

    samples = dfs[2].sample(5)
    university_samples = samples['university'].tolist()

    # Answer as a list of 5 university names
    return university_samples

"""
Once you have implemented this part,
you can run a few times to see different samples.

4b (commentary).
Based on the data, write down at least 2 strengths
and 3 weaknesses of this dataset.

=== ANSWER Q4b BELOW ===
Strengths:
1. The data is organized according to year, it is easier to find items in a date-sense.
2. You can find information based on ranking, each ranking represents a row that has the university name and following information.

Weaknesses:
1. It is hard to find a university by name.
2. It will be very difficult to find what one university placed as each year. 
3. No telling how many places a university moved in placement each year.
=== END OF Q4b ANSWER ===
"""

"""
5. Data cleaning

Let's see where we stand in terms of null values.
We can do this in two different ways.

a. Use .info() to see the number of non-null values in each column
displayed in the console.

b. Write a version using .count() to calculate the number of
non-null values in each column.

In both 5a and 5b: return as your answer
*for the 2021 data only*
as a list of the number of non-null values in each column.

Example: if there are 5 non-null values in the first column, 3 in the second, 4 in the third, and so on, you would return
    [5, 3, 4, ...]
"""

def q5a(dfs):
    # TODO
    # raise NotImplementedError
    # Remember to return the list here
    # (Since .info() does not return any values,
    # for this part, you will need to copy and paste
    # the output as a hardcoded list.)

    # use .info() to check how many non-null values there are for each column
    non_null_values = dfs[2].info()

    return [100, 100, 100, 100, 100, 100, 100, 100]

def q5b(dfs):
    # TODO
    # raise NotImplementedError
    # Remember to return the list here

    non_null_values = dfs[2].count()

    return [100, 100, 100, 100, 100, 100, 100, 100]

"""
5c.
One other thing:
Also fill this in with how many non-null values are expected.
We will use this in the unit tests below.
"""

def q5c():
    # raise NotImplementedError
    # TODO: fill this in with the expected number
    num_non_null = 100
    return num_non_null

"""
===== Interlude again: Unit tests =====

Unit tests

Now that we have completed a few parts,
let's talk about unit tests.
We won't be using them for the entire assignment
(in fact we won't be using them after this),
but they can be a good way to ensure your work is correct
without having to manually inspect the output.

We need to import pytest first.
"""

import pytest

"""
The following are a few unit tests for Q1-5.

To run the unit tests,
first, remove (or comment out) the `@pytest.mark.skip` decorator
from each unit test (function beginning with `test_`).
Then, run `pytest part1.py` in the terminal.
"""

# @pytest.mark.skip
def test_q1():
    dfs = load_input()
    assert len(dfs) == 3
    assert all([isinstance(df, pd.DataFrame) for df in dfs])

# @pytest.mark.skip
def test_q2():
    dfs = load_input()
    assert q2(dfs)

# @pytest.mark.skip
def test_q3():
    dfs = load_input()
    assert q3(dfs) == False

# @pytest.mark.skip
def test_q4():
    dfs = load_input()
    samples = q4(dfs)
    assert len(samples) == 5

# @pytest.mark.skip
def test_q5():
    dfs = load_input()
    answers = q5a(dfs) + q5b(dfs)
    assert len(answers) > 0
    num_non_null = q5c()
    for x in answers:
        assert x == num_non_null

"""
6a. Are there any tests which fail?

=== ANSWER Q6a BELOW ===

None of the tests failed.

=== END OF Q6a ANSWER ===

6b. For each test that fails, is it because your code
is wrong or because the test is wrong?

=== ANSWER Q6b BELOW ===

  Before having all the tests pass, I had some fail. 
  This was mostly due to q3 and q5. q3 was not returning the right kind of list because all of the values were returned as 1 index in the list.
  q5 was not working because .count() returned a list that included the column names in addition to the number of non-null values. This caused an error. 

=== END OF Q6b ANSWER ===

IMPORTANT: for any failing tests, if you think you have
not made any mistakes, mark it with
@pytest.mark.xfail
above the test to indicate that the test is expected to fail.
Run pytest part1.py again to see the new output.

6c. Return the number of tests that failed, even after your
code was fixed as the answer to this part.
(As an integer)
Please include expected failures (@pytest.mark.xfail).
(If you have no failing or xfail tests, return 0.)
"""

def q6c():
    # TODO
    # raise NotImplementedError

    return 2

"""
===== End of interlude =====

===== Questions 7-10: Data Processing =====

7. Adding columns

Notice that there is no 'year' column in any of the dataframe. As your first task, append an appropriate 'year' column in each dataframe.

Append a column 'year' in each dataframe. It must correspond to the year for which the data is represented.

As your answer to this part, return the number of columns in each dataframe after the addition.
"""

def q7(dfs):
    # TODO
    # raise NotImplementedError
    # Remember to return the list here

    # set this to be the values in year column
    current_year = 2019

    # use for loop to add into each data frame
    for df in dfs:
        # np.nan is for numerical values, None is for null values, and '' is for strings
        df['year'] = current_year

        # add 1 year to current_year for next year's data frame
        current_year = current_year + 1

    return dfs

"""
8a.
Next, find the count of universities in each region that made it to the Top 100 each year. Print all of them.

As your answer, return the count for "USA" in 2021.
"""

def q8a(dfs):
    # Enter Code here
    # TODO
    # raise NotImplementedError
    # Remember to return the count here

    # re-combine the data frames in the list into one dataframe
    dfs = pd.concat(dfs, ignore_index = True)

    # filter by year first 
    only_2021 = dfs[dfs['year'] == 2021]

    # filter by USA next
    only_USA_2021 = only_2021[only_2021['region'] == 'USA']

    # count how many universities
    count_USA_2021 = only_USA_2021['university'].count()

    return count_USA_2021

  

"""
8b.
Do you notice some trend? Comment on what you observe and why might that be consistent throughout the years.

=== ANSWER Q8b BELOW ===

  A trend that I notice is that a lot of the universities tend to remain close to where they placed in the rankings the previous year.
  Although the universities near the 100th ranking tend to be more mobile.
  
=== END OF Q8b ANSWER ===
"""

"""
9.
From the data of 2021, find the average score of all attributes for all universities.

As your answer, return the list of averages (for all attributes)
in the order they appear in the dataframe:
academic reputation, employer reputation, faculty student, citations per faculty, overall score.

The list should contain 5 elements.
"""

def q9(dfs):
    # Enter code here
    # TODO
    # raise NotImplementedError
    # Return the list here

    # take out df of rankings of 2021
    df_2021 = dfs[2]

    # filter out columns to only the ones we need
    need_df_2021 = df_2021[['academic reputation', 'employer reputation', 'faculty student', 'citations per faculty', 'overall score']]

    # calculate th means of each column
    # axis = 0 makes it so it calculates for the columns, axis = 1 is for rows
    column_means_2021 = need_df_2021.mean(axis = 0).tolist()

    return column_means_2021

"""
10.
From the same data of 2021, now find the average of *each* region for **all** attributes **excluding** 'rank' and 'year'.

In the function q10_helper, store the results in a variable named **avg_2021**
and return it.

Then in q10, print the first 5 rows of the avg_2021 dataframe.
"""

def q10_helper(dfs):
    # Enter code here
    # TODO

    # get the dataframe with only 2021
    df_2021 = dfs[2]

    # group the data according to region
    df_2021_region = df_2021.groupby('region')

    # keep only needed attributes
    df_2021_region_needed = df_2021_region[['academic reputation', 'employer reputation', 'faculty student', 'citations per faculty', 'overall score']]

    # calculate the average of each column
    # no need to specify the axis in mean() because the values are already grouped, and it will return an error
    avg_2021_fetus = df_2021_region_needed.mean()
    
    # Placeholder for the avg_2021 dataframe
    avg_2021 = pd.DataFrame(avg_2021_fetus)
  
    return avg_2021

def q10(avg_2021):
    """
    Input: the avg_2021 dataframe
    Print: the first 5 rows of the dataframe

    As your answer, simply return the number of rows printed.
    (That is, return the integer 5)
    """
    # Enter code here
    # raise NotImplementedError

    # get only the first 5 rows
    # head() automatically returns the first 5 rows
    avg_2021_head = avg_2021.head()
  
    # return 5
    return avg_2021_head

"""
===== Questions 11-14: Exploring the avg_2021 dataframe =====

11.
Sort the avg_2021 dataframe from the previous question based on overall score in a descending fashion (top to bottom).

As your answer to this part, return the first row of the sorted dataframe.
"""

def q11(avg_2021):
    # raise NotImplementedError

    # sort rows based on overall score in descending order
    avg_2021_score_desc = avg_2021.sort_values(by = 'overall score', ascending = False)

    # return only the first row of sorted dataframe
    return avg_2021_score_desc.iloc[0]

"""
12a.
What do you observe from the table above? Which country tops the ranking?

What is one country that went down in the rankings
between 2019 and 2021?

You will need to load the data from 2019 to get the answer to this part.
You may choose to do this
by writing another function like q10_helper and running q11,
or you may just do it separately
(e.g., in a Python shell) and return the name of the country/region
that you found went down in the rankings.

Errata: please note that the 2021 dataset we provided is flawed
(it is almost identical to the 2020 data).
This is why the question now asks for the difference between 2019 and 2021.
Your answer to which country/region went down will not be graded.

For the answer to this part return the name of the country/region that tops the ranking
and the name of one country/region that went down in the rankings.
"""

# use q12_helper to calculate the average of all attributes according to region of 2019 rankings dataframe
def q12_helper(dfs):
    # get the dataframe with only 2019
    df_2019 = dfs[0]

    # group the data according to region
    df_2019_region = df_2019.groupby('region')

    # keep only needed attributes
    df_2019_region_needed = df_2019_region[['academic reputation', 'employer reputation', 'faculty student', 'citations per faculty', 'overall score']]

    # calculate the average of each column
    # no need to specify the axis in mean() because the values are already grouped, and it will return an error
    avg_2019_fetus = df_2019_region_needed.mean()
    
    # Placeholder for the avg_2021 dataframe
    avg_2019 = pd.DataFrame(avg_2019_fetus)
  
    return avg_2019

# use q12 to calculate the overall score of 2019 in descending order
def q12(avg_2019):
    # raise NotImplementedError

    # sort rows based on overall score in descending order
    avg_2019_score_desc = avg_2019.sort_values(by = 'overall score', ascending = False)

    return avg_2019_score_desc

# use q12a to calculate the overall score of 2021 in descending order to compare to 2019 and then return which country is the one that moved rankings 
def q12a(avg_2021):
    # raise NotImplementedError
    # return ("TODO", "TODO")

    # sort rows based on overall score in descending order
    avg_2021_score_desc = avg_2021.sort_values(by = 'overall score', ascending = False)

    # print the data frame to be able to compare with 2019
    print(avg_2021_score_desc)

    # create new variable to hold the country that fell off
    country_fell_off = 'South Korea'

    return country_fell_off

"""
12b.
Comment on why the country above is at the top of the list.
(Note: This is an open-ended question.)

=== ANSWER Q12b BELOW ===

  Singapore is the country at the top of the list for both 2019 amd 2021. 
  This is because their overall score is the highest, which might have been most influenced by their high averages in academic reputation and faculty students.
  As their averages for those scores are uniquely higher.

=== END OF Q12b ANSWER ===
"""

"""
13a.
Represent all the attributes in the avg_2021 dataframe using a box and whisker plot.

Store your plot in output/part1-13a.png.

As the answer to this part, return the name of the plot you saved.

**Hint:** You can do this using subplots (and also otherwise)
"""

import matplotlib.pyplot as plt

def q13a(avg_2021):
    # Plot the box and whisker plot
    # TODO
    # raise NotImplementedError

    # create and plot the averages onto boxplot
    plt.figure()
    plt.boxplot(avg_2021, labels = avg_2021.columns)

    # edit labels and titles
    plt.title('Averages of Attributes from Top 100 Universities in 2021 According to Region')
    

    # save the plot onto png
    plt.savefig('output/part1-13a.png')
  
    return "output/part1-13a.png"

"""
b. Do you observe any anomalies in the box and whisker
plot?

=== ANSWER Q13b BELOW ===

  There is an anomoly, which is the outlier spotted in the overall score attribute. 
  It also has the smallest spread.

=== END OF Q13b ANSWER ===
"""

"""
14a.
Pick two attributes in the avg_2021 dataframe
and represent them using a scatter plot.

Store your plot in output/part1-14a.png.

As the answer to this part, return the name of the plot you saved.
"""

def q14a(avg_2021):
    # Enter code here
    # TODO
    # raise NotImplementedError

    # create new scatter plot
    plt.figure()
    plt.scatter(avg_2021['faculty student'], avg_2021['overall score'], color = 'blue')

    # edit labels and titles
    plt.title('Averages of Two Attributes from Top 100 Universities in 2021 According to Region')
    plt.xlabel('Average Number of Faculty and Students')
    plt.ylabel('Average Overall Score')

    # save the plot onto png
    plt.savefig('output/part1-14a.png')

    return "output/part1-14a.png"

"""
Do you observe any general trend?

=== ANSWER Q14b BELOW ===

  Between the x, the number of faculty and students, and the y, overall score, there is an overall positive trend.
  Although there are more x values that do not have very high y values.

=== END OF Q14b ANSWER ===

===== Questions 15-20: Exploring the data further =====

We're more than halfway through!

Let's come to the Top 10 Universities and observe how they performed over the years.

15. Create a smaller dataframe which has the top ten universities from each year, and only their overall scores across the three years.

Hint:

*   There will be four columns in the dataframe you make
*   The top ten universities are same across the three years. Only their rankings differ.
*   Use the merge function. You can read more about how to use it in the documentation: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.merge.html
*   Shape of the resultant dataframe should be (10, 4)

As your answer, return the shape of the new dataframe.
"""

def q15_helper(dfs):
    # Return the new dataframe
    # TODO
    # Placeholder:

    # get top 10 universities from 2019, only keep the university and overall score
    df_2019 = dfs[0]
    top_10_2019_fetus = df_2019[df_2019['rank'] <= 10][['university', 'overall score']].copy()

    # rename the columns
    top_10_2019 = top_10_2019_fetus.rename(columns = {'overall score': 'overall score 2019'})

    # get top 10 universities from 2020, only keep the university and overall score
    df_2020 = dfs[1]
    top_10_2020_fetus = df_2020[df_2020['rank'] <= 10][['university', 'overall score']].copy()

    # rename the columns
    top_10_2020 = top_10_2020_fetus.rename(columns = {'overall score': 'overall score 2020'})

    # get top 10 unversities from 2021, only keep the university and overall score
    df_2021 = dfs[2]
    top_10_2021_fetus = df_2021[df_2021['rank'] <= 10][['university', 'overall score']].copy()

    # rename the columns
    top_10_2021 = top_10_2021_fetus.rename(columns = {'overall score': 'overall score 2021'})
    
    # merge the universities from 2019 with 2020
    top_10 = top_10_2019.merge(top_10_2020, on = 'university', how = 'inner')
    # merge the new dataframe with 2021
    top_10 = top_10.merge(top_10_2021, on = 'university', how = 'inner')

    return top_10

def q15(top_10):
    # Enter code here
    # TODO
    # raise NotImplementedError

    # print the table to have insight
    print(top_10)

    # return the shape of the dataframe
    return top_10.shape

"""
16.
You should have noticed that when you merged,
Pandas auto-assigned the column names. Let's change them.

For the columns representing scores, rename them such that they describe the data that the column holds.

You should be able to modify the column names directly in the dataframe.
As your answer, return the new column names as a list.
"""

def q16(top_10):
    # Enter code here
    # TODO
    # raise NotImplementedError

    # the columns were already renamed in the previous function

    # return the column names as a list
    return list(top_10.columns)

    

"""
17a.
Draw a suitable plot to show how the overall scores of the Top 10 universities varied over the three years. Clearly label your graph and attach a legend. Explain why you chose the particular plot.

Save your plot in output/part1-17a.png.

As the answer to this part, return the name of the plot you saved.

Note:
*   All universities must be in the same plot.
*   Your graph should be clear and legend should be placed suitably
"""

def q17a(top_10):
    # Enter code here
    # TODO
    # raise NotImplementedError

    # set university as the index
    top_10_plot = top_10.set_index('university')

    # transpose the data so that the years are on the index (x-axis) instead
    top_10_t = top_10_plot.T

    # take the year from the column names to use as x-axis labels
    top_10_t.index = ['2019', '2020', '2021']

    # create the line plot
    ax = top_10_t.plot(
        kind = 'line',
        figsize = (12, 7), 
        # add a marker for each year
        marker = 'o'
    )

    # set title and labels
    ax.set_title('Overall Score of Top 10 Universities from 2019 to 2021')
    ax.set_xlabel('Year')
    ax.set_ylabel('Overall Score')

    # add a legend to show which university is which
    # bbox_to_anchor moves the legend outside according to (0, 0 is bottom-left, 1, 1 is top right)
    ax.legend(title = 'University', loc = 'center left', bbox_to_anchor = (1.1, 0.5))    # save the plot into png

    # tight_layout automatically adjusts figure boundaries to accomodate the elementnts
    plt.tight_layout()
      
    # save the figure into png
    plt.savefig('output/part1-17a.png')
    
    return "output/part1-17a.png"

"""
17b.
What do you observe from the plot above? Which university has remained consistent in their scores? Which have increased/decreased over the years?

=== ANSWER Q17a BELOW ===

  I observed from the plot that all of the universities remained close within their rankings. 
  The university that remained constant in their scores is Massachsuetts Institute of Technology (MIT).
  MIT remaine number 1 conistently throughout the three years.

=== END OF Q17b ANSWER ===
"""

"""
===== Questions 18-19: Correlation matrices =====

We're almost done!

Let's look at another useful tool to get an idea about how different variables are corelated to each other. We call it a **correlation matrix**

A correlation matrix provides a correlation coefficient (a number between -1 and 1) that tells how strongly two variables are correlated. Values closer to -1 mean strong negative correlation whereas values closer to 1 mean strong positve correlation. Values closer to 0 show variables having no or little correlation.

You can learn more about correlation matrices from here: https://www.statology.org/how-to-read-a-correlation-matrix/

18.
Plot a correlation matrix to see how each variable is correlated to another. You can use the data from 2021.

Print your correlation matrix and save it in output/part1-18.png.

As the answer to this part, return the name of the plot you saved.

**Helpful link:** https://datatofish.com/correlation-matrix-pandas/
"""

def q18(dfs):
    # Enter code here
    # TODO
    # raise NotImplementedError

    # create dataframe for 2021 data
    df_2021_fetus = dfs[2]

    # select only the numerical columns
    df_2021 = df_2021_fetus[['rank', 'academic reputation', 'employer reputation', 'faculty student', 'citations per faculty', 'overall score']]

    # create correlation matrix
    corr_mtrx_2021 = df_2021.corr()

    # visualize with matplotlib
    fig, ax = plt.subplots(figsize = (10, 8))
    plt.matshow(corr_mtrx_2021)

    # set the tick marks
    ax.set_xticks(range(len(corr_mtrx_2021.columns)), corr_mtrx_2021.columns, rotation = 90)
    ax.set_yticks(range(len(corr_mtrx_2021.columns)), corr_mtrx_2021.columns)

    # annotate matrix with correlation values
    for i in range(len(corr_mtrx_2021.columns)):
        for j in range(len(corr_mtrx_2021.columns)):

            # get and round correlatino values to 2 decimal places
            corr_values = corr_mtrx_2021.iloc[i, j]

            # place text onto plot
            plt.text(j, i, f'{corr_values:.2f}',
                     va = 'center', 
                     ha = 'center', 
                     fontsize = 9)
            
    # set the title
    plt.title('Correlation Matrix of Attributes')

    # fix the layout by adding more margin to fit tick labels
    plt.subplots_adjust(left = 0.2, top = 0.8)

    # save the figure
    plt.savefig('output/part1-18.png')
    return "output/part1-18.png"

"""
19. Comment on at least one entry in the matrix you obtained in the previous
part that you found surprising or interesting.

=== ANSWER Q19 BELOW ===

  Something that I found interesting in the matrix was that all of the attributes were most correlatted with the overall score and rank attributes only.
  Otherwise, the other attributes did not have much correlation with one another.

=== END OF Q19 ANSWER ===
"""

"""
===== Questions 20-23: Data manipulation and falsification =====

This is the last section.

20. Exploring data manipulation and falsification

For fun, this part will ask you to come up with a way to alter the
rankings such that your university of choice comes out in 1st place.

The data does not contain UC Davis, so let's pick a different university.
UC Berkeley is a public university nearby and in the same university system,
so let's pick that one.

We will write two functions.
a.
First, write a function that calculates a new column
(that is you should define and insert a new column to the dataframe whose value
depends on the other columns)
and calculates
it in such a way that Berkeley will come out on top in the 2021 rankings.

Note: you can "cheat"; it's OK if your scoring function is picked in some way
that obviously makes Berkeley come on top.
As an extra challenge to make it more interesting, you can try to come up with
a scoring function that is subtle!

b.
Use your new column to sort the data by the new values and return the top 10 university names as a list.

"""

def q20a(dfs):
    # TODO
    # raise NotImplementedError
    # For your answer, return the score for Berkeley in the new column.

    # take out the 2021 data
    df_2021 = dfs[2]

    # create row for Berkely
    Berkely_cheat = pd.DataFrame({'rank': [1], 
                                  'university': ['UC Berkely'], 
                                  'region': ['USA'], 
                                  'academic reputation': [0.0], 
                                  'employer reputation': [0.0], 
                                  'faculty student': [100.0], 
                                  'citations per faculty': [100.0], 
                                  'overall score': [0.0], 
                                  'year': [2021]})

    # use .concat to add in new row
    df_2021_cheat = pd.concat([df_2021_cheat, Berkely_cheat])

    # find the last row of the dataframe since that is where the berkely row is
    Berkely_row = len(df_2021_cheat) - 1

    # get the overall score of Berkely
    Berkely_ovrl_scr = df_2021_cheat.loc[Berkely_row, 'overall score']

    return Berkely_ovrl_scr

# def q20b(dfs):
    # TODO
    # raise NotImplementedError
    # For your answer, return the top 10 university names as a list.

"""
21. Exploring data manipulation and falsification, continued

This time, let's manipulate the data by changing the source files
instead.
Create a copy of data/2021.csv and name it
data/2021_falsified.csv.
Modify the data in such a way that UC Berkeley comes out on top.

For this part, you will also need to load in the new data
as part of the function.
The function does not take an input; you should get it from the file.

Return the top 10 university names as a list from the falsified data.
"""

# def q21():
    # TODO
    # raise NotImplementedError

"""
22. Exploring data manipulation and falsification, continued

Which of the methods above do you think would be the most effective
if you were a "bad actor" trying to manipulate the rankings?

Which do you think would be the most difficult to detect?

=== ANSWER Q22 BELOW ===

=== END OF Q22 ANSWER ===
"""

"""
===== Wrapping things up =====

To wrap things up, we have collected
everything together in a pipeline for you
below.

**Don't modify this part.**
It will put everything together,
run your pipeline and save all of your answers.

This is run in the main function
and will be used in the first part of Part 2.
"""

UNFINISHED = 0

def log_answer(name, func, *args):
    try:
        answer = func(*args)
        print(f"{name} answer: {answer}")
        with open(ANSWER_FILE, 'a') as f:
            f.write(f'{name},{answer}\n')
            print(f"Answer saved to {ANSWER_FILE}")
    except NotImplementedError:
        print(f"Warning: {name} not implemented.")
        with open(ANSWER_FILE, 'a') as f:
            f.write(f'{name},Not Implemented\n')
        global UNFINISHED
        UNFINISHED += 1

def PART_1_PIPELINE():
    open(ANSWER_FILE, 'w').close()

    try:
        dfs = load_input()
    except NotImplementedError:
        print("Welcome to Part 1! Implement load_input() to get started.")
        dfs = []

    # Questions 1-6
    log_answer("q1", q1, dfs)
    log_answer("q2", q2, dfs)
    log_answer("q3a", q3, dfs)
    # 3b: commentary
    log_answer("q4", q4, dfs)
    # 4b: commentary
    log_answer("q5a", q5a, dfs)
    log_answer("q5b", q5b, dfs)
    log_answer("q5c", q5c)
    # 6a: commentary
    # 6b: commentary
    log_answer("q6c", q6c)

    # Questions 7-10
    log_answer("q7", q7, dfs)
    log_answer("q8a", q8a, dfs)
    # 8b: commentary
    log_answer("q9", q9, dfs)
    # 10: avg_2021
    avg_2021 = q10_helper(dfs)
    log_answer("q10", q10, avg_2021)

    # Questions 11-15
    log_answer("q11", q11, avg_2021)
    # 12: avg_2019
    avg_2019 = q12_helper(dfs)
    log_answer("q12", q12, avg_2019)
    log_answer("q12a", q12a, avg_2021)
    # 12b: commentary
    log_answer("q13", q13a, avg_2021)
    # 13b: commentary
    log_answer("q14a", q14a, avg_2021)
    # 14b: commentary

    # Questions 15-17
    top_10 = q15_helper(dfs)
    log_answer("q15", q15, top_10)
    log_answer("q16", q16, top_10)
    log_answer("q17", q17a, top_10)
    # 17b: commentary

    # Questions 18-20
    log_answer("q18", q18, dfs)
    # 19: commentary

    # Questions 20-22
    log_answer("q20a", q20a, dfs)
    # log_answer("q20b", q20b, dfs)
    # log_answer("q21", q21)
    # 22: commentary

    # Answer: return the number of questions that are not implemented
    if UNFINISHED > 0:
        print("Warning: there are unfinished questions.")

    return UNFINISHED

"""
That's it for Part 1!

=== END OF PART 1 ===

Main function
"""

if __name__ == '__main__':
    log_answer("PART 1", PART_1_PIPELINE)
