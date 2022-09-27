#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#!/usr/bin/env python
# coding: utf-8


# Script for downloading SharePoint online Excel files
import sharepy
import datetime as dt
from datetime import date, timedelta
import pyodbc as pdb
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile


# conect to SharePoint site
s = sharepy.connect("https://mycomplog.sharepoint.com",username="clipservice@ftcli.com", password="updateMySharepoint")

# download the file to a local folder
f = "https://mycomplog.sharepoint.com/sites/CLIQualityTeam/Shared Documents/General/Layered Audit Tracking/Layered Audit Effectiveness Tracking-CHQ.xlsx"
s.getfile(f)


# read back the excel file into a pandas dataframe
LPA = pd.read_excel('Layered Audit Effectiveness Tracking-CHQ.xlsx', sheet_name='Data Entry Sheet')#, skiprows =96)


col_Names_LP=["WeekEnding",
           "Number of Level 1 Audits Assigned", 
           "Number of Level 1 Audits Completed", 
           "Number of Level 2 Audits Assigned",
            "Number of Level 2 Audits Completed"]
col_names_NC = ["WeekEnding", "Calibration","Docs and Records","Formal Customer Concern"
                ,"Materials","Operator Instruction","Process Control",
                "Safety","Training"]

'''
#Albion
Albion = LPA.iloc[32:60, 1:118]
Albion = Albion.T
Albion_LPA= Albion.iloc[0:114, 0:5]
Albion_LPA.columns = col_Names_LP
Albion_L1NC = Albion.iloc[0:114, [0, 10,11,12,13,14,15,16,17]]
Albion_L1NC.columns =  col_names_NC
Albion_L2NC = Albion.iloc[0:114, [0, 20,21,22,23,24,25,26,27]]
Albion_L2NC.columns = col_names_NC
Albion_LPA["Plant"]  = 'Albion'
Albion_L1NC["Plant"] = 'Albion'
Albion_L2NC["Plant"] = 'Albion'
'''
#Avon
Avon = LPA.iloc[63:91, 1:118]
Avon = Avon.T
Avon_LPA= Avon.iloc[0:114, 0:5]
Avon_LPA.columns = col_Names_LP
Avon_L1NC = Avon.iloc[0:114, [0, 10,11,12,13,14,15,16,17]]
Avon_L1NC.columns =  col_names_NC
Avon_L2NC = Avon.iloc[0:114, [0, 20,21,22,23,24,25,26,27]]
Avon_L2NC.columns = col_names_NC
Avon_LPA["Plant"] = 'Avon'
Avon_L1NC["Plant"] = 'Avon'
Avon_L2NC["Plant"] = 'Avon'

#Claycomo
Claycomo = LPA.iloc[94:122, 1:118]
Claycomo = Claycomo.T
Claycomo_LPA= Claycomo.iloc[0:114, 0:5]
Claycomo_LPA.columns = col_Names_LP
Claycomo_L1NC = Claycomo.iloc[0:114, [0, 10,11,12,13,14,15,16,17]]
Claycomo_L1NC.columns =  col_names_NC
Claycomo_L2NC = Claycomo.iloc[0:114, [0, 20,21,22,23,24,25,26,27]]
Claycomo_L2NC.columns = col_names_NC
Claycomo_LPA["Plant"] = 'Claycomo'
Claycomo_L1NC["Plant"] = 'Claycomo'
Claycomo_L2NC["Plant"] = 'Claycomo'

#Columbus
Columbus = LPA.iloc[125:153, 0:118]
Columbus = Columbus.T
Columbus_LPA= Columbus.iloc[1:114, 0:5]
Columbus_LPA.columns = col_Names_LP
Columbus_L1NC = Columbus.iloc[1:114, [0, 10,11,12,13,14,15,16,17]]
Columbus_L1NC.columns =  col_names_NC
Columbus_L2NC = Columbus.iloc[1:114, [0, 20,21,22,23,24,25,26,27]]
Columbus_L2NC.columns = col_names_NC
Columbus_LPA["Plant"] = 'Columbus'
Columbus_L1NC["Plant"] = 'Columbus'
Columbus_L2NC["Plant"] = 'Columbus'

