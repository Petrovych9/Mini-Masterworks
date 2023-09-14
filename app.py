import connectDB
import extraFunc
import infoByIP
import file


from flask import Flask, render_template, request, flash

# Create a Flask application instance:
app = Flask(__name__)                 #explanation:  When a Python script is executed directly, __name__ is set to '__main__'. When the script is imported as a module, __name__ is set to the module's name.
app.config['SECRET_KEY'] = 'hard to guess string'

# Create a route that will render the web form:
@app.route('/', methods=['POST',"GET"])
def index():
    return render_template('index.html')  #home page


@app.errorhandler(404)
def pageNotFound(error):
    return render_template('page404.html'), 404



# route that will indicate saving information:
@app.route('/bms', methods=['POST',"GET"])
def saveData():
    if request.method == "POST":
        name, author, pages, booktype, today = extraFunc.collectData()
        # format information to df
        data = extraFunc.createDf(name, author, pages, booktype, today)

        # saving to excel
        connectDB.saveToExcelDb(data)
        # saving to SQlite3 DB
        connectDB.saveToSqLite(['Bohdan', name, author, pages, booktype, today])
        flash('Data saved', category='success')
        return render_template('bms.html') #book managment system page
    else:
        return render_template('bms.html') #book managment system page


@app.route('/bms/allbooks', methods=['POST',"GET"])
def getAllbooks():
    query = "SELECT * FROM books"
    booksDB = connectDB.selectInSqlLite(query)
    print(booksDB)
    return render_template('allbooks.html', booksDB=connectDB.selectInSqlLite(query))


@app.route('/getAudio', methods=['POST',"GET"])
def getAudio():
    if request.method == "POST":
        url = request.form['url']
        audioPath = file.extractAudio(url)
    else:
        audioPath = 'AUDIO_2.mp3'
    return render_template('getAudio.html', audioPath=audioPath) #getAudio page


@app.route('/getLocationByIP', methods=['POST',"GET"])
def getLocationByIP():
    if request.method == "POST":
        ip = request.form['ipp']
        data = infoByIP.getData(ip)
        print(data)
        print(data['lat'],data['lon'])
        infoByIP.getLocation(data['lat'], data['lon'])
    else:
        data = 0
    return render_template('getLocationByIP.html', data=data) #getLocationByIP page


@app.route('/getLocationByIP/location', methods=['POST',"GET"])
def locationByIP():
    return render_template('location.html')

# Run the Application
if __name__ == '__main__':
    app.run(debug=True)


