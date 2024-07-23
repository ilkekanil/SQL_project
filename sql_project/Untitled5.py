#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Path to the Excel file
file_path = '/Users/ilkekanil/Desktop/sql_veriler.xlsx'

# Load the Excel file
xlsx = pd.ExcelFile(file_path)

# Check if the file exists
if 'Sheet1' in xlsx.sheet_names:
    # Read data from 'Sheet1'
    df = pd.read_excel(file_path, sheet_name='Sheet1')
    
    # Define the wanted columns
    expected_columns = ['Company Name', 'Supplier ID', 'Sales Amount']
    actual_columns = df.columns.tolist()
    
    # Check if all expected columns are present
    if all(col in actual_columns for col in expected_columns):
        print("Sheet1 has the expected columns.")
        
        # Sort the data 
        df = df.sort_values(by='Company Name')
        
        # Plot the data
        plt.figure(figsize=(12, 8))
        sns.barplot(x='Company Name', y='Sales Amount', data=df)
        plt.xticks(rotation=90)  # Rotate x-axis labels to avoid overlap
        plt.title('Sales Amount by Company')
        plt.xlabel('Company Name')
        plt.ylabel('Sales Amount')
        plt.tight_layout()
        plt.show()
    else:
        print(f"Sheet1 does not have the expected columns. Found columns: {actual_columns}")
else:
    print("Sheet1 is not found in the Excel file.")


# In[8]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Path to the Excel file
file_path = '/Users/ilkekanil/Desktop/sql_veriler.xlsx'

xlsx = pd.ExcelFile(file_path)

# Check if the file exists
if 'Sheet2' in xlsx.sheet_names:
    # Reading the data
    df = pd.read_excel(file_path, sheet_name='Sheet2')
    
    # Define the columns we want
    expected_columns = ['Employee ID', 'Last Name', 'First Name', 'Count Number']
    actual_columns = df.columns.tolist()
    
    # Check if all expected columns are present
    if all(col in actual_columns for col in expected_columns):
        print("Sheet2 has the expected columns.")
        
        # Create a new column combining 'First Name' and 'Last Name'
        df['Full Name'] = df['First Name'] + ' ' + df['Last Name']
        
        # Sort the data by 'Full Name' to make it organised 
        df = df.sort_values(by='Full Name')
        
        # Plot the data
        plt.figure(figsize=(12, 8))
        sns.barplot(x='Full Name', y='Count Number', data=df)
        plt.xticks(rotation=90)  # Rotate x-axis labels to avoid overlap
        
        # Set rows in increments to 5
        max_count = df['Count Number'].max()
        plt.yticks(np.arange(0, max_count + 5, 5))
        
        plt.title('Count Number by Full Name')
        plt.xlabel('Full Name')
        plt.ylabel('Count Number')
        plt.tight_layout()
        plt.show()
    else:
        print(f"Sheet2 does not have the expected columns. Found columns: {actual_columns}")
else:
    print("Sheet2 is not found in the Excel file.")


# In[17]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Path to the Excel file
file_path = '/Users/ilkekanil/Desktop/sql_veriler.xlsx'

# Load the Excel file
xlsx = pd.ExcelFile(file_path)

# Check if the file exists
if 'Sheet3' in xlsx.sheet_names:
    # Read data
    df = pd.read_excel(file_path, sheet_name='Sheet3')
    
    # Define the columns we want to take
    expected_columns = ['Product Name', 'Count Number']
    actual_columns = df.columns.tolist()
    
    # Check if all wanted columns are present
    if all(col in actual_columns for col in expected_columns):
        print("Sheet3 has the expected columns.")
        
        # Sort the data by 'Product Name'
        df = df.sort_values(by='Product Name')
        
        # Plot the data
        plt.figure(figsize=(12, 8))
        sns.barplot(x='Product Name', y='Count Number', data=df)
        plt.xticks(rotation=90)  # Rotate x-axis labels to avoid overlap
        
        # Set rows in increments to 5
        max_count = df['Count Number'].max()
        plt.yticks(np.arange(0, max_count + 5000, 5000))
        
        plt.title('Count Number by Product Name')
        plt.xlabel('Product Name')
        plt.ylabel('Count Number')
        plt.tight_layout()
        plt.show()
    else:
        print(f"Sheet3 does not have the expected columns. Found columns: {actual_columns}")
else:
    print("Sheet3 is not found in the Excel file.")


# In[20]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Path to the Excel file
file_path = '/Users/ilkekanil/Desktop/sql_veriler.xlsx'

# Load the Excel file
xlsx = pd.ExcelFile(file_path)

