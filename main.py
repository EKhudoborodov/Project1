from flask import Flask, render_template, request
from translate import Translator

app = Flask(__name__)

translator_en_ru = Translator(from_lang='English', to_lang='Russian')
translator_en_fr = Translator(from_lang='English', to_lang='French')
translator_en_ge = Translator(from_lang='English', to_lang='German')
translator_ru_en = Translator(from_lang='Russian', to_lang='English')
translator_ru_fr = Translator(from_lang='Russian', to_lang='French')
translator_ru_ge = Translator(from_lang='Russian', to_lang='German')
translator_fr_en = Translator(from_lang='French', to_lang='English')
translator_fr_ru = Translator(from_lang='French', to_lang='Russian')
translator_fr_ge = Translator(from_lang='French', to_lang='German')
translator_ge_en = Translator(from_lang='German', to_lang='English')
translator_ge_ru = Translator(from_lang='German', to_lang='Russian')
translator_ge_fr = Translator(from_lang='German', to_lang='French')

#@app.route('/<name>')
#def index(name):
#    return render_template('index.html', name=name)


#@app.route('/hello/<name>')
#def hello_with_name(name):
#    return f"hello {name}"

@app.route('/', methods=['GET', 'POST'])
def dict_page():
    if request.method == 'POST':
        word = request.form["word"]
        lang = request.form["lang"]
        if lang == 'EN':
            w1 = translator_en_ru.translate(word)
            w2 = translator_en_fr.translate(word)
            w3 = translator_en_ge.translate(word)
        else:
            if lang == 'RU':
                w1 = translator_ru_en.translate(word)
                w2 = translator_ru_fr.translate(word)
                w3 = translator_ru_ge.translate(word)
            else:
                if lang == 'FR':
                    w1 = translator_fr_ru.translate(word)
                    w2 = translator_fr_en.translate(word)
                    w3 = translator_fr_ge.translate(word)
                else:
                    w1 = translator_ge_ru.translate(word)
                    w2 = translator_ge_en.translate(word)
                    w3 = translator_ge_fr.translate(word)
        return render_template('result.html', word1=w1, word2=w2, word3=w3)

    return render_template('dict.html')

if __name__ == '__main__':
    app.run()