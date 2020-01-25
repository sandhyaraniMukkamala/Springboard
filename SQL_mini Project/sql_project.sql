/*In the mini project, you'll be asked a series of questions. You can
solve them using the platform, but for the final deliverable,
paste the code for each solution into this script, and upload it
to your GitHub.

Before starting with the questions, feel free to take your time,
exploring the data, and getting acquainted with the 3 tables. */



/* Q1: Some of the facilities charge a fee to members, but some do not.
Please list the names of the facilities that do. */

SELECT * FROM `Facilities` WHERE membercost != '0.0'


/* Q2: How many facilities do not charge a fee to members? */

SELECT COUNT(*) FROM `Facilities` WHERE membercost = '0.0'

/* Q3: How can you produce a list of facilities that charge a fee to members,
where the fee is less than 20% of the facility's monthly maintenance cost?
Return the facid, facility name, member cost, and monthly maintenance of the
facilities in question. */

SELECT facid, name, membercost, monthlymaintenance FROM `Facilities` WHERE membercost < (monthlymaintenance * 20.0 / 100.0) and membercost != '0.0'

/* Q4: How can you retrieve the details of facilities with ID 1 and 5?
Write the query without using the OR operator. */

SELECT * FROM `Facilities` WHERE facid IN (1, 5)

/* Q5: How can you produce a list of facilities, with each labelled as
'cheap' or 'expensive', depending on if their monthly maintenance cost is
more than $100? Return the name and monthly maintenance of the facilities
in question. */

SELECT name, monthlymaintenance, CASE WHEN monthlymaintenance <100.0 THEN 'Cheap' ELSE 'Expensive' END AS fac_type FROM `Facilities`

/* Q6: You'd like to get the first and last name of the last member(s)
who signed up. Do not use the LIMIT clause for your solution. */

SELECT firstname, surname FROM `Members` WHERE memid = (SELECT max(memid) FROM Members) 

/* Q7: How can you produce a list of all members who have used a tennis court?
Include in your output the name of the court, and the name of the member
formatted as a single column. Ensure no duplicate data, and order by
the member name. */

SELECT DISTINCT CONCAT(m.firstname, ' ', m.surname) AS member_name, f.name FROM Bookings b JOIN Facilities f on b.facid = f.facid JOIN Members m on b.memid = m.memid WHERE b.facid in (0, 1) ORDER BY 1

/* Q8: How can you produce a list of bookings on the day of 2012-09-14 which
will cost the member (or guest) more than $30? Remember that guests have
different costs to members (the listed costs are per half-hour 'slot'), and
the guest user's ID is always 0. Include in your output the name of the
facility, the name of the member formatted as a single column, and the cost.
Order by descending cost, and do not use any subqueries. */

SELECT DISTINCT CONCAT(m.firstname, ' ', m.surname) AS member_name, f.name, f.membercost * b.slots as cost, b.starttime FROM Bookings b JOIN Facilities f ON b.facid = b.facid JOIN Members m ON b.memid = m.memid WHERE date(b.starttime) = '2012-09-14' and b.memid > 0 and f.membercost * b.slots > 30 UNION SELECT DISTINCT CONCAT(m.firstname, ' ', m.surname) AS member_name, f.name, f.guestcost * b.slots as cost, b.starttime FROM Bookings b JOIN Facilities f on b.facid = f.facid JOIN Members m on b.memid = m.memid WHERE date(starttime) = '2012-09-14' and b.memid = 0 and f.guestcost * b.slots > 30 ORDER BY 3 DESC
/* Q9: This time, produce the same result as in Q8, but using a subquery. */

SELECT * FROM (SELECT DISTINCT CONCAT(m.firstname, ' ', m.surname) AS member_name, f.name, f.membercost * b.slots as cost, b.starttime FROM Bookings b JOIN Facilities f ON b.facid = b.facid JOIN Members m ON b.memid = m.memid WHERE date(b.starttime) = '2012-09-14' and b.memid > 0 and f.membercost * b.slots > 30 UNION SELECT DISTINCT CONCAT(m.firstname, ' ', m.surname) AS member_name, f.name, f.guestcost * b.slots as cost, b.starttime FROM Bookings b JOIN Facilities f on b.facid = f.facid JOIN Members m on b.memid = m.memid WHERE date(starttime) = '2012-09-14' and b.memid = 0 and f.guestcost * b.slots > 30) sub order by 3 DESC

/* Q10: Produce a list of facilities with a total revenue less than 1000.
The output of facility name and total revenue, sorted by revenue. Remember
that there's a different cost for guests and members! */

SELECT * FROM (SELECT name, sum(revenue) total_revenue from (SELECT f.name, f.membercost * b.slots as revenue, b.starttime from Bookings b JOIN Facilities f on b.facid = f.facid WHERE b.memid > 0 UNION SELECT f.name, f.guestcost * b.slots as revenue, b.starttime FROM Bookings b JOIN Facilities f ON b.facid = f.facid WHERE b.memid = 0) sub GROUP BY name) sub1 WHERE total_revenue < 1000 ORDER BY 2