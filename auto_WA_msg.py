# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 08:11:22 2021

@author: Pratik Walawalkar
@Discription: Send and schedule messages on WhatsApp
"""
import pywhatkit as whatsapp
from datetime import datetime


class send_message:
    

    current = datetime.now()
    current_hour = current.strftime("%H") 
    current_minutes = int(current.strftime("%M"))+1

    
    def contact_info():
        number = "+91123456789"                # Enter contact no. or group id here (group id is available in group link)
        message = "Test message using python"    # Enter the message to be sent
        hours = send_message.current_hour        # Enter hours
        minutes = send_message.current_minutes   # Enter minutes        

        send_message.send_msg(number, message, hours, minutes)
            
    def send_msg(contact, message, hours , minutes):

        whatsapp.sendwhatmsg(contact, message, hours, minutes )
        


if __name__ == "__main__":

    send_message.contact_info()