# Check if the  exists in the file
if 'Sheet4' in xlsx.sheet_names:
    # Read data from 'Sheet4'
    df = pd.read_excel(file_path, sheet_name='Sheet4')
    
    # Define the expected columns with corrected names
    expected_columns = ['Customer ID', 'Company Name', 'Total Orders', 'Total Spent', 'Last Order']
    actual_columns = df.columns.tolist()
    
    # Check if all expected columns are present
    if all(col in actual_columns for col in expected_columns):
        print("Sheet4 has the expected columns.")
        
        # Select wanted columns
        df = df[['Company Name', 'Total Orders', 'Total Spent', 'Last Order']]
        
        # Sort the data by 'Company Name'
        df = df.sort_values(by='Company Name')
        
        # Plot the graphs
        plt.figure(figsize=(14, 7))

        # Create a bar plot for 'Total Orders'
        plt.subplot(1, 2, 1)
        sns.barplot(x='Company Name', y='Total Orders', data=df)
        plt.xticks(rotation=90)
        plt.title('Total Orders by Company Name')
        plt.xlabel('Company Name')
        plt.ylabel('Total Orders')
        
        # Create a bar plot for 'Total Spent'
        plt.subplot(1, 2, 2)
        sns.barplot(x='Company Name', y='Total Spent', data=df)
        plt.xticks(rotation=90)
        plt.title('Total Spent by Company Name')
        plt.xlabel('Company Name')
        plt.ylabel('Total Spent')
        
        plt.tight_layout()
        plt.show()
    else:
        print(f"Sheet4 does not have the expected columns. Found columns: {actual_columns}")
else:
    print("Sheet4 is not found in the Excel file.")


# In[26]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Path to the Excel file
file_path = '/Users/ilkekanil/Desktop/sql_veriler.xlsx'

# Load the Excel file
xlsx = pd.ExcelFile(file_path)

# Check if the files exists in the file
if 'Sheet5' in xlsx.sheet_names:
    # Read data 
    df = pd.read_excel(file_path, sheet_name='Sheet5')
    
    # Define the wanted columns
    expected_columns = ['Year', 'Total Quantity', 'Total Revenue']
    actual_columns = df.columns.tolist()
    
    # Check if all the columns are present
    if all(col in actual_columns for col in expected_columns):
        print("Sheet5 has the expected columns.")
        
        # Select only the relevant columns
        df = df[['Year', 'Total Quantity', 'Total Revenue']]
        
        # Sort the data
        df = df.sort_values(by='Year')
        
        # Plot the graphs
        plt.figure(figsize=(14, 7))
        
        # Create a line plot for 'Total Quantity'
        plt.subplot(1, 2, 1)
        sns.lineplot(x='Year', y='Total Quantity', data=df, marker='o')
        plt.title('Total Quantity by Year')
        plt.xlabel('Year')
        plt.ylabel('Total Quantity')
        plt.xticks(ticks=np.arange(df['Year'].min(), df['Year'].max() + 1, 1), rotation=45)
        
        # Create a line plot for 'Total Revenue'
        plt.subplot(1, 2, 2)
        sns.lineplot(x='Year', y='Total Revenue', data=df, marker='o')
        plt.title('Total Revenue by Year')
        plt.xlabel('Year')
        plt.ylabel('Total Revenue')
        plt.xticks(ticks=np.arange(df['Year'].min(), df['Year'].max() + 1, 1), rotation=45)
        
        plt.tight_layout()
        plt.show()
    else:
        print(f"Sheet5 does not have the expected columns. Found columns: {actual_columns}")
else:
    print("Sheet5 is not found in the Excel file.")


# In[27]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Path to the Excel file
file_path = '/Users/ilkekanil/Desktop/sql_veriler.xlsx'

# Load the Excel file
xlsx = pd.ExcelFile(file_path)

# Check if the exists
if 'Sheet6' in xlsx.sheet_names:
    # Read data 
    df = pd.read_excel(file_path, sheet_name='Sheet6')
    
    # Define the wanted columns
    expected_columns = ['Employee ID', 'First Name', 'Last Name', 'Total Orders', 'Total Quantity', 'Total Revenue']
    actual_columns = df.columns.tolist()
    
    # Check if all the columns are present
    if all(col in actual_columns for col in expected_columns):
        print("Sheet6 has the expected columns.")
        
        # Combining 'First Name' and 'Last Name'
        df['Full Name'] = df['First Name'] + ' ' + df['Last Name']
        
        # Select the columns
        df = df[['Full Name', 'Total Orders', 'Total Quantity', 'Total Revenue']]
        
        # Sort the data by 'Full Name' for organisation
        df = df.sort_values(by='Full Name')
        
        # Plot Total Orders, Total Quantity, and Total Revenue
        plt.figure(figsize=(18, 12))
        
        # Create a plot for 'Total Orders'
        plt.subplot(3, 1, 1)
        sns.barplot(x='Full Name', y='Total Orders', data=df)
        plt.xticks(rotation=90)
        plt.title('Total Orders by Employee')
        plt.xlabel('Employee')
        plt.ylabel('Total Orders')
        
        # Create a plot for 'Total Quantity'
        plt.subplot(3, 1, 2)
        sns.barplot(x='Full Name', y='Total Quantity', data=df)
        plt.xticks(rotation=90)
        plt.title('Total Quantity by Employee')
        plt.xlabel('Employee')
        plt.ylabel('Total Quantity')
        
        # Create a plot for 'Total Revenue'
        plt.subplot(3, 1, 3)
        sns.barplot(x='Full Name', y='Total Revenue', data=df)
        plt.xticks(rotation=90)
        plt.title('Total Revenue by Employee')
        plt.xlabel('Employee')
        plt.ylabel('Total Revenue')
        
        plt.tight_layout()
        plt.show()
    else:
        print(f"Sheet6 does not have the expected columns. Found columns: {actual_columns}")
else:
    print("Sheet6 is not found in the Excel file.")


# In[ ]:




