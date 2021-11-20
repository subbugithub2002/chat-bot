#import the library
from nltk.chat.util import Chat, reflections
pairs = [
      ['my name is (.*)', ['hello %1 i am chatbot , how can i help you']],
      ['(What is the novel coronavirus?)', ['COVID-19 is a respiratory disease that affects your breathing and spreads from person-to-person contact.\n How it affects each person varies from mild to severe illness or death.\n Currently, there is no vaccine or treatment for COVID-19.\n The majority of individuals who get COVID-19 experience mild illness that can be monitored at home.\n Individuals who experience severe illness need to be hospitalized']],
      ['(where was the covid 19 first identified?)', ['it was first found in Wuhan, China, in December 2019.']],
      ['(Where did the coronavirus disease originate?)',['On 31 December 2019,\n the World Health Organization ( WHO ) was informed of a cluster of cases of pneumonia of unknown \n cause detected in Wuhan City, Hubei Province, China.']],
      ['(What causes covid 19?)',['covid 19 is caused by infection with the severe \n acute respiratory syndrome coronavirus 2 (SARS-CoV-2) virus strain']],
      ['(Is covid 19 caused by a virus or a bacteria?)',['The coronavirus disease (COVID-19) is caused \n by a virus, NOT by bacteria.']],
      ['(Can you get covid 19 after vaccine?)',['If you have been  vaccinated with a COVID-19 vaccine,\n you are less likely to catch COVID-19, and to become severely ill if you do catch \n it. You are also less likely to spread COVID-19 to other \n people, but it is still possible for this to happen.']],
      ['(What are the symptoms of COVID-19?)',['The most common symptoms of COVID-19 are Fever,Dry cough,Fatigue']],
      ['(What happens to people who get COVID-19?)',['Among those who develop symptoms, most (about 80%) recover from the disease without needing hospital treatment. \n About 15% become seriously ill and require oxygen and 5% become critically ill and need intensive care']],
      ['(Who is most at risk of severe illness from COVID-19?)',['People aged 60 years and over, and those with underlying medical problems like \n high blood pressure, heart and lung problems, diabetes, obesity or cancer, are at \n higher risk of developing serious illness.']],
      ['(What test should I get to see if I have COVID-19?)',['In most situations, a molecular test is used \n to detect SARS-CoV-2 and confirm infection. Polymerase chain reaction \n (PCR) is the most commonly used molecular test']],
      ['(What is the incubation period for COVID-19?)',['The incubation period for COVID-19 is thought to be within 14 days following exposure, \n with most cases occurring approximately four to five days after exposure']],
      
]
 chat = Chat(pairs, reflections)
chat.converse()
