#!/usr/bin/env python3
#script to utilize html to render questions in the proper format





#import what we need (package) 

import html


#the data in question is found below
trivia= {
         "category": "Entertainment: Film",
         "type": "multiple",
         "question": "Which of the following is NOT a quote from the 1942 film Casablanca? ",
         "correct_answer": "&quot;Frankly, my dear, I don&#039;t give a damn.&quot;",
         "incorrect_answers": [
             "&quot;Here&#039;s lookin&#039; at you, kid.&quot;",
             "&ldquo;Of all the gin joints, in all the towns, in all the world, she walks into mine&hellip;&rdquo;",
             "&quot;Round up the usual suspects.&quot;"
            ]
        }

#slicing to get whats needed

question= trivia["question"]
correct= trivia["correct_answer"]
incorrect1= trivia["incorrect_answers"][0]
incorrect2= trivia["incorrect_answers"][1]
incorrect3= trivia["incorrect_answers"][2]

#now with variables defined, lets print what the challenge asks for utilizing html.something

##print((html.unescape)correct_answer)

##print((html.unescape)(s)correct)

##print the correct answer
print(html.unescape(correct))
print(html.unescape(incorrect1))
print(html.unescape)(incorrect2)
print(html.unescape(incorrect3))
