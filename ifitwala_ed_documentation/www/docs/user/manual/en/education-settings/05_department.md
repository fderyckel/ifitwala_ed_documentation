<!-- add-breadcrumbs -->
# Department

**A Department is a team of educators that collaborate together around a discipline (the Arts dpt. or the Math dpt.) or around a category of students (the Learning Support dpt., the Middle School dpt.)**

A department can be linked to a particular section of your school but does not have to.  Usually each department has a lead.  The lead of the department has to be picked among one of the department members.  
Anyone employee can be part of a department. A person can be part of several departments.  They just have to be added in the department member list. 

To access the Academic Term doctype, go to:

> Home > School Settings > Department  

List View
 ![Department List View](/docs/assets/img/school-settings/department-listview.png)

Document View
![Department Document View](/docs/assets/img/school-settings/department-docview.png)


# 1. Before to fill in the department
It is preferable to fill in first the

* [The School](/docs/user/manual/en/education-settings/01_school) doctype
* [The Employee](/docs/user/manual/en/hr/01_employee.md) doctype


## 4. Validation rules and default behavior.
Here are some of the validation rules we have put in place to ensure the integrity of the data.

* unique name for department within the same school.  That means you can have 2 "Arts Dpt." but they have to be in 2 different school
* not twice the same department member in the child table

Other default behavior

* title is automatically created by concatenating the dpt. name and the school abbreviation
* filtering out department members already picked to not picked twice the same person.




{next}
