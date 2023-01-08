class Human:
    def __init__(self, name):
        self.name = name

    # ответ по умолчанию для всех одинаковый, можно 
    # доверить его родительскому классу
    def answer_question(self, question):
        
        print(f'{self.name}, {question}\nОчень интересный вопрос! Не знаю.')


class Student(Human):
    #  метод ask_question() принимает параметр someone:
    #  это объект, экземпляр класса Curator, Mentor или CodeReviewer,
    #  которому Student задаёт вопрос; 
    #  параметр question — это просто строка
    #  имя объекта и текст вопроса задаются при вызове метода ask_question
    def ask_question(self, someone, question):
        self.someone = someone
        self.question = question
        
        result = someone.answer_question(question)
        if result != None:
            print(result)
            
        print()  # этот print выводит разделительную пустую строку	


class Curator(Human):
    def answer_question(self, question):
        if question == 'мне грустненько, что делать?':
            return (f'{self.name}, {question}\nДержись, всё получится. Хочешь видео с котиками?')
        return super().answer_question(question)
        # здесь нужно проверить, пришёл куратору знакомый вопрос или нет
        # если да - ответить на него
        # если нет - вызвать метод answer_question() у родительского класса

# объявите и реализуйте классы CodeReviewer и Mentor
class CodeReviewer(Human):
    def answer_question(self, question):
        if question == ('что не так с моим проектом?'):
            return (f'{self.name}, {question}\nО, вопрос про проект, это я люблю.')
        else:
          return super().answer_question(question)    
    
class Mentor(Human):
    def answer_question(self, question):
        if question == 'как устроиться работать питонистом?':
            return (f'{self.name}, {question}\nСейчас расскажу.')
        elif question == 'мне грустненько, что делать?':
                return (f'{self.name}, {question}\nОтдохни и возвращайся с вопросами по теории.')  
                   
        return super().answer_question(question)
            

# следующий код менять не нужно, он работает, мы проверяли
student1 = Student('Тимофей')
curator = Curator('Марина')
mentor = Mentor('Ира')
reviewer = CodeReviewer('Евгений')
friend = Human('Виталя')
 
student1.ask_question(curator, 'мне грустненько, что делать?')
student1.ask_question(mentor, 'мне грустненько, что делать?')
student1.ask_question(reviewer, 'когда каникулы?')
student1.ask_question(reviewer, 'что не так с моим проектом?')
student1.ask_question(friend, 'как устроиться на работу питонистом?')
student1.ask_question(mentor, 'как устроиться работать питонистом?')