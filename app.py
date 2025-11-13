from flask import Flask, render_template

app = Flask(__name__)

# ✅ الصفحة الرئيسية
@app.route('/')
def index():
    return render_template('index.html')

# ✅ صفحة المعرض
@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')

# ✅ صفحة الخدمات
@app.route('/services')
def services():
    return render_template('services.html')

# ✅ صفحة من أنا
@app.route('/about')
def about():
    return render_template('about.html')

# ✅ صفحة التواصل
@app.route('/contact')
def contact():
    return render_template('contact.html')

# ✅ صفحة الأسعار
@app.route('/pricing')
def pricing():
    return render_template('pricing.html')

# ✅ صفحة المدونة
@app.route('/blog')
def blog():
    return render_template('blog.html')

# ✅ تشغيل التطبيق
if __name__ == '__main__':
    app.run(debug=True)
