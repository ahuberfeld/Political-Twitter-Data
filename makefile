TweetsPerYear.pdf: tweetsPerYear.py supportOrOppose.pdf
	python3 tweetsPerYear.py
supportOrOppose.pdf: topPre.txt topPost.txt topTrump.txt oppositionChart.py healthcareTags.pdf
	python3 oppositionChart.py
healthcareTags.pdf: topPre.txt topPost.txt topTrump.txt healthcareChart.py
	python3 healthcareChart.py

healthcareChart.py: topPre.txt topPost.txt topTrump.txt
oppositionChart.py: topPre.txt topPost.txt topTrump.txt
tweetsPerYear.py: preTweets.csv postTweets.csv

topPre.txt: preTags.txt
	less preTags.txt |sort| uniq -c -i | sort -b -n -r | head -50 >topPre.txt
topPost.txt: postTags.txt
	less postTags.txt |sort| uniq -c -i | sort -b -n -r | head -50 >topPost.txt
topTrump.txt: trumpTags.txt
	less trumpTags.txt |sort| uniq -c -i | sort -b -n -r | head -50 >topTrump.txt

preTags.txt: preTweets.csv file2.py
	python3 file2.py

preTweets.csv: file1.py pol_tweets.csv
	python3 file1.py

postTweets.csv: file1.py pol_tweets.csv
	python3 file1.py


postTags.txt: postTweets.csv file2.py 
	python3 file2.py


trumpTags.txt: trumpTweets.txt file2.py
	python3 file2.py

