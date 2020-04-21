<h1> Class Backend</h1>
<h3>This will be a class description for the backend that will allow for easy creation
of an interface between the frontend and the database stored remotely on Amazon Lightsail
server</h3>

<p>def __init__(self,filename,debug=false)</p>
<p>creates the connection with the object self and locates the filename for the
database</p>
<p>returns nothing</p>


<h2>User Interaction Functions</h2>
<p>add user(self,username,password)</p>
<p>returns Yes or no</p>
<p>delete user</p>
<p>sign in(username,password)</p> 
<p>sign out</p>


<h2>Server Interaction Functions</h2>
<p>upload file</p>
<p>download file</p>


<h2>__Private Class Funtions</h2>

<p>load</p>
<p>save</p>
<p>debug</p>
<p>connect</p>
<p>disconnect</p>
<p>select all from table</p>


<h5>Creation functions</h5>
<p>create database</p>
<p>create table</p>
<p>create row</p>


<h5>Deletion Functions</h5>
<p>delete database</p>
<p>delete table</p>
<p>delete column</p>
<p>delete row</p>

<h5>Security Checks</h5>
<p>Password Salting</p>
<p>File Checksums</p>
<p>Html Entities checking</p>
<p>Public Box Encyrption-Secure Data Transfer</p>
