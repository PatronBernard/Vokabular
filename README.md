<h1>QT Application to Practice Translations</h1>

<h3>Requirements:</h3>   
<ul><li>Python 3 or higher  
<li>openpyxl  
<li>PyQt4</li></ul>
  
<h3>Usage: </h3>    
```>python Vertaal_OefeningQT.py <excel file with words and translations.xlsx>```  
For example:  
```>python Vertaal_OefeningQT.py testopgave.xlsx```  

<p>Note that the xlsx file should be UTF-8 encoded and contain only two columns. 
The first column contains the word that has to be translated, the second one the solution.
So far it appears to work with multiple words and commas, although this requires more testing. 
Word comparison is case-insensitive. 
</p>


<h3>Improvements that might get implemented:  </h3>   
<ul><li>Words that you get wrong will occur more often  </li>
<li>Multiple tries/hints </li> 
<li>Save sessions  </li>
<li>ban/unban words  </li></ul>

<h3> Version History </h3>
<h4>v1.0 (27/09/2014)</h4> 
<ul><li>Added: basic functionality</li></ul>