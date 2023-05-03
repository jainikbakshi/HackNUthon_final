# HackNUthon_final
Welcome to the GitHub repository for our project on Behavior analysis to identify cyberterrorism and extremism on the Dark Web.

Our project aims to address the complex challenge of detecting cyberterrorism and extremism on the Dark Web using state-of-the-art natural language processing and Machine
learning techniques. The system is designed to analyze large volumes of text and identify specific patterns and keywords that are indicative of cyberterrorism and extremism.
To achieve this, we utilized the TOR browser to access the Dark Web and conducted web crawling to extract relevant text from the URLs provided. We then employed a sophisticated pre-trained 
model from Hugging Face to classify this text and identify potential instances of cyberterrorism or extremism with high accuracy.

Our project also features a modular architecture, which makes it highly scalable and easily customizable. 
It provides a robust foundation for the development of new features and improvements, allowing for further refinement and adaptation to emerging threats and challenges.
We encourage interested developers and researchers to explore our codebase and documentation to learn more about the technical aspects of our approach and methods. 
Our project aims to contribute to the advancement of the field of cybersecurity and provide valuable insights for policy-makers and law enforcement agencies working to 
combat cyberterrorism and extremism.

## Flow of the project

1. Ahmia.py scrapes all the onion websites for a particular keyword which is chosen randomly by the computer.
2. If a user wants to access data of "N" files, N is given as an input to the tor1.py file which scrapes the data out of first "N" Onion files.
3. Run text.py to filter all the html tags and get the raw data.
4. app.py is a flask based GUI.

It is still not connected whole with the backend, but we plan to do it in near future.

## Our GUI 

### Home Page
![home](https://user-images.githubusercontent.com/65659074/235864724-8d582050-8941-4e94-8f52-c0d7af41ad0a.png)

### Testimonials
![test](https://user-images.githubusercontent.com/65659074/235864776-6e9c0a6d-1d70-49e0-b280-5b0f56b2e1ef.jpg)

### Services
![serv](https://user-images.githubusercontent.com/65659074/235864811-dd4be47b-eae3-42ec-a003-163a44b157f4.jpg)
