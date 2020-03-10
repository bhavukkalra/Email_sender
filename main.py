import pandas as pd
import smtplib
import email
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

#Tried to use these functions to improve 
#code readibility but problems faced
# in future to do list till then 
# did this the old fashioned way
def get_name(df,iterable):
    return str((df["Name"][iterable]))
    
def get_email(df,iterable):
    return str((df["Email"][iterable]))

df = pd.read_csv("PATH TO GOOGLE FORMS CSV")

#need attributes names from dataframe and filename
def send_mail(name,send_email):

    
    
    
    #html to include in the body section
    html = """
    

    Good Day,<br><br> 
    Basic Template
    <br>
    Best Regards <br>
  
    """

    # Creating message.
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "TITLE"
    msg['From'] = "SENDER'S NAME"
    msg['To'] = send_email

    # The MIME types for text/html
    HTML_Contents = MIMEText(html, 'html')

    # Adding pptx file attachment
    #FOR ADDING AN ATTACHMENT 
    #Un comment attach functions
    #temp_filename = name
    
    #filename= str(name) + '.pdf'
    fo=open(filename,'rb')
    #attach = email.mime.application.MIMEApplication(fo.read(),_subtype="pdf")
    fo.close()
    #attach.add_header('Content-Disposition','attachment',filename=filename)

    # Attachment and HTML to body message.
    #msg.attach(attach)
    msg.attach(HTML_Contents)
    


    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('SENDER'S EMAIL ID','AUTHORISATION CODE FROM GMAIL')

    

    server.sendmail('SENDER'S EMAIL ID',send_email,msg.as_string())
    print("sent mail to ",name, "  ", send_email)
    server.quit()



 if __name__ = "__main__":
     #driver function
     for i in range(0,df.shape[0]):
    cur_name = df['Name'][i]
    cur_email = df['Email'][i]
    send_mail(cur_name,cur_email)




 #alternate driver function 
 #incroporating user input ambiguity 


# if __name__ = "__main__":

#     driver function
   
#     new_name = ""
#     cur_name = df['Name'][i]
#     cur_email = df['Email'][i]
#     for i in range(len(cur_name)-1):,
#         new_name = new_name + cur_name[i]
#     send_mail(new_name,cur_email)
     


    
