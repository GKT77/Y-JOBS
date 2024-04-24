from flask import Flask, render_template, request, redirect, jsonify
app =  Flask (__name__)
JOBS = [
  {
    'id' : 1,
    'title' : 'Data Analyst',
     'location' : 'Toronto, Canda',
    'salary': 'CAD $100,000'
  },
  {
    'id' : 2,
    'title' : 'Java Developer',
     'location' : 'Calgary, Canda',
    'salary': 'CAD $110,000'
  },
{
  'id' : 3,
  'title' : 'DevOps Engineer',
   'location' : 'Remote',
 
},
{
  'id' : 4,
  'title' : 'Test automation Engineer',
   'location' : 'Toronto, Canda',
  'salary': 'CAD $95,000'
},
{
  'id' : 5,
  'title' : 'Test Engineer',
   'location' : 'Vancouer, Canda',
  'salary': 'CAD $100,000'
},
{
  'id' : 6,
  'title' : 'Salesforce Developer',
   'location' : 'Toronto, Canda',
  'salary': 'CAD $115,000'
},
  {
    'id' : 7,
    'title' : 'Front end Developer',
     'location' : 'Montreal, Canda',
    'salary': 'CAD $120,000'
  }
]
@app.route("/")
def hello_Y():
  return render_template('home.html', jobs=JOBS, company_name='Y')

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)