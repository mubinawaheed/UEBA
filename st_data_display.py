
import pandas as pd
import streamlit as st

# import Device_MP as dv

# import matrixprofile as mp


file_names=["device.csv","file.csv","logon.csv","psychometric.csv","email.csv"]
st.title("UEBA data (r4.2)")

# for i in file_names:
#st.text("Device Data")    
# data1=pd.read_csv("device.csv")
# data2=pd.read_csv("email.csv")
# data3=pd.read_csv("file.csv")

# st.write(i+ " Data")
# st.dataframe(data1)
# st.dataframe(data2)
# st.dataframe(data3)
device,file,logon,psychometric,email=st.tabs(file_names)
with device:
    dev=pd.read_csv("device.csv")
    st.subheader("Device Data") 
    st.dataframe(dev)
    # x=dv.profileDate
    
    st.image(r'motifs_date.png')
    st.image(r'discord_date.png')
    st.image(r'motifs_hour.png')
    st.image(r'discord_hour.png')
    
    # st.line_chart(x['data']['ts'])
    
    # st.line_chart(x['mp'])
    
# with email:
#     em=pd.read_csv("email.csv",nrows=150)
#     st.subheader("Email Data") 
#     st.dataframe(em)
# with file:
#     fl=pd.read_csv("file.csv",nrows=150)
#     st.subheader("file Data")
#     st.dataframe(fl)
# with logon:
#     lgn=pd.read_csv("logon.csv", nrows=150)
#     st.subheader("logon data")
#     st.dataframe(lgn)
# with psychometric:
#     psycho=pd.read_csv("psychometric.csv",nrows=150)
#     st.subheader("psychometric Data")
#     st.dataframe(psycho)
    
    
    
    
    
    
    
    
    



#st.dataframe(device)