#Crandall
Crandall = LPA.iloc[156:186, 0:118]
Crandall = Crandall.T
Crandall_LPA= Crandall.iloc[1:114, 0:5]
Crandall_LPA.columns = col_Names_LP
Crandall_L1NC = Crandall.iloc[1:114, [0, 10,11,12,13,14,15,16,17]]
Crandall_L1NC.columns =  col_names_NC
Crandall_L2NC = Crandall.iloc[1:114, [0, 20,21,22,23,24,25,26,27]]
Crandall_L2NC.columns = col_names_NC
Crandall_LPA["Plant"] = 'Crandall'
Crandall_L1NC["Plant"] = 'Crandall'
Crandall_L2NC["Plant"] = 'Crandall'

#Dearbon
Dearborn = LPA.iloc[187:216, 0:118]
Dearborn = Dearborn.T
Dearborn_LPA= Dearborn.iloc[1:114, 0:5]
Dearborn_LPA.columns = col_Names_LP
Dearborn_L1NC = Dearborn.iloc[1:114, [0, 10,11,12,13,14,15,16,17]]
Dearborn_L1NC.columns =  col_names_NC
Dearborn_L2NC = Dearborn.iloc[1:114, [0, 20,21,22,23,24,25,26,27]]
Dearborn_L2NC.columns = col_names_NC
Dearborn_LPA["Plant"] = 'Dearborn'
Dearborn_L1NC["Plant"] = 'Dearborn'
Dearborn_L2NC["Plant"] = 'Dearborn'

#Denton

Denton = LPA.iloc[218:246, 0:118]
Denton = Denton.T
Denton_LPA= Denton.iloc[1:114, 0:5]
Denton_LPA.columns = col_Names_LP
Denton_L1NC = Denton.iloc[1:114, [0, 10,11,12,13,14,15,16,17]]
Denton_L1NC.columns =  col_names_NC
Denton_L2NC = Denton.iloc[1:114, [0, 20,21,22,23,24,25,26,27]]
Denton_L2NC.columns = col_names_NC
Denton_LPA["Plant"] = 'Denton'
Denton_L1NC["Plant"] = 'Denton'
Denton_L2NC["Plant"] = 'Denton'
'''
#Eldridge
Eldridge = LPA.iloc[249:277, 0:118]
Eldridge = Eldridge.T
Eldridge_LPA= Eldridge.iloc[1:114, 0:5]
Eldridge_LPA.columns = col_Names_LP
Eldridge_L1NC = Eldridge.iloc[1:114, [0, 10,11,12,13,14,15,16,17]]
Eldridge_L1NC.columns =  col_names_NC
Eldridge_L2NC = Eldridge.iloc[1:114, [0, 20,21,22,23,24,25,26,27]]
Eldridge_L2NC.columns = col_names_NC
Eldridge_LPA["Plant"] = 'Eldridge'
Eldridge_L1NC["Plant"] = 'Eldridge'
Eldridge_L2NC["Plant"] = 'Eldridge'
'''

#Fairfax
Fairfax = LPA.iloc[280:320, 0:118]
Fairfax = Fairfax.T
Fairfax_LPA= Fairfax.iloc[1:114, 0:5]
Fairfax_LPA.columns = col_Names_LP
Fairfax_L1NC = Fairfax.iloc[1:114, [0, 10,11,12,13,14,15,16,17]]
Fairfax_L1NC.columns =  col_names_NC
Fairfax_L2NC = Fairfax.iloc[1:114, [0, 20,21,22,23,24,25,26,27]]
Fairfax_L2NC.columns = col_names_NC
Fairfax_LPA["Plant"] = 'Fairfax'
Fairfax_L1NC["Plant"] = 'Fairfax'
Fairfax_L2NC["Plant"] = 'Fairfax'

#Florence
Florence = LPA.iloc[311:340, 0:118]
Florence = Florence.T
Florence_LPA= Florence.iloc[1:114, 0:5]
Florence_LPA.columns = col_Names_LP
Florence_L1NC = Florence.iloc[1:114, [0, 10,11,12,13,14,15,16,17]]
Florence_L1NC.columns =  col_names_NC
Florence_L2NC = Florence.iloc[1:114, [0, 20,21,22,23,24,25,26,27]]
Florence_L2NC.columns = col_names_NC
Florence_LPA["Plant"] = 'Florence'
Florence_L1NC["Plant"] = 'Florence'
Florence_L2NC["Plant"] = 'Florence'

