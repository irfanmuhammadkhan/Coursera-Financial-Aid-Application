# Q1 Coursera Financial Aid Application
# Why are you applying for Financial Aid? (150 words minimum required)
 
application = '''My name is <|NAME|>, I'm a student from <|COUNTRY|> and I want to learn <|COURSE NAME|> Course. I think it will be beneficial for my work. But I've no job of my own to carry the expenses to pay for the certificate of this course, it is very difficult for me to gather such an amount of money for the certificate. Financial Aid will help me take this course without any adverse impact on my monthly essential needs. So, I'm in need of this financial aid. I want to take this course as I want to learn. This course will boost my career. It will help me perform better in understanding and learning this technology and give me an edge over my competitors. A verified certificate will attach credibility to the certificate I receive from this course. I plan to complete all assignments on or before time as I have done in previous Signature Track Courses. Also, I intend to participate in Discussion Forums, which I have found to supplement my learning immensely in the other online courses I have taken on Coursera. I also plan to grade assignments that are peer-reviewed which I believe will be an invaluable learning opportunity.
'''
name = input("Enter Your Full Name: ")
country = input("Enter Your Counry Name: ")
course = input("Enter Your Course Name: ")
application = application.replace("<|NAME|>", name)
application = application.replace("<|COUNTRY|>", country)
application = application.replace("<|COURSE NAME|>", course)

print(application)

