import os

print("""
\x1b[38;2;255;20;147m
                           _              
                          (_)             
 ___ _   _ _ __ ___   __ _ _ _   _  __ _  
/ __| | | | '_ ` _ \ / _` | | | | |/ _` | 
\__ \ |_| | | | | | | (_| | | |_| | (_| | 
|___/\__,_|_| |_| |_|\__,_|_|\__, |\__,_| 
                              __/ |       
                             |___/\x1b[38;2;0;255;58m>(sumaiya )
""") 

print("""[1] pip\n[2] pip3\nWhich one do you use?""")

c = input(">>>: ")
if c == "1":
    os.system("pip install cloudscraper")
    os.system("pip install socks")
    os.system("pip install pysocks")
    os.system("pip install colorama")
    os.system("pip install undetected_chromedriver")
    os.system("pip install httpx")

elif c == "2":
    os.system("pip3 install cloudscraper")
    os.system("pip3 install socks")
    os.system("pip3 install pysocks")
    os.system("pip3 install colorama")
    os.system("pip3 install undetected_chromedriver")
    os.system("pip3 install httpx")
if os.name == "nt":
    pass
else:
    os.system("wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb")
    os.system("apt-get install ./google-chrome-stable_current_amd64.deb")

print("Done.")
