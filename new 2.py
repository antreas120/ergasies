def peristrofi(Stoixia):
	pinakasPer = [[""]*8 for _ in range(8)]
	for graper in range(8):
		for row in range(8):
			pinakasPer[graper][row] = Stoixia[row][graper];
	return pinakasPer;
txt = open("Sample.txt","r");
Stoixia = [[""]*8 for _ in range(8)]
for row in range(8):
	metavliti = "";
for column in range(8):
	if(column==7):
	    metavliti =(Stoixia[row][column]) +metavliti ;
	elif(column!=7):
		metavliti =metavliti + (Stoixia[row][column]) + "0";
	print metavliti
gramm = txt.readlines();
rows=0;
columns=0;
for gram in gramm:
	Stix = gram.split("");
	timi = "";
	for sti in Stix:
		timi =timi + sti;
		Stoixia[rows][columns] = timi;
		columns = columns + 1;
	rows = rows + 1;
	columns = 0;
print("peristrofi 1");
e1 = peristrofi(Stoixia);
print("peristrofi 2");
e2 = peristrofi(e1);
print("peristrofi 3");
e3 = peristrofi(e2);






