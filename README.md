# Photo-Album

**Install Instructions:**

This app utilizes the Requests library, users will need to install the package. 

* Open your terminal and run the following command:
- Windows: python -m pip install requests

- MAC: 
  1) sudo easy_install pip
  2) sudo pip install --upgrade pip 
  3) pip install requests
  
- Linux: pip install requests

**How to run app:**
* Run the application by navigating to the main.py file.
* To retrieve a photo id, provide an integer value between 1 and 5000.
* NOTE: If invalid input is given, (i.e: "-1" or a string value) a prompt will be given.


**Future Implementations**

After reflecting on my application, these are a couple features that I would like to implement in the future.
* Build off my unittests and implement full integration tests for main().
* Create a format method to handle any specific formatting demands. This way it would allow, depending on business requirements, any specified return value instead of the full string.
