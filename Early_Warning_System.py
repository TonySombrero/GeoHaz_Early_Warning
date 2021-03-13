# Early Warning System 
# Anthony Semeraro
# Mar 08, 2021

# *** Currently only operational for Tsunami Warnings and offshore earthquakes with potential for Tsunamis ***

# Uses hash to check for updates to the Pacific US Tsunami Alert Site .xml deliverables, initiates Early Warning Function
# if a change is detected. Auto updates every 60 seconds to stay up to date. 

# Once Early Warning is initiated, the .xml file is read in, parsed for critical information, and dispersed to select 
# phone numbers as SMS messages and emails containing more information. 

import hashlib
import urllib3
import random
import time

# XML Parsing
from xml.etree import cElementTree as ET
import requests
import re

# SMS Messaging Protocol
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Time
from datetime import datetime

# Email Messaging Protocol
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# url to be scraped
url = 'https://www.tsunami.gov/events/xml/PAAQCAP.xml'

# time between checks in seconds
sleeptime = 60

def getHash():
    # random integer to select user agent
    randomint = random.randint(0,7)

    # User_Agents
    # This helps skirt a bit around servers that detect repeaded requests from the same machine.
    # This will not prevent your IP from getting banned but will help a bit by pretending to be different browsers
    # and operating systems.
    user_agents = [
        'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11',
        'Opera/9.25 (Windows NT 5.1; U; en)',
        'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
        'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)',
        'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.142 Safari/535.19',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:11.0) Gecko/20100101 Firefox/11.0',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:8.0.1) Gecko/20100101 Firefox/8.0.1',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.151 Safari/535.19'
    ]

    http = urllib3.PoolManager()
    request = http.request(
        "GET",
        url,
        headers = {
            "User-agent": user_agents[randomint]
        }
    )

    return hashlib.sha224(request.data).hexdigest()

current_hash = getHash() # Get the current hash, which is what the website is now

def Early_Warning():
    xmlfile = requests.get(url, allow_redirects=True)

    # Writing informaiton to a .xml file
    open('Tsunami.xml', 'wb').write(xmlfile.content)

    # Preparing the parsing of the .xml file
    tree = ET.parse('Tsunami.xml')
    root = tree.getroot()

    iterator = tree.iter()

    # Parsing the .xml file

    for data in tree.iter():
        info = str(data)
        if 'event' in info:
            event = info.split("'")[1::2]

        if 'description' in info:
            description = info.split("'")[1::2]
            
        if 'instruction' in info:
            instruction = info.split("'")[1::2]
            
        if 'areaDesc' in info:
            areadesc = info.split("'")[1::2]
            
        if 'circle' in info:
            location = info.split("'")[1::2]

        if 'predictedArrivalTime:' in info:
            predictarrival = info.split("'")[1::2]

        if 'value' in info:
            value = info.split("'")[1::2]
        
    message = ''
    email_message = ''

    for elem in tree.iter(event[0]):
        eventtext = (elem.text)
        eventtext = eventtext + '\n'
        #print(eventtext + '\n')

    for elem in tree.iter(description[0]):
        descriptiontext = (elem.text)
        desc = eventtext + '\n'
        #print(descriptiontext + '\n')

    for elem in tree.iter(instruction[0]):
        instructiontext = (elem.text)
        #print(instructiontext + '\n')

    for elem in tree.iter(areadesc[0]):
        areadesctext = (elem.text)
        #print(areadesctext + '\n')

    for elem in tree.iter(location[0]):
        locationtext = (elem.text)
        #print(locationtext + '\n')

    for elem in tree.iter(value[0]):
        value = (elem.text)
        value = value + '\n'
        message = message + value
        email_message = email_message + value 

    #if "NO" in instructiontext:
        #risk = "No Tsunami Risk"
        #print("No Tsunami Risk")
    #else:
        #risk = "Tsunami Risk"
        #print("Tsunami Risk")

    #%% SMS Protocol

    # Dummy email account for use as security settings have to be reduced for this protocol as it is from an 
    # unidentified developer (Anthony Semeraro)

    email = "your sending email for text protocol"
    pas = "your sending email password for text protocol"

    # SMS Gateways
    # List of cell carrier email gateways for email -> text protocol

    # AT&T: [number]@txt.att.net
    # Sprint: [number]@messaging.sprintpcs.com or [number]@pm .sprint.com
    # T-Mobile: [number]@tmomail.net
    # Verizon: [number]@vtext.com
    # Boost Mobile: [number]@myboostmobile.com
    # Cricket: [number]@sms.mycricket.com
    # Metro PCS: [number]@mymetropcs.com
    # Tracfone: [number]@mmst5.tracfone.com
    # U.S. Cellular: [number]@email.uscc.net
    # Virgin Mobile: [number]@vmobl.com

    sms_gateway = 'your number @carrieremailgateway.com'

    # The server we use to send emails in our case it will be gmail but every email provider has a different smtp 
    # and port is also provided by the email provider.
    smtp = "smtp.gmail.com" 
    port = 587
    # This will start our email server
    server = smtplib.SMTP(smtp,port)
    # Starting the server
    server.starttls()
    # Now we need to login
    server.login(email,pas)

    # Use the MIME module to structure our message.
    msg = MIMEMultipart()
    msg['From'] = email
    msg['To'] = sms_gateway
    # Make sure you add a new line in the subject
    msg['Subject'] = eventtext 
    # Make sure you also add new lines to your body

    # and then attach that body furthermore you can also send html content.
    msg.attach(MIMEText(message, 'plain'))

    sms = msg.as_string()

    server.sendmail(email,sms_gateway,sms)

    # lastly quit the server
    server.quit()

    #%% Email Sending

    sender_email = "your sending email here"
    receiver_email = "your receiver email here"
    password = "your sending email password here"

    message = MIMEMultipart("alternative")
    message["Subject"] = "Early_Warning_Message"
    message["From"] = sender_email
    message["To"] = receiver_email

    # Create the plain-text and HTML version of your message
    text = email_message
    #html = Tsunami.xml

    # Turn these into plain/html MIMEText objects
    part1 = MIMEText(text, "plain")
    #part2 = MIMEText(html, "html")

    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    message.attach(part1)
    #message.attach(part2)

    # *** Need to figure out smtplib issues on raspberry pi for email section to work ***

    # Create secure connection with server and send email
    context = ssl.create_default_context()     #context=context
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender_email, password)
        server.sendmail(
            sender_email, receiver_email, message.as_string()
        )


while 1: # Run forever
    if getHash() != current_hash: # If the webpage has updated, initiate Early_Warning()
        Early_Warning()

    # Remnant else statement for testing 

    #else: # If something has not changed
        #Early_Warning()
        #print("yay")
    time.sleep(sleeptime) # Sleeps the loop for 60 seconds before trying again

