#!/usr/bin/env python
# coding: utf-8

# ### Note
# * Instructions have been included for each segment. You do not have to follow them exactly, but they are included to help you think through the steps.

# In[3]:


# Dependencies and Setup
import pandas as pd

# File to Load (Remember to Change These)
school_data_to_load = "Resources/schools_complete.csv"
student_data_to_load = "Resources/students_complete.csv"

# Read School and Student Data File and store into Pandas Data Frames
school_data = pd.read_csv(school_data_to_load)
student_data = pd.read_csv(student_data_to_load)

# Combine the data into a single dataset
school_data_complete = pd.merge(student_data, school_data, how="left", on=["school_name", "school_name"])
school_data_complete.head()


# ## District Summary
# 
# * Calculate the total number of schools
# 
# * Calculate the total number of students
# 
# * Calculate the total budget
# 
# * Calculate the average math score 
# 
# * Calculate the average reading score
# 
# * Calculate the overall passing rate (overall average score), i.e. (avg. math score + avg. reading score)/2
# 
# * Calculate the percentage of students with a passing math score (70 or greater)
# 
# * Calculate the percentage of students with a passing reading score (70 or greater)
# 
# * Create a dataframe to hold the above results
# 
# * Optional: give the displayed data cleaner formatting

# In[88]:


school_count= school_data_complete["school_name"].nunique()
school_count


# In[234]:


school_data_complete['budget'] = pd.to_numeric(school_data_complete['budget'])
school_data_complete['math_score'] = pd.to_numeric(school_data_complete['math_score'])
school_data_complete['reading_score'] = pd.to_numeric(school_data_complete['reading_score'])


# In[145]:


student_count = school_data_complete["student_name"].count()
student_count


# In[166]:


total_budget_df = school_data_complete.groupby("school_name")
total_budget_df = pd.DataFrame(total_budget_df.mean())
total_budget= total_budget_df.iloc[:, 5].sum()
total_budget


# In[135]:


avg_read_score= school_data_complete["reading_score"].mean()
avg_read_score


# In[31]:


avg_math_score = school_data_complete["math_score"].mean()
avg_math_score


# In[32]:


pass_rate = (avg_math_score + avg_read_score)/2
pass_rate


# In[93]:


math_pass= school_data_complete.loc[(school_data_complete["math_score"] >= 70)]
math_pass = math_pass["math_score"].count()/student_count*100
math_pass


# In[94]:


read_pass= school_data_complete.loc[(school_data_complete["reading_score"] >= 70)]
read_pass = read_pass["reading_score"].count()/student_count*100
read_pass


# In[175]:


summary_df = pd.DataFrame({"School Count" :[school_count], "Total Number of Students":[student_count],
                           "Total Budget": [total_budget],"Average Math Score":[avg_math_score], 
                           "Average Reading Score": [avg_read_score],"Overall Passing Rate":[pass_rate],
                           "% Passing Math" :[math_pass],"% Passing Reading":[read_pass]}) 
summary_df


# ## School Summary

# * Create an overview table that summarizes key metrics about each school, including:
#   * School Name
#   * School Type
#   * Total Students
#   * Total School Budget
#   * Per Student Budget
#   * Average Math Score
#   * Average Reading Score
#   * % Passing Math
#   * % Passing Reading
#   * Overall Passing Rate (Average of the above two)
#   
# * Create a dataframe to hold the above results

# ## Top Performing Schools (By Passing Rate)

# * Sort and display the top five schools in overall passing rate

# In[241]:


school_group = school_data_complete.groupby("school_name")
school_group = school_group['type']
school_df = pd.DataFrame(school_group).value.count()
school_df
school_df = school_group.mean()
school_pass_rate = school_df['reading_score'] + school_df['math_score'] 
school_pass_rate = school_pass_rate/2
school_df["Overall Pass Rate"]=school_pass_rate


# In[230]:


student_budget = school_df['budget'] / school_df['size']
school_df["Per Student Budget"] = student_budget


# In[223]:





# In[217]:


school_df = pd.DataFrame({"Overall Passing Rate"[school_pass_rate]})
school_df


# ## Bottom Performing Schools (By Passing Rate)

# * Sort and display the five worst-performing schools

# In[14]:





# ## Math Scores by Grade

# * Create a table that lists the average Reading Score for students of each grade level (9th, 10th, 11th, 12th) at each school.
# 
#   * Create a pandas series for each grade. Hint: use a conditional statement.
#   
#   * Group each series by school
#   
#   * Combine the series into a dataframe
#   
#   * Optional: give the displayed data cleaner formatting

# In[15]:





# ## Reading Score by Grade 

# * Perform the same operations as above for reading scores

# In[16]:





# ## Scores by School Spending

# * Create a table that breaks down school performances based on average Spending Ranges (Per Student). Use 4 reasonable bins to group school spending. Include in the table each of the following:
#   * Average Math Score
#   * Average Reading Score
#   * % Passing Math
#   * % Passing Reading
#   * Overall Passing Rate (Average of the above two)

# In[17]:


# Sample bins. Feel free to create your own bins.
spending_bins = [0, 585, 615, 645, 675]
group_names = ["<$585", "$585-615", "$615-645", "$645-675"]


# In[18]:





# ## Scores by School Size

# * Perform the same operations as above, based on school size.

# In[ ]:


# Sample bins. Feel free to create your own bins.
size_bins = [0, 1000, 2000, 5000]
group_names = ["Small (<1000)", "Medium (1000-2000)", "Large (2000-5000)"]


# In[19]:





# ## Scores by School Type

# * Perform the same operations as above, based on school type.

# In[20]:





# In[ ]:




