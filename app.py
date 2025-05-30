from flask import Flask, render_template, request
import PyPDF2
import pandas as pd

app = Flask(__name__)

# ✅ CSV फाईल एकदाच लोड कर
df = pd.read_csv('phishing_model.csv', usecols=['url', 'type'], on_bad_lines='skip')


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/scam/", methods=['GET', 'POST'])
def detect_scam():
    if "file" not in request.files or request.files['file'].filename == '':
        return render_template("index.html", message="No file uploaded")

    file = request.files['file']
    extracted_text = ""

    if file.filename.endswith(".pdf"):
        try:
            pdf_reader = PyPDF2.PdfReader(file)
            extracted_text = " ".join([page.extract_text() for page in pdf_reader.pages if page.extract_text()])
        except Exception as e:
            return render_template("index.html", message=f"Failed to read PDF: {e}")
    elif file.filename.endswith('.txt'):
        try:
            extracted_text = file.read().decode("utf-8")
        except Exception as e:
            return render_template("index.html", message=f"Failed to read text file: {e}")
    else:
        return render_template("index.html", message="Unsupported file format. Upload a .pdf or .txt file.")

    print(extracted_text)  # Optional: for debugging

    return render_template("index.html", message="File processed successfully", text=extracted_text)

# ✅ URL Prediction route
@app.route("/predict", methods=["POST"])
def predict():
    url = request.form.get("url")
    if not url:
        return render_template("index.html", message="No URL provided")

    url = url.strip().lower()
    match = df[df['url'] == url]

    if not match.empty:
        prediction = match.iloc[0]['type']
    else:
        prediction = "Unknown"

    return render_template("index.html", input_url=url, predicted_class=prediction)

if __name__ == "__main__":
    app.run(debug=True)
