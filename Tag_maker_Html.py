def HTML_Tag_maker(Tagname,Text):
    print(f'<{Tagname}>{Text}</{Tagname}>')
tagname = input("Please enter your tag name :")
Text = input('Enter your text:')
HTML_Tag_maker(Tagname=tagname,Text=Text)
