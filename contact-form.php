<?php
    $name= $_POST['name'];
    $visitor_email = $_POST['email'];
    $message = $_POST['message'];

    $email_from=['safhira19001@mail.unpad.ac.id'];
    
    $email_subject="New sub";

    $email_body="User name: $name.\n".
                    "User email: $visitor_email.\n".
                        "User message: $message.\n";

    $to = "safhiraaprilia@gmail.com"

    $headers = "From: $email_from\r\n";

    $headers = "Reply To: $visitor_email \r\n";

    mail($to,$email_subject,$email_body,$headers);
    
    header("location: index.html");