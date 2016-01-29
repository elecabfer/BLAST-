inp=open('blastx_glimmer_ncbi_tce1_n3_b80.xls', 'r')
inp2=inp.read()
spl=inp2.split('# Query:')
headers=open('headers_ncbi_DB.txt','r').read()
intergenic=open('blastx_glimmer_annotated.xls','w') #no es intergenic, pero asi  se llama la variable ;)
orfs=open('genes_glimmer_TCE1.fasta','r').read()
##########################orfs, que no siguen bien el orden
orfs=orfs.split('>')
print len(orfs)
#####################headers
headers= headers.split('>')
#########################BLAST hits
for a in range(0, len(spl)): #por cada enrtada del blast, que tiene mal el numero
    positive='no'
    if '# 0 hits found' not in spl[a]:
        tabs=spl[a].split('\t')
        if len(tabs) > 12:
            tabs=tabs[:12]
        elif len(tabs)>10:
            ref=tabs[1] #ref es el id del blast
            evalue=float(tabs[10])
            qstart=tabs[6]
            qend=tabs[7]
            lenght=int(tabs[3])
            if lenght > 1 and evalue < 10:
                for h in headers:
                        if ref in h:
                                positive='si'
                                intergenic.write(h[:-1]+'\t'+str(qstart)+'\t'+str(qend)+'\t'+str(evalue)+'\t'+orfs[a][1:orfs[a].find('\n')]+'\n')
                                #break
                if positive=='no': #si la secuencia no esta 
                        intergenic.write(str(tabs[1])+'\t'+str(qstart)+'\t'+str(qend)+'\t'+str(evalue)+'\t'+orfs[a][1:orfs[a].find('\n')]+'\n')
print 'fini'
