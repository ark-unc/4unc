
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
sales_by_month = df.filter(items=['Sales']).groupby(pd.Grouper(freq='M')).sum()

st.dataframe(sales_by_month)
#st.write(sales_by_month)

# Here the grouped months are the index and automatically used for the x axis
st.line_chart(sales_by_month, y="Sales")

# Additions for Assignment
#sales_by_month = df.filter(items=['Sub_Category','Sales']).groupby(pd.Grouper(freq='M')).sum()
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
#st.write("Selected Sub-Cat :", sales_by_sub_cat)


#sales_by_month = df.filter(items=['Sub_Category','Sales']).groupby(pd.Grouper(freq='M')).sum()
#st.line_chart(sales_by_month, y="Sales", color='Sub_Category')

test_df["Order_Date"] = pd.to_datetime(test_df["Order_Date"])
test_df.set_index('Order_Date', inplace=True)

sales_by_sub_cat = test_df.groupby([pd.Grouper(freq='Y'),'Sub_Category'])["Sales"].sum()
sales_by_sub_cat1 = test_df.groupby(['Sub_Category',pd.Grouper(freq='Y')])["Sales"].sum()
st.write("SALES BY SUB CAT")
st.write(sales_by_sub_cat1)
#pull the rows from 'sales_by_sub_cat for 'sub-cat_slectec'
s2 = sales_by_sub_cat1.loc[sub_cat_selected]
st.write("Selected Sub-Cat Data for graph:")
ss1 = s2.to_frame()
st.dataframe(ss1)
#s2.set_index('Order_Date', inplace=True)
#s2 = sales_by_sub_cat.filter(sub_cat_selected)
#s2.reset_index()
#s2.set_index('Sub_Category', inplace=True)
st.write("111")
#st.write(type(ss1))
st.write(ss1[1])
#st.write(ss1.get_loc())
st.write(ss1.describe())
df_info = s2.info()
st.write(df_info)
st.write("121212")
st.write(ss1.shape)
st.write("23233")
st.write(ss1.shape)
st.write("2222")
st.write(ss1.get('Sub_Category'))
st.line_chart(ss1,y='Sales')#, Color ='Sub_Category')

#st.write("Selected Sub-Cat Data for graph:", s2)

#st.line_chart(s2)

st.write("### (4 & 5) show three metrics - total sales, total profit, and overall profit & Delta")

test_metrics = test_df.groupby(['Sub_Category'])[["Sales","Profit"]].sum()
#st.write("METRICS")
#st.write(test_metrics)
#st.write("testing111")
s3 = test_metrics.loc[sub_cat_selected]
#st.write("testing22222")
overall_profit = test_metrics['Profit'].sum()
overall_sales = test_metrics['Sales'].sum()
overall_margin = (overall_profit/overall_sales)*100
#st.write(overall_profit)
#st.write(overall_margin)
#st.write(16.867-overall_margin)

#st.write("length of " + str(len(s3)));
#st.write("testing333333")
for ind in range(len(s3)):
    st.metric("Sub-Category " , sub_cat_selected[ind])
    st.metric("Sales ", s3.loc[sub_cat_selected[ind]][0])
    st.metric("Profit ", s3.loc[sub_cat_selected[ind]][1])
    margin = ((s3.loc[sub_cat_selected[ind]][1])/(s3.loc[sub_cat_selected[ind]][0]))*100
    l_margin = margin - overall_margin
    st.metric("Overall profit Margin %",margin,delta=l_margin)
    #st.write("local margin")
    #st.write(l_margin)
    
    #st.metric("Overall profit Margin %", ((s3.loc[sub_cat_selected[ind]][1])/(s3.loc[sub_cat_selected[ind]][0]))*100,delta=(((s3.loc[sub_cat_selected[ind]][1])/(s3.loc[sub_cat_selected[ind]][0]))-overall_margin))

    #print("Sub-Cat" + t12[ind])
    #print("Sales" + str(t2.loc[t12[ind]][0]))
    #print("Profit" + str(t2.loc[t12[ind]][1]))
    #print("Overall profit Margin %"+ str((t2.loc[t12[ind]][1]/t2.loc[t12[ind]][0])*100))

    
#st.write("testing555555");
#st.write("### (5) use the delta option in the overall profit margin metric to show the difference between the overall average profit margin (all products across all categories)")
# first find the overall avrage profilt. That is sum of profit column
#st.write("Metrics Sub-Cat Data :", s3)
#s3.apply(st.metric(s3))
# for sub_cat_selected extract test_metrics (Sales & Profit) and calculate % profile/sales
# output of above will be input for st.metric 

#st.line_chart(sales_by_sub_cat, y="Sales")
#sales_by_sub_cat = test_df.groupby(['Sub_Category']) ['Sales'].sum()

#sales_by_month_cat_1 = sales_by_month_cat.groupby('Sub_Category')

#sales_by_month = df.filter(items=['Sales']).groupby(pd.Grouper(freq='M')).sum()

#st.line_chart(sales_by_sub_cat, y='Sales')
#st.line_chart(s2, y='Sales')

#st.line_chart(df.groupby("Sub_Category", as_index=False).sum(), x="Sub_Category", y="Sales", color="#04f")
              
st.write("## Done With additions")
#st.write("### (1) add a drop down for Category (https://docs.streamlit.io/library/api-reference/widgets/st.selectbox)")
#st.write("### (2) add a multi-select for Sub_Category *in the selected Category (1)* (https://docs.streamlit.io/library/api-reference/widgets/st.multiselect)")
#st.write("### (3) show a line chart of sales for the selected items in (2)")
#st.write("### (4) show three metrics (https://docs.streamlit.io/library/api-reference/data/st.metric) for the selected items in (2): total sales, total profit, and overall profit margin (%)")
#st.write("### (5) use the delta option in the overall profit margin metric to show the difference between the overall average profit margin (all products across all categories)")

