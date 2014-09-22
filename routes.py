from flask import Flask, render_template, request
import frequency_analysis
import lexical_diversity
import fb_popularity
import cik

app=Flask(__name__)

@app.route('/')
def home():
	return render_template('home.html')
	
@app.route('/twitter')
def twter():
	return render_template('twitter.html')
	
@app.route('/process', methods=['POST'])
def process():
	kwargs = {}
	hashtag = request.form['hashtag']
	kwargs['result']= frequency_analysis.freq(hashtag)
	return render_template('results.html',**kwargs)
	
@app.route('/lexical_diversity')	
def lex_div():
	return render_template('lexical_diversity.html')
	
@app.route('/l_process', methods=['POST'])
def l_process():
	kwargs = {}
	hashtag = request.form['hashtag']
	words, screen_names, hashtags, status_texts=lexical_diversity.lex(hashtag)
	kwargs['lexd_words']= lexical_diversity.lexical_diversity(words)
	kwargs['lexd_screen_names']= lexical_diversity.lexical_diversity(screen_names)
	kwargs['lexd_hashtags']= lexical_diversity.lexical_diversity(hashtags)
	kwargs['lexd_status_texts']= lexical_diversity.average_words(status_texts)
	return render_template('ld_results.html',**kwargs)
	
@app.route('/facebook')
def fbook():
	return render_template('facebook.html')	

@app.route('/popular', methods = ['POST'])
def popular():
	kwargs = {}
	hashtag1 = request.form["hashtag"]
	hashtag2 = request.form["hashtag2"]
	#kwargs['popu']= fb_popularity.popularity(hashtag1,hashtag2)
	kwargs['comp']= fb_popularity.compare(hashtag1,hashtag2)
	return render_template('fb_pop.html', **kwargs)
	
@app.route('/linkedin')
def lnkdin():
	return render_template('linkedin.html')

@app.route('/about')
def about():
	return render_template('about.html')
	
@app.route('/developer')
def developer():
	return render_template('developer.html')

@app.route('/mutual_funds')
def projs():
	return render_template('mutual.html')
	
@app.route('/mutual_results',methods = ['POST'])
def proj_res():
	list1=[]
	kwargs = {}
	ciknum= request.form["cik_number"]
	link = cik.getLatestFiling(ciknum)
	if link!="No filing found, please try a different CIK number.":
		filingLink = cik.getFilingTextFile(link)
		iterator =  cik.getHoldings(filingLink)
		for x in iterator:
			list1.append(x)
		kwargs['ans']=list1
		
	return render_template('cik_results.html', **kwargs)

	
if __name__ =="__main__":
	app.run(debug='True',port=8080)