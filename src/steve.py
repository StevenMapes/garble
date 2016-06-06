from src.minify_jsmin import garble_js

js = "var img = new Image(1,1); img.src = 'http://mobi-force.com/wp-content/uploads/2015/04/Logo1.jpg'; document.getElementsByTagName('body')[0].appendChild(img); var img = new Image(1,1); img.src = 'http://mobi-force.com/wp-content/uploads/2015/04/Google-adwords-logo-1-222x150.jpg'; document.getElementsByTagName('body')[0].appendChild(img);"
print(garble_js(js))
