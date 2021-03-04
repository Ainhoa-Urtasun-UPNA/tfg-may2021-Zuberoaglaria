from wordcloud import WordCloud
f = open(r'Wikipedia_economia.txt','r',encoding='utf-8',errors='ignore')
text_jobs = f.read()
graph = WordCloud(width = 3000, height = 2000, random_state=1, background_color='salmon', colormap='Pastel1', collocations=False).generate(text_jobs)
graph.to_file('graph.png')
