from flask import Flask, render_template,request, url_for
import os.path

app = Flask(__name__)
@app.route('/',methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def counter():
    tom_value=0
    jerry_value=0
    final_tom=0
    final_jerry=0
    file_exists = os.path.isfile('/tmp/variable.txt')   
    if not (file_exists):
        with open("variable.txt","r") as fp:
            for i,line in enumerate(fp):
                if i==0:
                    tom_value = int(line.split(':')[1])
                if i==1:
                    jerry_value= int(line.split(':')[1])
        
        lines1=list()
        lines1.append('tom:{}\n'.format(tom_value))
        lines1.append('jerry:{}'.format(jerry_value))
        
        with open("/tmp/variable.txt", "w") as fp:
            for line in lines1:
                fp.write(line)

    with open("/tmp/variable.txt","r") as fp:    
        for i,line in enumerate(fp):
            if i==0:
                final_tom = int(line.split(':')[1])
            if i==1:
                final_jerry= int(line.split(':')[1])

    if request.method == 'POST':

        if request.form.get('tom') == 'ctom':
            final_tom+=1
        elif request.form.get('jerry') == 'cjerry':
            final_jerry+=1

        lines=[None]*2
        lines[0] ='tom:{}\n'.format(final_tom)
        lines[1]='jerry:{}'.format(final_jerry)

        with open("/tmp/variable.txt", "w") as fp:
            for line in lines:
                fp.write(line)

    return render_template('index.html', tom_count=final_tom,jerry_count=final_jerry)    

if __name__ == '__main__':
    app.run(debug=True)