#Kent
Kent = LPA.iloc[342:370, 0:118]
Kent = Kent.T
Kent_LPA= Kent.iloc[1:114, 0:5]
Kent_LPA.columns = col_Names_LP
Kent_L1NC = Kent.iloc[1:114, [0, 10,11,12,13,14,15,16,17]]
Kent_L1NC.columns =  col_names_NC
Kent_L2NC = Kent.iloc[1:114, [0, 20,21,22,23,24,25,26,27]]
Kent_L2NC.columns = col_names_NC
Kent_LPA["Plant"] = 'Kent'
Kent_L1NC["Plant"] = 'Kent'
Kent_L2NC["Plant"] = 'Kent'

# SpringHill
SPH = LPA.iloc[373:410, 0:118]
SPH = SPH.T
SPH_LPA= SPH.iloc[1:114, 0:5]
SPH_LPA.columns = col_Names_LP
SPH_L1NC = SPH.iloc[1:114, [0, 10,11,12,13,14,15,16,17]]
SPH_L1NC.columns =  col_names_NC
SPH_L2NC = SPH.iloc[1:114, [0, 20,21,22,23,24,25,26,27]]
SPH_L2NC.columns = col_names_NC
SPH_LPA["Plant"] = 'Springhill'
SPH_L1NC["Plant"] = 'Springhill'
SPH_L2NC["Plant"] = 'Springhill'

#Wentzville
Wentzville = LPA.iloc[404:432, 0:118]
Wentzville = Wentzville.T
Wentzville_LPA= Wentzville.iloc[1:114, 0:5]
Wentzville_LPA.columns = col_Names_LP
Wentzville_L1NC = Wentzville.iloc[1:114, [0, 10,11,12,13,14,15,16,17]]
Wentzville_L1NC.columns =  col_names_NC
Wentzville_L2NC = Wentzville.iloc[1:114, [0, 20,21,22,23,24,25,26,27]]
Wentzville_L2NC.columns = col_names_NC
Wentzville_LPA["Plant"] = 'Wentzville'
Wentzville_L1NC["Plant"] = 'Wentzville'
Wentzville_L2NC["Plant"] = 'Wentzville'

#Watertown
Watertown = LPA.iloc[435:463, 0:118]
Watertown = Watertown.T
Watertown_LPA= Watertown.iloc[1:114, 0:5]
Watertown_LPA.columns = col_Names_LP
Watertown_L1NC = Watertown.iloc[1:114, [0, 10,11,12,13,14,15,16,17]]
Watertown_L1NC.columns =  col_names_NC
Watertown_L2NC = Watertown.iloc[1:114, [0, 20,21,22,23,24,25,26,27]]
Watertown_L2NC.columns = col_names_NC
Watertown_LPA["Plant"] = 'Watertown'
Watertown_L1NC["Plant"] = 'Watertown'
Watertown_L2NC["Plant"] = 'Watertown'


# Make a data frame for Layerd Process Audit data


LPA_Union = pd.concat([Avon_LPA,Claycomo_LPA,Columbus_LPA,Dearborn_LPA,Fairfax_LPA,Florence_LPA,SPH_LPA,Wentzville_LPA,Crandall_LPA,Kent_LPA, Denton_LPA, Watertown_LPA])


# Save data in a local file


dt_now = dt.datetime.now().strftime("%m%d%Y %H%M%S")
LPA_Union.to_csv('C:\\Users\\farshid.hosseini\\Documents\\CLIP_Integration\\LayerdProcessAudit\\LPA_{}.csv'.format(dt_now), index = None, header =True)


# Maske a data frame for level 1 non-conformance and add a column call Level to it


L1NC_Union = pd.concat([ 
                        Avon_L1NC,
                        Claycomo_L1NC,
                        Columbus_L1NC,
                        Dearborn_L1NC,
                        
                       Fairfax_L1NC,
                        Florence_L1NC,
                        SPH_L1NC,
                        Wentzville_L1NC,
                        Crandall_L1NC,
                        Kent_L1NC, 
                       Denton_L1NC,
                        Watertown_L1NC])

L1NC_Union["Level"] = 'Level1'


# Save data in a local file


L1NC_Union.to_csv('C:\\Users\\farshid.hosseini\\Documents\\CLIP_Integration\\LayerdProcessAudit\\L1NC_{}.csv'.format(dt_now), index = None, header =True)


# # Maske a data frame for level 2 non-conformance and add a column call Level to it


