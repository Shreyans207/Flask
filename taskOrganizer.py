from flask import Flask
from flask import jsonify,request

app =  Flask(__name__)

tasks_1 = [{
    'id' : 1,
    'title' : 'Rotational Motion',
    'description' : 'Lecture-1 , from 3:30 to 6 pm',
    'done' : False
}  , {
    'id' : 2,
    'title' : 'Give me a bath',
    'description' : 'from 5 to 8 pm',
    'done' : False
}]

@app.route('/add_task', methods = ['POST'])
def add_task() : 
    # request.json will contain the data that is to be posted on the webapp by fetching from the 
    if not request.json : 
        return jsonify({
            'status' : 'error' ,
            'message' : 'Please provide data' 
            })

    temp = {
    # -1 for the last element
    'id' : tasks_1[-1]['id'] + 1,
    'title' : request.json['title'],
    'description' : request.json['description'],
    'done' : False
    }

    tasks_1.append(temp)

    return jsonify({
        'status' : 'success',
        'message' : 'You are all set'
    })

@app.route('/get_data')
def display() :
    return jsonify({
        'data' : tasks_1
    }) 

if __name__ == '__main__' : 
    app.run(debug = True)

# {
    # "title": "Swimming",
    # "description": "Water park , from 8 to 11"
# }
