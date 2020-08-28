Description of Project

We are building an open source software repository site with download options with two
umbrella components, the user interaction platform and our data storage and management
system.
Python 3.8 will be our language of choice on this project. As of now flask will be our framework
that we are going to be building in. We’ve also discussed the idea of javascript and php being
used in conjunction with python on the web side to facilitate a higher quality user experience.

On a user level:

We are going to create a visual display for the data we have stored on our servers. This
is going to be a team effort to create an effective system that intuitively conveys important
information about the downloads available. A web framework like flask will be the heavy lifting
component of this piece as it takes care of the low level server interactions for us and our job is
to implement the logic required to collect our data.

On data storage and management level:

We initially will need to compile and organize a desired set of test data. Our site is going
to be designed to be file agnostic and as generally accepting of any user input. Our test data is
going to reflect and be a representative set.
Our set of data is going to need some storage method that has a set of interactive
methods associated.

We break this into 4 components that will function together as one.
1. Database schema design and implementation
2. Interaction with that database
3. The data preparation to be returned to the front end
4. And data security practices are implemented into the design to ensure data correctness
when served to the user.
