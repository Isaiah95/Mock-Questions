def main():
    extenstions(input("File name: "))


def extenstions(e): # checks to see which extetnstion the file is in then tells you the MIME type

    if ".gif" in e: # in checks to see if the the string ".gif" is contained inside the string. if so it will print "image/jpeg"

        print ("image/gif")

    elif ".jpg" in e or ".jpeg" in e: #both jpg and jpeg use image/jpeg

        print ("image/jpeg")

    elif ".png" in e:
        
         print ("image/png")
         
    elif ".pdf" in e:
        
         print ("application/pdf")
    elif ".txt" in e:
        
         print ("text/plain")
    elif ".zip" in e:

         print ("application/zip")
    else:

         print ("application/octet-stream")  #defult value for all other cases
