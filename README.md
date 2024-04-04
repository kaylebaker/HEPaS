CSI3344 Distributed Systems
Assignment 3: Distributed system project & video demo

HEPaS is a simple three-tier distributed system. The system has one client-side application, one or more server-side applications, and one database server which holds all OUST students’ course learning records.

• The client (application) is an interface that collects data from the user, performs preliminary pre-processing of the data items, and sends the data collected to the remote application/s at server-side.
• The server-side application uses the data received from the client to authenticate the user. After a successful authentication, the server-side application sends a request to the database server to get the user/student’s learning records. It then assesses whether the user meets Honors enrolment criteria therefore determining if the user is eligible for honors studies. The assessment result is then sent back to the client application.

• After the client application receives the data from the server, it finally displays the assessment results to the user.

In this project, you are requested to design and implement a version of the above-described HEPaS under some practical requirements.