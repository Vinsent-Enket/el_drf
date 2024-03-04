s = 'http://google.com/sdfdsfsdf dfs'
d = 'http://YouTube.com/dsfdsf'
q = 'http://127.0.0.1:8000/zdasdasd'

value = [s, d, q]
permitted_words = ['http://youtube.com', 'http://127.0.0.1:8000']

# сделать приведение к одному регистру
# сделать валидар на формат ссылки, убрать http и тд
# dict(value).get(self.field) разобраться


for word in value:
    word2 = word.lower()
    if word2.startswith('http://youtube.com') or word2.startswith('http://127.0.0.1:8000'):
        print(word, 'подходит')
    else:
        print(word, ' не подходит')

