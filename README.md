# GeoHaz_Early_Warning

## Anthony Semeraro 

### Built for GEOL 597T Final Project. 

## Background

Geologic Hazards pose great risk to infrastructure, economics, and human life. Having an early warning system can help mitigate many of these risks by allowing infrasturcture to prepare (shutting off gas lines, stopping trains, etc) along with humans to react (initiate evacuation plans, grab essential items, etc).  

Many of these events (Tsuanami, Volcano, Wildfire) will occur where relocation
within a short time span is required to mitigate loss of life. Depending on your proximity to these hazards, minutes to even seconds can make the differenece 
between life and death. Currently early warning systems in the US are in their infancy, or lack any ability to customize when you get an alert, or are located 
on social media platforms. I wanted to have a more customizable early warning system that will send alerts directly to my phone as a text message that I can 
change the parameters of what is sent. 

### Please subscribe to Government alerts on your phone and to tsunami twitter feeds for professional early warning alerts. 

Currently this program only works for Tsunami .xml files from Tsunami.gov, but will be expanded soon for other geologic hazards. 

The email protocol is commented out for now as the email section errors out on my raspberry pi. 

Ultimate goal of this program is to have it cycling constantly on a raspberry pi so that it is running 24/7 to send an alert within 60 seconds of the alert is sent. 

# Use of this program 

Update the section for sms protocols with your specific number and the code for the specific carrier. 

Also update the email protocols, as well as use your own email to send the messages to your phone/email. 

It is required to manually override blocks from unidentified developers for the email protocol for both sms and email messages to go through. 
2 factor identification will also need to be manually removed, it is recommended to create a dummy email to use as the sending email to 
prevent any security hacks with critical emails. 

# Get Hash

This function checks the tsunami.gov xml deliverable every 60 seconds with different browsers to prevent the ip address from being banned. \

# Early Warning

This function downloads the .xml file and parses the important information to send. Then it activates the sms and email protocols to send the message. 


