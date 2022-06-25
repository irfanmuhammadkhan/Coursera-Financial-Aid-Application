# Q2 Coursera Financial Aid Application
# Why are you applying for Financial Aid? (150 words minimum required)
 
application = '''My main career goal is to learn every day. I really want to learn and progress in my career. Becoming an expert requires constant learning and improvement. Taking this course will help me to learn and study <|COURSE NAME|> and also implement it. It can help me advance in my knowledge. This course will help me in defining <|COURSE NAME|>, understand the potential impact of our business and industry, write a thought leadership piece regarding use cases and industry potential of <|COURSE NAME|>, explain <|COURSE NAME|> to clients, and friends, join a community of economists, business leaders, entrepreneurs, and technologists that are shaping this technology as we speak. Identifying which aspects of <|COURSE NAME|> seem most important and relevant to us, walking away with a strong foundation in where <|COURSE NAME|>, what it does, and how to prepare for it. The <|COURSE NAME|> course will help me achieve it to learn. Courses on Coursera helped me to greatly increase my knowledge in the past. Thank you so much, Coursera.
'''
course = input("Enter Your Course Name: ")
application = application.replace("<|COURSE NAME|>", course)

print(application)

