# original code retrieved from (on 02.11.2024): https://docs.greatexpectations.io/docs/core/introduction/try_gx/?procedure=sample_code

# Import required modules from GX library.
import great_expectations as gx
import pandas as pd
import requests as r

def get_data(): 

    print("Get data from sedlabanki.is")
    #TODO: change default time frame to 20 years ago to today 
    # get user input: from date; to date; file format
    from_date = input("choose date from (yyyy-mm-dd): ")
    to_date = input("choose date to (yyyy-mm-dd): ")
    if from_date == "" or to_date == "": # provide default from and to dates
        from_date = "2004-09-17"
        to_date = "2024-09-17"
        print(f"no from or to dates provided - default dates: {from_date} to {to_date}")
    fileformat = input("choose fileformat (csv/xml): ")
    if fileformat == "": # provide default format
        fileformat = "csv"
        print(f"no file format chosen - default format: {fileformat}")
        
    # assemble url
    url_template = f"http://www.sedlabanki.is/xmltimeseries/Default.aspx?DagsFra={from_date}&DagsTil={to_date}T23:59:59&TimeSeriesID=4055&Type={fileformat}"

    #TODO: check if file with requested data already exits - if it exits still return filename
    filename = f"sedlabankinn_data_from_{from_date}_to_{to_date}.{fileformat}"

    #TODO: currently only possible to download csv properly, xml is encoded incorrectly; fix this!
    # download and decode data, write to file in data-folder
    response = r.get(url_template)
    data = response.content.decode("utf-8") #("utf-8")
    file = open("../data/" + filename, "w", encoding="utf-8")
    file.write(data)
    file.close()
    return filename

filename = "sedlabankinn_data_from_2004-09-17_to_2024-09-17.csv"# get_data()

# Create Data Context.
context = gx.get_context()

# Import data into Pandas DataFrame.
# TODO: use xml version to automatically get column names from xml elements
df = pd.read_csv("../data/" + filename, sep=";", header=None) 
column_names = ["Group ID", "Name", "TimeSeries ID", "FameName", "Name", "Description", "Date", "Value"] 
df.columns = column_names # indicate there is no header (i.e. no column names) with header=None and set column names manually retrieved from xml elements 

# Connect to data.
# Create Data Source, Data Asset, Batch Definition, and Batch.
data_source = context.data_sources.add_pandas("pandas")
data_asset = data_source.add_dataframe_asset(name="pd dataframe asset")

batch_definition = data_asset.add_batch_definition_whole_dataframe("batch definition")
batch = batch_definition.get_batch(batch_parameters={"dataframe": df})

# Create Expectation.
valsbetween_expectation = gx.expectations.ExpectColumnValuesToBeBetween(column="Value", min_value=0, max_value=999)
column_names_expectation = gx.expectations.ExpectTableColumnsToMatchOrderedList(column_list=column_names)
no_null_cells_expectation = gx.expectations.ExpectColumnValuesToNotBeNull(column="Value")


# Validate Batch using Expectation.
valsbetween_validation_result = batch.validate(valsbetween_expectation)
column_names_validation_result = batch.validate(column_names_expectation)
no_null_cells_validation_result = batch.validate(no_null_cells_expectation)

# print results
print("Info about data (filename):", filename)
print("are the values in the Values column between the specified range (i.e. 0-999)?\n", valsbetween_validation_result) 
print("are the column names in the dataframe the same as the ones in the column_names list:\n", column_names_validation_result)
print("is it the case that there are no null values in the Values column?\n", no_null_cells_validation_result)