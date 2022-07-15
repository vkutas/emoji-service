## Emoji Service
Python service which can provide you with emoji you like.

The service can accept http and https requests with POST and GET methods. POST request receive JSON object of the following format: 
`{"word":"name", "count": n}` and returns a string which consists of 'name' repeated 'n' times using emoji which name is equal to the 'name' as delimeter. If there is no emoji with the name 'name', random emoji is used instead. 
 
 **http POST  example:**  
 Request:  
 `curl -X POST -d '{"word":"owl", "count":3}' http://<ip_address>`  
 Response:  
 `🦉owl🦉owl🦉owl🦉`

**POST https example:** 
Because server uses self-signed SSL certificate, you should use `-k` flag to ask curl don't verify it:  
 `curl -X POST -k -d '{"word":"dolphin", "count":5}' https://<ip_address>`  
 Response:  
 `🐬dolphin🐬dolphin🐬dolphin🐬dolphin🐬dolphin🐬`  

 or, you can import certificate from them server and tell curl where it located.

 **WARNING: Don't use mentioned above approach with production servers, only for testing purpose on local machine!**

GET http and https request returns greetings page. You can see it in your browser typing server IP in address line.

New Line
New Line2