L2NC_Union = pd.concat([
                        Avon_L2NC,
                        Claycomo_L2NC,
                        Columbus_L2NC,
                        Dearborn_L2NC,
                       
                       Fairfax_L2NC,
                        Florence_L2NC,
                        SPH_L2NC,
                        Wentzville_L2NC,
                        Crandall_L2NC,
                        Kent_L2NC, 
                       Denton_L2NC,
                        Watertown_L2NC])
L2NC_Union["Level"] = 'Level2'


# Save data in a local file


L2NC_Union.to_csv('C:\\Users\\farshid.hosseini\\Documents\\CLIP_Integration\\LayerdProcessAudit\\L2NC_{}.csv'.format(dt_now), index = None, header =True)


# connect to the target database
server = 'tcp:cliq.database.windows.net'
database = 'CLIQ_Staging_DB' #'Staging_UltiPro'
username = 'cliq_admin'
password = 'gfd#2019'
driver= '{ODBC Driver 13 for SQL Server}'
cnxn = pdb.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+password)
cursor = cnxn.cursor()

# Remove old data and insert new data for Layerd Process Audit
cursor.execute("""TRUNCATE TABLE [clip].[LayaredProcessAudit_Source]""")
for index, ROW in LPA_Union.iterrows():
    cursor.execute("""INSERT INTO [clip].[LayaredProcessAudit_Source]
                        (                     
                           [Facility]
                          ,[Date]
                          ,[# of Level 1 Audits Assigned]
                          ,[# of Level 1 Audits Completed]
                          ,[# of Level 2 Audits Assigned]
                          ,[# of Level 2 Audits Completed]

                        )
                  values (?,?,?,?,?,?)"""
                            ,ROW['Plant']
                            ,ROW['WeekEnding']
                            ,ROW['Number of Level 1 Audits Assigned']
                            ,ROW['Number of Level 1 Audits Completed']
                            ,ROW['Number of Level 2 Audits Assigned']
                            ,ROW['Number of Level 2 Audits Completed']

                      ) 
    cursor.commit()


# Remove old data and insert new data for LPA non-conformance data
cursor.execute("""TRUNCATE TABLE [clip].[LPA_NC_Source]""")
for index, ROW in L1NC_Union.iterrows():
    cursor.execute("""INSERT INTO [clip].[LPA_NC_Source]
                        (                     
                           [WeekEnding]
                          ,[Calibration]
                          ,[Docs and Records]
                          ,[Formal Customer Concern]
                          ,[Materials]
                          ,[Operator Instruction]
                          ,[Process Control]
                          ,[Safety]
                          ,[Training]
                          ,[Plant]
                          ,[Level]

                        )
                  values (?,?,?,?,?,?,?,?,?,?,?)"""
                            ,ROW['WeekEnding']
                            ,ROW['Calibration']
                            ,ROW['Docs and Records']
                            ,ROW['Formal Customer Concern']
                            ,ROW['Materials']
                            ,ROW['Operator Instruction']
                            ,ROW['Process Control']
                            ,ROW['Safety']
                            ,ROW['Training']
                            ,ROW['Plant']
                            ,ROW['Level']

                      ) 
    cursor.commit()
for index, ROW in L2NC_Union.iterrows():
    cursor.execute("""INSERT INTO [clip].[LPA_NC_Source]
                        (                     
                           [WeekEnding]
                          ,[Calibration]
                          ,[Docs and Records]
                          ,[Formal Customer Concern]
                          ,[Materials]
                          ,[Operator Instruction]
                          ,[Process Control]
                          ,[Safety]
                          ,[Training]
                          ,[Plant]
                          ,[Level]

                        )
                  values (?,?,?,?,?,?,?,?,?,?,?)"""
                            ,ROW['WeekEnding']
                            ,ROW['Calibration']
                            ,ROW['Docs and Records']
                            ,ROW['Formal Customer Concern']
                            ,ROW['Materials']
                            ,ROW['Operator Instruction']
                            ,ROW['Process Control']
                            ,ROW['Safety']
                            ,ROW['Training']
                            ,ROW['Plant']
                            ,ROW['Level']

                      ) 
    cursor.commit()


# Execute a stored procedure that merges data into final desination tables in the database


cursor.execute("""{CALL [clip].[Merge_Clip_LayerdProcessAudit]}""")
cursor.commit()
cursor.close()

