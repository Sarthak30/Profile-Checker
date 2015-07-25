import requests
x = raw_input('Enter the username : ')
print '1. Facebook'
print '2. Quora'
print '3. Codechef'
print '4. Codeforces'
print '5. Github'
print '6. Check for all'
choice = int(raw_input('For which website you want to search the username?(Input the number of website): '))
codeforce = 'http://codeforces.com/profile/'+x
codechef = 'http://www.codechef.com/users/'+x
facebook = 'http://www.facebook.com/'+x
quora = 'http://www.quora.com/'+x
github = 'http://github.com/'+x
if(choice == 1):
	r = requests.get(facebook)
	if (r.status_code==200):
		print 'Copy-paste url in web-browser'
		print facebook
	else:
		print 'Check the username'
		print 'It is not found'
elif(choice == 2):
	r = requests.get(quora)
	if (r.status_code==200):
		print 'Copy-paste url in web-browser'
		print quora
	else:
		print 'Check the username'
		print 'It is not found'
if(choice == 3):
	r = requests.get(codechef)
	if (r.status_code==200):
		print 'Copy-paste url in web-browser'
		print codechef
	else:
		print 'Check the username'
		print 'It is not found'
elif(choice == 4):
	r = requests.get(codeforce)
	if (r.status_code==200):
		print 'Copy-paste url in web-browser'
		print codeforce
	else:
		print 'Check the username'
		print 'It is not found'
elif(choice == 5):
	r = requests.get(github)
	if (r.status_code==200):
		print 'Copy-paste url in web-browser'
		print github
	else:
		print 'Check the username'
		print 'It is not found'
elif(choice == 6):
	r = requests.get(facebook)
	if (r.status_code==200):
		print 'Found for facebook'
		print 'Copy-paste url in web-browser'
		print facebook
	else:
		print 'It is not found on facebook'
	r = requests.get(quora)
	if (r.status_code==200):
		print 'Found for quora'
		print 'Copy-paste url in web-browser'
		print quora
	else:
		print 'It is not found on quora'
	r = requests.get(facebook)
	if (r.status_code==200):
		print 'Found for codechef'
		print 'Copy-paste url in web-browser'
		print codechef
	else:
		print 'It is not found on codechef'
	r = requests.get(facebook)
	if (r.status_code==200):
		print 'Found for codeforces'
		print 'Copy-paste url in web-browser'
		print codeforce
	else:
		print 'It is not found on codeforces'
	r = requests.get(facebook)
	if (r.status_code==200):
		print 'Found for github'
		print 'Copy-paste url in web-browser'
		print github
	else:
		print 'It is not found on github'
else:
	print 'Error 404!! Choice not available'
	
