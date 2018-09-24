#!c:/Python34/python.exe
 
print("Content-Type: text/html")

print("""
  """)
print('''
<html>
<head>
<style>
.form{  font-family:Arial, Helvetica, sans-serif;
        position: absolute;
	    right: 0;
	    width:40%;
	    margin: 20px;
	    max-width: 100px;
	    padding: 16px;
	    background-color: white;

}
font{
font-family:Arial, Helvetica, sans-serif;
color:993333;
font-size: 1.875em;
}
h4{
font-family:Arial, Helvetica, sans-serif;
color:993333;
font-size:200%;
}
input[type=numeric],select{
    width: 30%;
    padding: 15px;
    margin: 5px 0 22px 0;
    border: none;
    background:#ddd;
    font-family:Arial, Helvetica, sans-serif;
}
.btn {
    background-color:663333;
    color: white;
    padding: 16px 20px;
    border: none;
    cursor: pointer;
    width: 20%;
    opacity: 0.9;
    border-radius: 5px;
}

.btn:hover {
    opacity: 1;
}
</style>
</head>
<body>
<font>Please provide the following details for predicting the quantity of food you should make</font>
<form action=fetchpredict.py>
<label><b>Time slot:</b></label><br>
<select placeholder='timeslot' name='ts'>
<option value='0.0'>Morning time</option>
<option value='0.5'>evening time</option>
<option value='1'>Night time</option>
</select><br>
<label>Number of adults:</label><br>
<input type='numeric' placeholder='adult number' name='ano' required><br>
<label>Determine weather:</label><br>
<select placeholder='weather' name='wr'>
<option value='0'>Non favourable</option>
<option value='0.5'>Favourable</option>
<option value='1'>medium</option>
</select><br>
<label>Air conditioned hall?</label><br>
<select placeholder='A/C or not' name='ac'>
<option value='0.5'>Yes</option>
<option value='0'>No</option>
</select><br>
<label>Number of children:</label><br>
<input type='numeric' placeholder='children' name='cno' required><br>
<label>holiday day</label><br>
<select placeholder='holiday?' name='hd'>
<option value='0.5'>Yes</option>
<option value='0'>No</option>
</select><br>
<label>Variety of food</label><br>
<select placeholder='variety' name='var'>
<option value='0'>Low</option>
<option value='1'>Medium</option>
<option value='2'>High</option>
</select><br>
<button type="submit" class="btn">Predict</button>
</form>
</body>
</html>
''')  
 
    
