# GeoHaz Early Warning

## Anthony Semeraro 
## 15 March 2021

### Built for GEOL 597T Final Project. 

## Background

Geologic Hazards pose great risk to infrastructure, economics, and human life. Having an early warning system can help mitigate many of these risks by allowing infrastructure to prepare (shutting off gas lines, stopping trains, etc.) along with humans to react (initiate evacuation plans, grab essential items, etc.). Depending on your proximity to these hazards, minutes to even seconds can make the difference between life and death. Currently early warning systems in the US are in their infancy, or lack any ability to customize when you get an alert, or are located on social media platforms. I wanted to have a more customizable early warning system that will send alerts directly to my phone as a text message that I can adjust the notification so I know that it is a unique notification. 

*** Please subscribe to Government alerts on your phone and to tsunami twitter feeds for professional early warning alerts. ***

### Limitations

This script relies on local power, Internet, and cellular communications. If the power or Internet signals go down, this will not work. If only the cellular communications go down, then the SMS messaging will fail but the email messaging will continue to work. Currently this program only works for Tsunami .xml files from Tsunami.gov, but will be expanded soon for other geologic hazards. These Tsunami alerts only report tsunami dangers to Alaska, BC, and the Western US. If you live outside of these regions, this will only notify you of events but will not send any specific wave time or risk to your local region.  

# Use of this program 

This program is designed to run constantly in the background. Remember this if you restart your computer to restart this program if you are using it. Best practice is to run this script on a server or another machine that is constantly running to prevent any issues. 

### User Inputs

- Update the section for sms protocols with your specific number and the email ending for your specific carrier. 

- Update the sending email with a non-important Gmail account and password, as you have to allow apps by unidentified developers and disable two-factor authentication. 

- Update the receiving email with a Gmail account that you monitor closely for alert messages.  

# Get Hash

This function checks the tsunami.gov xml deliverable with different browsers to prevent the ip address from being banned. Every time it pulls the hash information from the input URL, it compares that info with the info from the last time it pulled the information to compare them. If they are the same, the URL has not been updated, and the loop will continue. If the info does not match, then the URL was updated, and the Early Warning function will be initiated. 

# Early Warning

This function reads in the .xml file and parses the important information. Once the information is pulled out of the file, it is organized into messages for text and email. Then it activates the sms and email servers, attaches the messages to headers, and sends the message. Once the message is sent, the hash is cleared, and the loop continues checking until the next update to the Tsunami.gov deliverables.

[Early_Warning_poster.pdf](https://github.com/TonySombrero/GeoHaz_Early_Warning/files/6167975/Early_Warning_poster.pdf)
