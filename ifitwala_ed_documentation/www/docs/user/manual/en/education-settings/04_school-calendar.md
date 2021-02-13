<!-- add-breadcrumbs -->
# School Calendar

The school calendar details the weekend and breaks that happen during a given academic year.  This will also compute the number of instructional days within an academic year.

To access the School Calendar doctype, go to:

> Home > School Settings > School Calendar

List View
 ![School Calendar List View](/docs/assets/img/school-settings/academic-term-listview.png)

Document View
![School Calendar Document View](/docs/assets/img/school-settings/academic-term-docview.png)


## 1. Before to fill in the School Calendar
It is preferable to fill in first

* [The School](/docs/user/manual/en/education-settings/01_school) doctype
* [The Academic Year](/docs/user/manual/en/education-settings/02_academic-year) doctype

## 2. Fields to fill in the Calendar  

In Standard View.
![Academic Term Fields in standard view](/docs/assets/img/school-settings/academic-term-fields.png)

* *Academic Year*: a link to the Academic Year related to this school calendar.
* *Term Name*: the name to be given to the term.  For instance if you are having semesters as terms, you would call it S1 or S2.  If you are having quarters as terms, you could call it Q1 or Q2, etc.  You could also create a year long term for course that are year long.  
* *Term Start Date*: the first day of your academic term.
* *Term End Date*: the last day of your academic term.

## 3. Documents linked to Academic Term

* [Student Leave Application](/docs/user/manual/en/education-settings/education-settings)
* [Student Attendance](/docs/user/manual/en/schedule/program-enrollment) 

## 4.  Roles and permissions

The following roles have permissions on the Academic Term.
![Permissions for Academic Term](/docs/assets/img/school-settings/academic-term-permission.png)

When the academic term is linked to a school, only the employees of that school (or its children) will have permission to read the DocType.

## 5. Awesomeness, validation rules and other default behaviors

* two all-day school events are created in the [School Event](/docs/user/manual/en/education-settings/07_school-event) Calendar.  One for the start of the academic term and one for its end. These events are public and will be visible to everyone belonging to that school.
![Academic Term School Event](/docs/assets/img/school-settings/academic-term-calendar.png)

Here are some of the validation rules we have put in place to ensure the integrity of the data.

* unique name for academic term
* the start of the academic term cannot be after the end of the academic term (or vice-versa)
* an academic term has to be within its academic year.

{next}
