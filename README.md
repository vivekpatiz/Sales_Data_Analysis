# Sales_Data_Analysis

## Problem Statement
An analysis of the historical data of a company which sells products and ships them to its customers' destinations was conducted in order to determine the future cost effective shipping methods and approaches.

## Dataset Used
A historical dataset with 1000,000 rows and 13 columns spanning 8 years. Data is stored in a single table.

## We start by cleaning our data. Tasks during this section include:

1. Drop NaN values from DataFrame

2. Removing rows based on a condition

3. Change the type of columns (to_numeric, to_datetime, astype)


## Questions followed - Once we have cleaned up our data a bit, we move the data exploration section. In this section we explore 5 high level business questions related to our data:
1. What was the best month for sales? How much was earned that month?
2. What city sold the most product?
3. What time should we display advertisemens to maximize the likelihood of customer’s buying product?
4. What products are most often sold together?
5. What product sold the most? Why do you think it sold the most?

## Analyses derived from the dataset
##1. What was the best month for sales? How much was earned that month?
![image](https://user-images.githubusercontent.com/41379292/201622032-8426c5ca-7a0b-415d-a071-b02fa34f1ae7.png)

##2. What city sold the most product?
![image](https://user-images.githubusercontent.com/41379292/201622210-ec4183d4-b5b9-4ac5-9ddc-5b90ba003d4b.png)

##3. What time should we display advertisemens to maximize the likelihood of customer’s buying product?
![image](https://user-images.githubusercontent.com/41379292/201622281-926fcd92-b92b-42fc-ab77-6fdea29ab085.png)

##4. What products are most often sold together?
![image](https://user-images.githubusercontent.com/41379292/201622460-1e4cc7b8-a88d-4298-aebb-3a9b7fba9cd3.png)

##5. What product sold the most? Why do you think it sold the most?
![image](https://user-images.githubusercontent.com/41379292/201622514-272a6db3-da9e-4a16-8d6a-3a03cb7f6d6d.png)


### Active filters needed to interact with the data and the dashboard 
Country, years, and quarters

<img width="130" height="155" alt="countryslicer" src="https://user-images.githubusercontent.com/71536311/191996934-3fefa752-2aca-4285-b51b-d2f5bda2671e.png">  <img width="130" height="120" alt="yearslicer" src="https://user-images.githubusercontent.com/71536311/191996968-115a04a3-7280-4e1e-b447-ec7f1c014492.png">  <img width="120" height="85" alt="quarterslicer" src="https://user-images.githubusercontent.com/71536311/191996992-fc2f9fef-1b51-4676-9aab-59e10625f756.png">

## Tools Used
![Microsoft Excel](https://img.shields.io/badge/Microsoft_Excel-217346?style=for-the-badge&logo=microsoft-excel&logoColor=white)

- Utilized **Power Query** to extract and transform the data, then transferred the data to **Power Pivot** for further analysis.
- **Power Pivot** is used to store the data for further exploration in the future, if the number of rows increases into the millions.
- Implemented **OFFSET** and **COUNTA** functions to prepare reports that interpret transaction, order, COGS, revenue, and net profit on a monthly and quarterly basis, by sales channel, by sales regions and by item types sold over time.

## Overview
![image](https://user-images.githubusercontent.com/71536311/195052888-c7c70f32-81e7-4a49-b7c7-19db0c9126bc.png)

![p1](https://user-images.githubusercontent.com/71536311/192129988-152f8048-77e3-43bb-90a6-ab8955581e09.gif)
![p2](https://user-images.githubusercontent.com/71536311/192128415-eff3e519-397d-4596-a6ef-84ba9f335f8d.gif)
![p3](https://user-images.githubusercontent.com/71536311/192136774-3b7d46d8-e060-48b2-ae02-44e9fba7ad9d.gif)
![p4](https://user-images.githubusercontent.com/71536311/192136941-32cc6e78-38bb-4ec5-abd4-1d26d47ade11.gif)
![p5](https://user-images.githubusercontent.com/71536311/192138750-73af196a-d635-4071-a408-fd356a3c0467.gif)   
