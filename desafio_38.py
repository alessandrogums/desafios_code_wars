def format_duration(seconds):
	 

	if seconds == 0 :
		return 'now'
	else:
		year = seconds // 31536000
		days = (seconds %31536000) // 86400
		hours = (seconds % 86400) // 3600
		minutes = (seconds % 3600) // 60
		secondss = (seconds % 60)

		dici_dates = {'year':year, 'day':days , 'hour':hours, 'minute':minutes,'second':secondss}
		dici_clr = {x:y for x,y in dici_dates.items() if y>0}

		penult, c = None, 0  
	
		if len(dici_clr) > 1 : 
			penult=len(dici_clr) - 2


		str_conc=''

		for k,v in dici_clr.items():
			 
			

			if v == 1:
			
				if c == penult:
					str_conc+=str(v) +' '+ k +' and '
				else:
					str_conc+=str(v) +' ' + k +', '
			else:
				
				if c == penult:
					str_conc+=str(v) +' ' + k +'s'+' and '
				else:
					str_conc+=str(v) +' ' + k +'s'+ ', '

			c+=1
			
		return str_conc[:-2]
