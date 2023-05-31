class Phone:
    price = 4200
    brand = 'Apple'
    Model = 'iPhone XR'

    def SEND_SMS(self , number , sms):
        text = f"Sending SMS to : {number} and the message is {sms} "
        return text


my_phone = Phone()

output = my_phone.SEND_SMS(1734129746,"Hi there Maruf Good to See you")
print(output)