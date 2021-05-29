from flask import Flask, request
import requests
import json
import twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


@app.route('/bot', methods = ['GET','POST'])
def bot():
    incoming_msg = request.values.get('Body', '').lower()
    #print(incoming_msg)
    resp = MessagingResponse()
    msg = resp.message()
    responded = False

    if 'hi' in incoming_msg or 'hey' in incoming_msg or 'heya' in incoming_msg or 'menu' in incoming_msg:
        text = f'Hello Fella!, \nThis is ELIZA, a covid bot to provide latest information updates corona virus for you and your family to stay stay safe.\n For any emergency 👇 \n 📞 Helpline: 011-23978046 | Toll-Free Number: 1075 \n ✉ Email: ncov2019@gov.in \n\n Please enter one of the following option 👇 \n *A*. Get information on countries and COntinents. \n *B*. Get information on vaccination in India. \n *C*. How does it *Spread*? \n *D*. *Preventive measures* to be taken.'
        msg.body(text)
        responded = False

    # IF-ELSE Statements

    if 'C' in incoming_msg:
        text = f'_Coronavirus spreads from an infected person through_ 👇 \n\n ♦ Small droplets from the nose or mouth which are spread when a person coughs or sneezes \n\n ♦ Touching an object or surface with these droplets on it and then touching your mouth, nose, or eyes before washing your hands \n \n ♦ Close personal contact, such as touching or shaking hands \n Please watch the video for more information 👇 https://youtu.be/0MgNgcwcKzE \n\n 👉 Type G to check the *Preventive Measures* \n 👉 Type *A, B, C, D, E* to see other options \n 👉 Type *Menu* to view the Main Menu'
        msg.body(text)
        msg.media('https://user-images.githubusercontent.com/34777376/77290801-f2421280-6d02-11ea-8b08-fdb516af3d5a.jpeg')
        responded = True
    
    if 'D' in incoming_msg:
        text = f'_Coronavirus infection can be prevented through the following means_ 👇 \n ✔️ Clean hand with soap and water or alcohol-based hand rub \n https://youtu.be/EJbjyo2xa2o \n\n ✔️ Cover nose and mouth when coughing & sneezing with a tissue or flexed elbow \n https://youtu.be/f2b_hgncFi4 \n\n ✔️ Avoid close contact & maintain 1-meter distance with anyone who is coughing or sneezin \n https://youtu.be/mYyNQZ6IdRk \n\n ✔️ Isolation of persons traveling from affected countries or places for at least 14 day \n https://www.mohfw.gov.in/AdditionalTravelAdvisory1homeisolation.pdf \n\n ✔️ Quarantine if advise \n https://www.mohfw.gov.in/Guidelinesforhomequarantine.pdf \n\n 👉 Type *A, B, C, D, E, F* to see other option \n 👉 Type *Menu* to view the Main Menu'
        msg.body(text)
        msg.media('https://user-images.githubusercontent.com/34777376/77290864-1c93d000-6d03-11ea-96fe-18298535d125.jpeg')
        responded = True

    if responded == False:
        msg.body('I only know about Covid-19, sorry!')

    return str(resp)

if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True)