import re
import csv
import subprocess
##pdf is name of the pdf out is outfile name opts as of now ive only done 2
def pdf2txt(pdf,txt,**opts):
    cmd=['pdftotext']
    if not opts.get('layoput')==False:
        cmd.append('-layout')
    if not opts.get('nopgbrk')==False:
        cmd.append('-nopgbrk')
  ##there are a bunch more options nopgbrk and layout are the 2 i use and they are default true
    cmd.append(pdf)
    cmd.append(txt)
    subprocess.call(cmd)
    return txt
##txt is the text file out put from pdf2txt nocopy is a list of lines to not copy from the txt file include
##['',' '] to include blank lines out is the out csv fieldlst is a list or tulip containing the feilds 
##in order from right to left outfile is csv file portble format
def simptbl(txt, nocopy, out, fieldlst):
    lnlst=[]
    with open(txt, 'r')as tf:
        for ln in tf.readlines():
            rlst=[]
            ln=str(ln)
            if not ln in nocopy:    
                rlst=[]
                row=ln.split('  ')
                for wrd in row:
                    if not wrd=='':
                      rlst.append(wrd)
                if len(rlst)>0:
                    lnlst.append(rlst)
    dictlst=[]            
    for r in lnlst:
        if len(r)==len(fieldlst):
            rdict=dict.fromkeys(fieldlst)
            for i, field in enumerate(fieldlst):
                n=i-1
                rdict.update({field:r[n]})
            dictlst.append(rdict)
        else:
            with open('.err.log', 'a') as log:
                errlst=['ERROR WHITH LINE \n',' '.join(r)]
                err=''.join(errlst)
                log.write(err)
    with open(out, 'w')as ouf:        
        wo=csv.DictWriter(ouf, fieldlst)
        wo.writeheader()
        wo.writerows(dictlst)
                               
                
                