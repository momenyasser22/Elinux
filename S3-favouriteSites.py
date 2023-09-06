import webbrowser
facebook = "https://www.facebook.com/"
instagram = "https://www.instagram.com/"
youtube ="https://www.youtube.com/"
linkedin = "https://www.linkedin.com/"
github = "https://github.com/"
twitter = "https://twitter.com/"

print ("Welcome to the Favourite Sites\n")
print ("1. Facebook\n2. Instagram\n3. Youtube\n4. Linkedin\n5. Github\n6. Twitter")
Choice =int (input("Enter number choice"))
    
if Choice == 1:
    webbrowser.open(facebook)
elif Choice == 2:
    webbrowser.open(instagram)
elif Choice == 3:
    webbrowser.open(youtube)
elif Choice == 4:
    webbrowser.open(linkedin)
elif Choice == 5:
    webbrowser.open(github)
elif Choice == 6:
    webbrowser.open(twitter)
else:
    print("Invalid Choice")
