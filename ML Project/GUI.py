from flask import *
import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.neural_network import MLPClassifier

app = Flask(__name__)

def train_test():
    d1= pd.read_csv('data.csv')
    enc=LabelEncoder()
    for i in (2,3,4,5,6,7,16,26):
        d1.iloc[:,i]= enc.fit_transform(d1.iloc[:,i])
    d1.drop(['EmpNumber'],inplace=True, axis=1)
    Y= d1.PerformanceRating
    X= d1.iloc[:,[4,5,9,16,20,21,22,23,24]]
    X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.2, random_state=10)
    sc= StandardScaler()
    X_train= sc.fit_transform(X_train)
    X_test= sc.transform(X_test)
    return X_train,Y_train,X_test,Y_test

@app.route('/algorithms_dropdown', methods=['GET', 'POST'])
def algorithms_dropdown():
    X_train,Y_train,X_test,Y_test=train_test()

    report_table=None
    select = request.form.get('comp_select')
    if select=="Decision tree":
        report_table= decision_tree(X_train,Y_train,X_test,Y_test)[0]
    elif select=="Neural network":
        report_table= neural_network(X_train,Y_train,X_test,Y_test)[0]
    if select=="Support vector":
        report_table= support_vector(X_train,Y_train,X_test,Y_test)[0]
    return render_template('display_algo.html',  tables=[report_table.to_html(classes='data')], titles=report_table.columns.values)



def decision_tree(X_train,Y_train,X_test,Y_test):  
    classifier_dtg= DecisionTreeClassifier(random_state=43, splitter='best')
    parameters=[{'min_samples_split':[2,3,4,5],'criterion':['gini']},{'min_samples_leaf':[2,3,4,5],'criterion':['entropy']}]
    model_gridtree=GridSearchCV(estimator=classifier_dtg, param_grid=parameters, scoring='accuracy', cv=10)
    model_gridtree.fit(X_train,Y_train)
    Y_Predict_dtree= model_gridtree.predict(X_test)
    report=(classification_report(Y_test, Y_Predict_dtree,output_dict=True))
    report_table=pd.DataFrame(report).transpose()
    accuracy=accuracy_score(Y_test, Y_Predict_dtree)

    return [report_table,accuracy]

def support_vector(X_train,Y_train,X_test,Y_test):
    rbf_svc = SVC(kernel='rbf', C=100, random_state=10).fit(X_train,Y_train)
    Y_predict_svm = rbf_svc.predict(X_test)
    report=(classification_report(Y_test,Y_predict_svm,output_dict=True))
    report_table=pd.DataFrame(report).transpose()
    accuracy=accuracy_score(Y_test,Y_predict_svm)
    return [report_table,accuracy]

def neural_network(X_train,Y_train,X_test,Y_test):
    model_mlp = MLPClassifier(hidden_layer_sizes=(100,100,100),batch_size=10,learning_rate_init=0.01,max_iter=2000,random_state=10)
    model_mlp.fit(X_train,Y_train)
    Y_predict_mlp = model_mlp.predict(X_test)
    report=(classification_report(Y_test,Y_predict_mlp,output_dict=True))
    report_table=pd.DataFrame(report).transpose()
    accuracy=accuracy_score(Y_test,Y_predict_mlp)

    return [report_table,accuracy]

@app.route('/dataset.html')
def dataset():  
    return render_template('dataset.html'); 

@app.route('/algorithms.html')
def algorithms():
    algorithms=['Decision tree','Neural network','Support vector']
    return render_template('algorithms.html',algorithms=algorithms); 

@app.route('/accuracy.html')
def accuracy():
    X_train,Y_train,X_test,Y_test=train_test()
    deci=decision_tree(X_train,Y_train,X_test,Y_test)[1]
    neut=neural_network(X_train,Y_train,X_test,Y_test)[1]
    sup=support_vector(X_train,Y_train,X_test,Y_test)[1]

    accuracies={'Decision tree: ':deci,'Neural network: ':neut,'Support vector: ':sup}
    return render_template('accuracy.html',accuracies=accuracies)

@app.route('/features.html')
def features():  
    return render_template('features.html'); 

@app.route('/')
def home():  
    return render_template('website.html'); 

if __name__ =="__main__":  
    app.run(debug=True)  
