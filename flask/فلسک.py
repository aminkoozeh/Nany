from flask import Flask,render_template,request

app=Flask(__name__)

@app.route('/' , methods=["GET","post"])
def salam():
    if request.method == "POST" :
        vorody = request.form['user']
        y = ''
        r = '0'
        # r=input()
        # y=y+r+','
        for n in range(2):
            e = open('دانی.txt', 'r')
            q = e.read()
            q = q.replace('q', 'ض')
            q = q.replace('w', 'ص')
            q = q.replace('e', 'ث')
            q = q.replace('r', 'ق')
            q = q.replace('t', 'ف')
            q = q.replace('y', 'غ')
            q = q.replace('u', 'ع')
            q = q.replace('i', 'ه')
            q = q.replace('o', 'خ')
            q = q.replace('p', 'ح')
            q = q.replace('{', 'ج')
            q = q.replace('}', 'چ')
            q = q.replace('\\', 'پ')
            q = q.replace('a', 'ش')
            q = q.replace('s', 'س')
            q = q.replace('d', 'ی')
            q = q.replace('f', 'ب')
            q = q.replace('g', 'ل')
            q = q.replace('h', 'ا')
            q = q.replace('H', 'آ')
            q = q.replace('j', 'ت')
            q = q.replace('k', 'ن')
            q = q.replace('l', 'م')
            q = q.replace(';', 'ک')
            q = q.replace('"', 'گ')
            q = q.replace('z', 'ظ')
            q = q.replace('x', 'ط')
            q = q.replace('c', 'ز')
            q = q.replace('v', 'ر')
            q = q.replace('b', 'ذ')
            q = q.replace('n', 'د')
            q = q.replace('m', 'ئ')
            q = q.replace('<', 'و')
            q = q.replace('?', '؟')
            w = q.split(',')
            if r == '03':
                chorogy = w
            e.close()
            if r in w:
                chorogy = w[w.index(r) + 1]
                y = y + w[w.index(r) + 1] + ','
                r = vorody
                y = y + r + ','
            else:
                chorogy = r
                y = y + r + ','
                q = q + ',' + r
                w = w + [r]
                r = vorody
                y = y + r + ','
                q = q + ',' + r
                w = w + [r]
                r = vorody
                y = y + r + ','
            # print(w,'w')
            # print(q,'q')
            q = q.replace('ض', 'q')
            q = q.replace('ص', 'w')
            q = q.replace('ث', 'e')
            q = q.replace('ق', 'r')
            q = q.replace('ف', 't')
            q = q.replace('غ', 'y')
            q = q.replace('ع', 'u')
            q = q.replace('ه', 'i')
            q = q.replace('خ', 'o')
            q = q.replace('ح', 'p')
            q = q.replace('ج', '{')
            q = q.replace('چ', '}')
            q = q.replace('پ', '\\')
            q = q.replace('ش', 'a')
            q = q.replace('س', 's')
            q = q.replace('ی', 'd')
            q = q.replace('ب', 'f')
            q = q.replace('ل', 'g')
            q = q.replace('ا', 'h')
            q = q.replace('آ', 'H')
            q = q.replace('ت', 'j')
            q = q.replace('ن', 'k')
            q = q.replace('م', 'l')
            q = q.replace('ک', ';')
            q = q.replace('گ', '"')
            q = q.replace('ظ', 'z')
            q = q.replace('ط', 'x')
            q = q.replace('ز', 'c')
            q = q.replace('ر', 'v')
            q = q.replace('ذ', 'b')
            q = q.replace('د', 'n')
            q = q.replace('ئ', 'm')
            q = q.replace('و', '<')
            q = q.replace('؟', '?')
            t = open('دانی.txt', 'w')
            t.write(q)
            t.close()
            q = y
            q = q.replace('ض', 'q')
            q = q.replace('ص', 'w')
            q = q.replace('ث', 'e')
            q = q.replace('ق', 'r')
            q = q.replace('ف', 't')
            q = q.replace('غ', 'y')
            q = q.replace('ع', 'u')
            q = q.replace('ه', 'i')
            q = q.replace('خ', 'o')
            q = q.replace('ح', 'p')
            q = q.replace('ج', '{')
            q = q.replace('چ', '}')
            q = q.replace('پ', '\\')
            q = q.replace('ش', 'a')
            q = q.replace('س', 's')
            q = q.replace('ی', 'd')
            q = q.replace('ب', 'f')
            q = q.replace('ل', 'g')
            q = q.replace('ا', 'h')
            q = q.replace('آ', 'H')
            q = q.replace('ت', 'j')
            q = q.replace('ن', 'k')
            q = q.replace('م', 'l')
            q = q.replace('ک', ';')
            q = q.replace('گ', '"')
            q = q.replace('ظ', 'z')
            q = q.replace('ط', 'x')
            q = q.replace('ز', 'c')
            q = q.replace('ر', 'v')
            q = q.replace('ذ', 'b')
            q = q.replace('د', 'n')
            q = q.replace('ئ', 'm')
            q = q.replace('و', '<')
            q = q.replace('؟', '?')
            u = open('مکالمات دانی.txt', 'r')
            q = u.read() + q
            u.close()
            t = open('مکالمات دانی.txt', 'w')
            t.write(q)
            t.close()
            if r == '02':
                q = q.replace('q', 'ض')
                q = q.replace('w', 'ص')
                q = q.replace('e', 'ث')
                q = q.replace('r', 'ق')
                q = q.replace('t', 'ف')
                q = q.replace('y', 'غ')
                q = q.replace('u', 'ع')
                q = q.replace('i', 'ه')
                q = q.replace('o', 'خ')
                q = q.replace('p', 'ح')
                q = q.replace('{', 'ج')
                q = q.replace('}', 'چ')
                q = q.replace('\\', 'پ')
                q = q.replace('a', 'ش')
                q = q.replace('s', 'س')
                q = q.replace('d', 'ی')
                q = q.replace('f', 'ب')
                q = q.replace('g', 'ل')
                q = q.replace('h', 'ا')
                q = q.replace('H', 'آ')
                q = q.replace('j', 'ت')
                q = q.replace('k', 'ن')
                q = q.replace('l', 'م')
                q = q.replace(';', 'ک')
                q = q.replace('"', 'گ')
                q = q.replace('z', 'ظ')
                q = q.replace('x', 'ط')
                q = q.replace('c', 'ز')
                q = q.replace('v', 'ر')
                q = q.replace('b', 'ذ')
                q = q.replace('n', 'د')
                q = q.replace('m', 'ئ')
                q = q.replace('<', 'و')
                q = q.replace('?', '؟')
                chorogy = q
        return render_template('صفحه اول.html', user=chorogy)
    return render_template('صفحه اول.html', user=None)

#@app.route('/2')
#def nveshtan():
    ##vorody=request.form['title']
 #   return render_template('نوشتن.html')

#@app.route('/3' , methods=["post"])
#def gptchat():
#    vorody = request.form['user']
#    return f"نام شما:{vorody}"
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
