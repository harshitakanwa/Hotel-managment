
from email.message import EmailMessage
import smtplib, ssl
import imghdr
from django.shortcuts import render, redirect
import datetime


def send_room_details(user_email,username , user_first_name, email_context):
    username = email_context['room_user']
    room_id = email_context['room_id']
    room_taking_date = email_context['room_taking_date']
    room_leaving_date = email_context['room_leaving_date']
    room_booking_date = email_context['room_booking_date']
    room_price = email_context['room_price']
    hall_price = email_context['hall_price']
    meal_price = email_context['meal_price']
    gym_price = email_context['gym_price']
    total_price = email_context['total_price']
    smtp_server = 'smtp.gmail.com'
    port = 465  # 587

    sender = 'hotel.cs300@gmail.com' #'library.cs303@gmail.com'
    password = "Hotel@2021" #'XK9xdYmsT5ktxmV'    # input("Enter your password : ")

    context = ssl.create_default_context()

    receivers = [
        user_email
    ]

    for receiver in receivers:
        message = EmailMessage()
        message["To"] = receiver
        message["Subject"] = "Login Details for Hotel Transylvenia"
        message["From"] = f"Hotel Transylvenia <{sender}>"
        content = f'''\
        Hi {user_first_name}.
        Our django site is deployed at https://jithendra1798.pythonanywhere.com/.
        We also need to implement automate emails. I am sending this email using Python.
        We also need to add some features we thougt in README.md file(we forgot to write some features).

        I am also sending an attachment of our project Outline.

        NOTE : I sent this message to you only for testing purpose!!

        Thanks and Regards
        Jithendra
        '''
        message.set_content(content)
        '''# Attaching images
        file_data = file_type = file_name = None
        with open("outline.png","rb") as f:
            file_data = f.read()
            file_type = imghdr.what(f.name)
            file_name = f.name

        message.add_attachment(file_data, maintype="image", subtype=file_type, filename=file_name)

        # Attaching PDF's
        with open("Project Outline.pdf","rb") as f:
            file_data = f.read()
            file_name = f.name

        message.add_attachment(file_data, maintype="application", subtype='octet-stream', filename=file_name)
        '''
        style = f'''  
            width: 25px;
            padding: 20px;
            font-size: 25px;
            text-align: center;
            text-decoration: none;
            margin: 5px 2px;
            color: white;
            border-radius: 50%; 
            '''
        # Sending HTML formatted email
        message.add_alternative(f"""<!Doctype html>
    <html>
    <head>
        <meta charset="utf-8">
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
        <style type="text/css">
            .fa {style}
        </style>
    </head>
    <body>
        <div class="aHl"></div>
        <div id=":1tf" tabindex="-1"></div>
        <div id=":1v6" class="ii gt">
            <div id=":1v7" class="a3s aiL msg514661073054809951">
                <u></u>            
                <div style="padding:0;margin:0 auto;width:100%!important;font-family:'Helvetica Neue',Helvetica,Arial,sans-serif">
                <div style="overflow:hidden;color:transparent;width:0;font-size:0;opacity:0;height:0"> Hi Guys. This email is for testing purpose.</div>
                <table role="presentation" style="background-color:#999999;table-layout:fixed" width="100%" cellspacing="0" cellpadding="0" border="0" bgcolor="#EDF0F3" align="center">
                    <tbody>
                        <tr>
                            <td align="center">
                            <center style="width:100%">
                                <table role="presentation" class="m_514661073054809951phoenix-email-container" style="background-color:#ffe4e1;margin:0 auto;max-width:700px;width:inherit" width="512" cellspacing="0" cellpadding="0" border="0" bgcolor="#FFFFFF">
                                    <tbody>
                                        <tr>
                                        <td style="background-color:#FFD580;padding:5px 16px 13px;border-bottom:1px solid #ececec" bgcolor="#F6F8FA">
                                            <table role="presentation" style="width:100%!important;min-width:100%!important" width="100%" cellspacing="0" cellpadding="0" border="0">
                                                <tbody>
                                                    <tr>
                                                    <td valign="middle" align="left"><a href="https://jithendra1798.pythonanywhere.com/" style="color:#0073b1;display:inline-block;text-decoration:none" target="_blank" data-saferedirecturl="https://www.google.com/url?q=https://jithendra1798.pythonanywhere.com/"> <img alt="VIM Library" src="https://github.com/jithendra1798/SE-Project/blob/main/icons/old-library-building.png?raw=true" style="max-height:42px;outline:none;color:#ffffff;max-width:unset!important;text-decoration:none" class="CToWUd" height="42" border="0"></a></td>
                                                    <td style="padding:0 0 0 10px;padding-top:7px" valign="middle" align="left"><a href="https://jithendra1798.pythonanywhere.com/" style="color:#0073b1;display:inline-block;text-decoration:none" target="_blank" data-saferedirecturl="https://www.google.com/url?q=https://jithendra1798.pythonanywhere.com/">Hotel&nbsp;Tansylvenia</a></td>
                                                    <td width="100%" valign="middle" align="right">
                                                        <a href="https://jithendra1798.pythonanywhere.com/" style="margin:0;color:#0073b1;display:inline-block;text-decoration:none" target="_blank" data-saferedirecturl="https://www.google.com/url?q=https://jithendra1798.pythonanywhere.com/">
                                                            <table role="presentation" width="100%" cellspacing="0" cellpadding="0" border="0">
                                                                <tbody>
                                                                <tr>
                                                                    <td style="padding:0 0 0 10px;padding-top:7px" valign="middle" align="left">
                                                                        <p style="margin:0;font-weight:400"> <span style="word-wrap:break-word;color:#4c4c4c;word-break:break-word;font-weight:400;font-size:14px;line-height:1.429">Admin</span></p>
                                                                    </td>      
                                                                    <td style="padding-top:7px;padding-left:10px" width="40" valign="middle"> <img alt="Admin" src="https://raw.githubusercontent.com/jithendra1798/SE-Project/main/icons/admin.jpg" style="border-radius:50%;outline:none;color:#ea4561;max-width:unset!important;text-decoration:none;" class="CToWUd" width="36" height="36" border="0"></td>
                                                                </tr>
                                                                </tbody>
                                                            </table>
                                                        </a>
                                                    </td>
                                                    <td width="1">&nbsp;</td>
                                                    </tr>
                                                </tbody>
                                            </table>
                                        </td>
                                        </tr>
                                        <tr>
                                        <td>
                                            <table role="presentation" width="100%" cellspacing="0" cellpadding="0" border="0">
                                                <tbody>
                                                    <tr>
                                                    <td>
                                                        <table role="presentation" width="100%" cellspacing="0" cellpadding="0" border="0">
                                                            <tbody>
                                                                <tr>
                                                                <td style="padding:24px 24px 36px 24px">
                                                                    <table role="presentation" width="100%" cellspacing="0" cellpadding="0" border="0">
                                                                        <tbody>
                                                                            <tr>
                                                                                <hr style="color:#9b2335;">
                                                                                <center><h4 style="color:#34568b">Welcome to Hotel Transylvenia, {user_first_name}!</h4></center>
                                                                                <hr style="color:#9b2335;">
                                                                                <br>
                                                                            </tr>
                                                                            <tr>
                                                                                <hr style="color:#9b2335;">
                                                                                <center><h4 style="color:#34568b">Room Number : {room_id}!</h4></center>
                                                                                <hr style="color:#9b2335;">
                                                                                <br>
                                                                            </tr>
                                                                            <tr>
                                                                            <td id="m_514661073054809951qatest-hero-headline" colspan="2" style="padding-bottom:12px" align="left">
                                                                                <p style="margin:0;word-wrap:break-word;color:#4c4c4c;word-break:break-word;font-weight:400;font-size:16px;line-height:1.5">This email includes your room details, you rencently booked on Hotel Transylvenia!</p><br>
                                                                            </td>
                                                                            </tr>
                                                                            <tr>
                                                                            <td id="m_514661073054809951qatest-hero-headline" colspan="2" style="padding-bottom:12px" align="left">
                                                                                <p style="margin:0;word-wrap:break-word;color:#4c4c4c;word-break:break-word;font-weight:400;font-size:18px;line-height:1.5"><b>Username : {username}</b></p>
                                                                            </td>
                                                                            </tr>
                                                                            <tr>
                                                                            <td id="m_514661073054809951qatest-hero-headline" colspan="2" style="padding-bottom:12px" align="left">
                                                                                <p style="margin:0;word-wrap:break-word;color:#4c4c4c;word-break:break-word;font-weight:400;font-size:18px;line-height:1.5"><b>Check-In date : {room_taking_date}</b></p>
                                                                            </td>
                                                                            </tr>
                                                                            <tr>
                                                                            <td id="m_514661073054809951qatest-hero-headline" colspan="2" style="padding-bottom:12px" align="left">
                                                                                <p style="margin:0;word-wrap:break-word;color:#4c4c4c;word-break:break-word;font-weight:400;font-size:18px;line-height:1.5"><b>Check-Out date : {room_leaving_date}</b></p>
                                                                            </td>
                                                                            </tr>
                                                                            <tr>
                                                                            <td id="m_514661073054809951qatest-hero-headline" colspan="2" style="padding-bottom:12px" align="left">
                                                                                <p style="margin:0;word-wrap:break-word;color:#4c4c4c;word-break:break-word;font-weight:400;font-size:18px;line-height:1.5"><b>Booking date : {room_booking_date}</b></p>
                                                                            </td>
                                                                            </tr>
                                                                            <tr>
                                                                            	<td>
<table role="presentation" width="100%" cellspacing="0" cellpadding="0" border="0" class="table table-striped">
  <thead class="thead-dark">
    <tr>
      <th scope="col">#</th>
      <th scope="col">Name</th>
      <th scope="col">Price</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th scope="row">1</th>
      <td>Room Price</td>
      <td>{room_price}</td>
    </tr>
    <tr>
      <th scope="row">2</th>
      <td>Function Hall</td>
      <td>{hall_price}</td>
    </tr>
    <tr>
      <th scope="row">3</th>
      <td>Meal / Cafe</td>
      <td>{meal_price}</td>
    </tr>
    <tr>
      <th scope="row">4</th>
      <td>Gym / Swimming Pool</td>
      <td>{gym_price}</td>
    </tr>
    <tr>
      <th scope="row">===>></th>
      <td>Total</td>
      <td>{total_price}</td>
    </tr>
  </tbody>
</table></td></tr>
                                                                            <tr>
                                                                            <td id="m_514661073054809951qatest-hero-headline" colspan="2" style="padding-bottom:12px" align="left"><br>
                                                                                <p style="margin:0;word-wrap:break-word;color:#4c4c4c;word-break:break-word;font-weight:400;font-size:16px;line-height:1.5">Thank you for booking with our Hotel Transylvenia.</p>
                                                                            </td>
                                                                            </tr>
                                                                            <tr>
                                                                            <td id="m_514661073054809951qatest-hero-headline" colspan="2" style="padding-bottom:12px" align="left">
                                                                                <br>
                                                                                <p style="margin:0;word-wrap:break-word;color:hsl(216, 71%, 36%);word-break:break-word;font-weight:400;font-size:17px;line-height:1.5">Regards,</p>
                                                                                <p style="margin:0;word-wrap:break-word;color:hsl(216, 71%, 36%);word-break:break-word;font-weight:400;font-size:17px;line-height:1.5"><b>Admin</b> - Hotel Transylvenia</p>
                                                                            </td>
                                                                            </tr>
                                                                            <tr>
                                                                            <td id="m_514661073054809951qatest-hero-headline" colspan="2" style="padding-bottom:12px" align="left">
                                                                                <br><p style="margin:0;word-wrap:break-word;color:#4c4c4c;word-break:break-word;color: red;font-weight:400;font-size:15px;line-height:1.5"><b>NOTE : This is an Automated system generated email. Do not reply to this email.</b></p>
                                                                            </td>
                                                                            </tr>
                                                                        </tbody>
                                                                    </table>
                                                                </td>
                                                                </tr>
                                                            </tbody>
                                                        </table>
                                                        <div>
                                                            <div>   </div>
                                                            <div>   </div>
                                                        </div>
                                                    </td>
                                                    </tr>
                                                </tbody>
                                            </table>
                                        </td>
                                        </tr>
                                        <tr>
                                        <td>
                                            <table role="presentation" style="background-color:#edf0f3;padding:0 24px;color:#6a6c6d;text-align:center" width="100%" cellspacing="0" cellpadding="0" border="0" bgcolor="#EDF0F3" align="center">
                                                <tbody>
                                                    
                                                    <tr>
                                                    <td>
                                                        <table role="presentation" width="100%" cellspacing="0" cellpadding="0" border="0">
                                                            <tbody>
                                                                <hr>
                                                                <a href="https://github.com/jithendra1798/SE-Project" target="_blank">
                                                                <i class="fa fa-github fa-3x" style = "background: #000000;"></i></a>
                                                                <a href="https://jithendra1798.pythonanywhere.com/" target="_blank">
                                                                <i class="fa fa-medium" style = "background: #00aff0;"></i></a>
                                                                </tr>
                                                                <hr> 
                                                                <tr>
                                                                <td style="padding:12px 0 12px 0;text-align:center" align="center">
                                                                    <p style="margin:0;color:#6a6c6d;font-weight:400;font-size:12px;line-height:1.333">You are receiving this email because you are a Hotel Transylvenia user.</p>
                                                                </td>
                                                                </tr>
                                                                <tr>
                                                                <td style="padding:0 0 16px 0;vertical-align:middle;text-align:center" valign="middle" align="center"><span style="color:#6a6c6d;font-weight:400;font-size:12px;line-height:1.333">Hotel Transylvenia © 2021</span></a>&nbsp;|&nbsp;<span style="color:#6a6c6d;font-weight:400;font-size:12px;line-height:1.333">An Automation Project by a group of 5 CSE'23 students at NITK.</span></td>
                                                                </tr>
                                                            </tbody>
                                                        </table>
                                                    </td>
                                                    </tr>
                                                </tbody>
                                            </table>
                                        </td>
                                        </tr>
                                    </tbody>
                                </table>
                            </center>
                            </td>
                        </tr>
                    </tbody>
                </table>
                
                <div class="yj6qo"></div>
                <div class="adL"> </div>
                </div>
                <div class="adL"> </div>
            </div>
        </div>
        <div id=":1ti" class="ii gt" style="display:none">
            <div id=":1tj" class="a3s aiL "></div>
        </div>
        <div class="hi"></div>
    </body>
    </html>





    """,subtype="html")

        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender, password)
            # Send email
            server.send_message(message)
            print("Email sent!")