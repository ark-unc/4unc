import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import math

st.title("Data App Assignment, on Oct 7th")

st.write("### Input Data and Examples")
df = pd.read_csv("Superstore_Sales_utf8.csv", parse_dates=True)
test_df = pd.read_csv("Superstore_Sales_utf8.csv", parse_dates=True)
st.dataframe(df)
#st.write(df.head(2))
# This bar chart will not have solid bars--but lines--because the detail data is being graphed independently
st.bar_chart(df, x="Category", y="Sales")

# Now let's do the same graph where we do the aggregation first in Pandas... (this results in a chart with solid bars)
st.dataframe(df.groupby("Category").sum())
# Using as_index=False here preserves the Category as a column.  If we exclude that, Category would become the datafram index and we would need to use x=None to tell bar_chart to use the index
st.bar_chart(df.groupby("Category", as_index=False).sum(), x="Category", y="Sales", color="#04f")

# Aggregating by time
# Here we ensure Order_Date is in datetime format, then set is as an index to our dataframe
df["Order_Date"] = pd.to_datetime(df["Order_Date"])
df.set_index('Order_Date', inplace=True)
# Here the Grouper is using our newly set index to group by Month ('M')
sales_by_month = df.filter(items=['Sub_Category','Sales']).groupby(pd.Grouper(freq='M')).sum()


#sales_by_month = df.filter(items=['Sub_Category','Sales']).groupby(pd.Grouper(freq='M')).sum()
#st.line_chart(sales_by_month, y="Sales", color='Sub_Category')

test_df["Order_Date"] = pd.to_datetime(test_df["Order_Date"])
test_df.set_index('Order_Date', inplace=True)

sales_by_sub_cat = test_df.groupby([test_df.Order_Date.dt.year,'Sub_Category'])["Sales"].sum()
#sales_by_sub_cat = test_df.groupby(['Sub_Category']) ['Sales'].sum()

st.dataframe(sales_by_month)
st.write(sales_by_sub_cat)

# Here the grouped months are the index and automatically used for the x axis
st.line_chart(sales_by_month, y="Sales")

# Additions for Assignment
st.write("## Additions")
label1 = 'Category'
label2 = 'Sub-Category'
st.write("### (1) add a drop down for Category")
selected_option = st.selectbox(label1, df.groupby("Category"))
st.write("Selected Option is :", selected_option)

st.write("### (2) add a multi-select for Sub_Category *in the selected Category (1)* ")
sub_cat_options = (df['Sub_Category'].loc[df['Category'] == selected_option].unique())
sub_cat_selected = st.multiselect(label2, sub_cat_options)

st.write("Selected Option is :", sub_cat_selected)

st.write("### (3) show a line chart of sales for the selected items in (2)")

#print(str_sls_1)
#str_sls_2 = str_sls_1.reset_index();

#sales_by_sub_cat = df.groupby([df.Order_Date.dt.year, 'Sub_Category']) ['Sales'].sum()
st.write("Selected Sub-Cat :", sales_by_sub_cat)

s2 = sales_by_sub_cat.filter(sub_cat_selected)
st.write("Selected Sub-Cat Data for graph:", s2)
#sales_by_month_cat_1 = sales_by_month_cat.groupby('Sub_Category')

#sales_by_month = df.filter(items=['Sales']).groupby(pd.Grouper(freq='M')).sum()

st.line_chart(sales_by_sub_cat, y='Sales')
st.line_chart(s2, y='Sales')

#st.line_chart(df.groupby("Sub_Category", as_index=False).sum(), x="Sub_Category", y="Sales", color="#04f")
              
st.write("## Your additions")
st.write("### (1) add a drop down for Category (https://docs.streamlit.io/library/api-reference/widgets/st.selectbox)")
st.write("### (2) add a multi-select for Sub_Category *in the selected Category (1)* (https://docs.streamlit.io/library/api-reference/widgets/st.multiselect)")
st.write("### (3) show a line chart of sales for the selected items in (2)")
st.write("### (4) show three metrics (https://docs.streamlit.io/library/api-reference/data/st.metric) for the selected items in (2): total sales, total profit, and overall profit margin (%)")
st.write("### (5) use the delta option in the overall profit margin metric to show the difference between the overall average profit margin (all products across all categories)")
