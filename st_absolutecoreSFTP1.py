#st_absolutecoreSFTP1.py
#20240724 ver:001
import streamlit as st
import pyAesCrypt
#import os
import paramiko
#from path import Path
#import datetime

st.title("Core SFTP")

def btn_func()
    paramiko.util.log_to_file("paramiko.log")
    host,port = "ssh.pythonanywhere.com",22
    
    transport = paramiko.Transport(host,port)
    username = "alastair"
    password = 'q548*"rBa)kC>6xZ;VPFp-'  #changed 20240628
    
    transport.connect(username=username,password=password)
    sftp = paramiko.SFTPClient.from_transport(transport)
    
    # Upload from my desktop to pythonanywhere, London, UK
    bufferSize = 64 * 1024
    key = "Qa23cf542!28&^9856"
    
    pyAesCrypt.encryptFile("outward_bound.txt", "outward_bound.txt.aes", key)
    
    outfile = "outward_bound.txt.aes"
    localpath = outfile
    filepath = "/home/alastair/encrypted/" + outfile
    sftp.put(localpath,filepath)

    if sftp: sftp.close()
    if transport: transport.close()

if st.button("Submit", on_click=btn_func)

st.write('finished')


    

