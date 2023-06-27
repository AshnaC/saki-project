# Project Plan

## Summary

<!-- Describe your data science project in max. 5 sentences. -->


The project explores various environmental indicators from the German state of North Rhine-Westphalia.<br />
We have Environmental indicator data for the region from 1981 to 2021. <br />
We also have the average yearly temperature from the same region which is considered here as an indicator of Climate change.<br />
In this project, we aim to explore the relationship between different environmental indicators and average yearly temperature and with each other.<br />
The project also tries to assess the trends and patterns in different environmental indicators over time by analyzing time series data. <br />
The Average temperature data is available from 1880 to 2022, which would enable us to some temperature forcasting with the data.<br />

## Rationale

<!-- Outline the impact of the analysis, e.g. which pains it solves. -->

By examining the various Environmental Indicators together, we can gain a comprehensive understanding of how environmental changes and temperature fluctuations interact and influence each other.<br />
By analyzing the historical data, we can identify whether environmental indicators have been improving, deteriorating, or remaining stable. <br />
Thus helping in formalising methods to reduce their effects 

## Datasources

### Datasource1: Environmental Indicators

- Metadata URL: https://mobilithek.info/offers/-6975598255649615930
- Data URL: https://umweltindikatoren.nrw.de/fileadmin/indikatoren/data/indinrw_EPSG25832_csv.zip
- Data Type: CSV

Information about Environmental indicators for the state of North Rhine-Westphalia at regular intervals 

### Datasource 2: Temperature over the years

- Metadata URL: https://www.dwd.de/EN/ourservices/zeitreihen/zeitreihen.html?nn=519080
- Data URL: [URL-1]
- Data Type: CSV

Temperature information of North Rhine-Westphalia from 1881

### Datasource 3: Supplementary data set with Environment Indicators

- Metadata URL: https://www.gu.se/en/quality-government/qog-data/data-downloads/eu-regional-dataset
- Data URL: https://www.qogdata.pol.gu.se/data/qog_eureg_long_nov20.csv
- Data Type: CSV

Dataset that could be used with Data Source 1

## Work Packages

<!-- List of work packages ordered sequentially, each pointing to an issue with more details. -->

1. Load the corresponding data source [#1][i1]
2. Clean the data set and perform exploratory data analysis [#2][i2]
3. Add Data Pipeline [#3][i3]
4. Define Test cases for Data Pipeline [#4][i4]
5. Perform Analysis on Temperature Data [#5][i5]
6. Perform Analysis on Environmental indicators data [#6][i6]

[i1]: https://github.com/AshnaC/saki-project/issues/1
[i2]: https://github.com/AshnaC/saki-project/issues/2
[i3]: https://github.com/AshnaC/saki-project/issues/6
[i4]: https://github.com/AshnaC/saki-project/issues/7
[i5]: https://github.com/AshnaC/saki-project/issues/4
[i6]: https://github.com/AshnaC/saki-project/issues/5
[URL-1]: https://www.dwd.de/DE/leistungen/_config/leistungsteckbriefPublication.htm?view=nasPublication&nn=519080&imageFilePath=53506697617349850946672964853111778565853965682886767456893003839179072832754824718322058142463114108434062341293166072318725182194297636726826938791268927312211409068677713515879705002009600980877290877920434757144829346504451025102558455130226038248753805928723523872990021989423773129689612038886768327997&download=true

