<!-- add-breadcrumbs -->
# School Calendar

The school calendar details the weekend and breaks that happen during a given academic year.  This will also compute the number of instructional days within an academic year.  
School calendar will be taken into consideration when taking attendance, or creating student leave request, or creating the courses schedule.

To access the School Calendar doctype, go to:

> Home > School Settings > School Calendar

List View
 ![School Calendar List View](/docs/assets/img/school-settings/school-calendar-listview1.png)

Document View
![School Calendar Document View](/docs/assets/img/school-settings/school-calendar-docview1.png)

![School Calendar Document View2](/docs/assets/img/school-settings/school-calendar-docview2.png)


## 1. Before to fill in the School Calendar
It is preferable to fill in first

* [The School](/docs/user/manual/en/education-settings/01_school) doctype
* [The Academic Year](/docs/user/manual/en/education-settings/02_academic-year) doctype
* [The Academic Term](/docs/user/manual/en/education-settings/02_academic-term) doctype

## 2. Fields to fill in the Calendar  

In Standard View.
![Academic Term Fields in standard view](/docs/assets/img/school-settings/academic-term-fields.png)

* *Academic Year*: a link to the Academic Year related to this school calendar.
* *Calendar Name*: the name to be given to the calendar.  For instance, you could give it the same name as your academic year to keep the naming simple.
* *School*: the school that this school calendar belong to.
* *Start of Break*: the first day of your school break - (you will repeat the process for each of your break during your school calendar year, even if the break is only one day long.)
* *End of Break*: the last day of your break.
* *Break Color*: Color for the calendar view. This can be set in the Education Setting document as default values.
* *Add to holidays*: to add these days to the holiday list.
* *Weekly Off*: most schools around the world have 2 days off per week.  This allows you to mark all the weekend / days off for the academic year.
* *Weekend Color*: Color for the calendar view. This can be set in the Education Setting document as default values.

## 3. Documents linked to School Calendar

* [Student Leave Application](/docs/user/manual/en/student/07_student-leave-application)
* [Student Attendance](/docs/user/manual/en/student/06_student-attendance)

## 4. Roles and permissions

The following roles have permissions on the Academic Term.
![Permissions for School Calendar](/docs/assets/img/school-settings/school-calendar-permission.png)

When the academic term is linked to a school, only the employees of that school (or its children) will have permission to read the DocType.

## 5. Awesomeness, validation rules and other default behaviors

* automatically compute the number of days within your academic year, the number of holidays and weekend and the number of instructional days.  
* automatically bring up a table with all the academic terms and their length (in days) as long as their belong the chosen academic year. 

Here are some of the validation rules we have put in place to ensure the integrity of the data.

* unique name for school calendar
* all breaks/weekend have to be within the academic year
*

{next}
