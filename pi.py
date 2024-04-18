text_1 = """How I want a drink, alcoholic of course, after the heavy chapters involving quantum mechanics. All of thy geometry, Herr Planck, is fairly hard."""

#text_1からカンマとピリオドを消す。
text_2 = text_1.replace(',',"").replace('.',"")

#空白によって文字列を分割し、各要素の長さを求める。更にリストにする。
text_3 = list(map(len, text_2.split(" ")))

#textの各要素を文字列に変換して連結する。
result = ''.join([str(x) for x in text_3])

print(result) 