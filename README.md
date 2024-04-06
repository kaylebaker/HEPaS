# CSI3344 Distributed Systems
## Assignment 3: Distributed system project

**HEPaS** is a simple three-tier distributed system. The system has one client-side application, one or more server-side applications, and one database server which holds all OUST students’ course learning records.

- The client (application) is an interface that collects data from the user, performs preliminary pre-processing of the data items, and sends the data collected to the remote application/s at server-side.
- The server-side application uses the data received from the client to authenticate the user. After a successful authentication, the server-side application sends a request to the database server to get the user/student’s learning records. It then assesses whether the user meets Honors enrolment criteria therefore determining if the user is eligible for honors studies. The assessment result is then sent back to the client application.
- After the client application receives the data from the server, it finally displays the assessment results to the user.

## Project Description
Design and implement a version of the above-described HEPaS under some practical requirements.

## Implementation
Scripts written in Python using Pyro4 (https://pyro4.readthedocs.io/en/stable/#) library to allow them to talk to each other over a network.
Database built with SQLite.

## Client_Controller (client)
The client application allows a user to enter data for the Honors enrolment pre-assessment (HEPa). A user can be a (former or current) student at OUST, or anyone interested in enrolling an Honors course at OUST.
The client application first prompts the user to answer whether he/she is an OUST student. If the user is an OUST student (former or current), the client will ask the user to enter his/her Person ID (or Student ID, which can be e.g., an 8-digit number) and other information (e.g., first and last name, his/her OUST email address, etc.) to authenticate the user. The client then passes the data items entered to the server-side application/s to proceed the HEPa evaluation/assessment.
If the user is not an OUST student, the client requests the user to enter a Person ID and a sequence of unit scores (or marks e.g., in 'unit_code, mark pair'), one by one, through keyboard. The number of unit scores entered should be between 16 and 30, including “Fail” (e.g., a unit score below 50) marks and duplicate unit marks (if the student did the same unit multiple times).

## RMI_Controller.py (server-1)
Provides services/operations that process the data received from clients, calculate the averages, evaluate the eligibility based on evaluation criteria, and so on. The evaluation results are then returned to the client. If necessary, the server can send a service request to the database server, such as obtaining an OUST student’s course learning records, etc.

The basic operations on the server-1 include (but are not limited to):
- displaying individual scores (in 'unit_code, mark' pairs) on the screen in their input order;
- calculating the course average;
- selecting the best (or highest) 8 scores, and calculating the average of the best 8 scores;
- evaluating the eligibility according to the Honors evaluation criteria (see below); and finally,
- sending the evaluation result back to the client.

## DB_Controller.py (server-2)
Database server: it stores (former or current) OUST students’ course learning records (OSCLR), which may include student’s unit selection/learning history, related unit results, etc.
The student learning records in OSCLR database are read-only. HEPaS client cannot make any changes to student’s learning records in the OSCLR database.