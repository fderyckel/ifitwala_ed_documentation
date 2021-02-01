<!-- add-breadcrumbs -->
# Department

**A Department is a team of educators that collaborate together around a discipline (the Arts dpt. or the Math dpt.) or around a category of students (the Learning Support dpt., the Middle School dpt.)**

To access the Department doctype, go to:

> Home > School Settings > Department     

A department can be linked to a particular section of your school but does not have to.  Academic departments tend to be linked to a particular section of the school; for instance, an Arts dpt. in primary and an Arts dpt. in secondary school, some other departments tend to be across sections; for instance Learning Support or Gifted and Talented. Any employee can be part of a department. Also, as it is often the cases in schools, a person can be part of several departments.  They just have to be added in the department member list. This doctype allows you to reflect the organizational structure of your school.

Usually each department has a lead.  The lead of the department has to be picked among one of the department members.  

Sometimes, department can have their own philosophy on how to approach their subject.

List view
![Department list view](/docs/assets/img/school-settings/department-listview.png)

Doc View
![Department Doc view](/docs/assets/img/school-settings/department-docview.png)

# 1. Before to fill in the department
It is preferable to fill in first the

* [The School](/docs/user/manual/en/education-settings/01_school) doctype
* [The Employee](/docs/user/manual/en/hr/01_employee.md) doctype

# 2. Fields to fill in the Department doctype

In Standard View (blank).
![Department Fields in standard view](/docs/assets/img/school-settings/department-empty-docview.png)

* *Department Name*: to set up the name of the department.
* *School*: to set up which school does this department belong to.
* *Department Lead*: to set up who is leading that department.
* *Enabled*: by default, this box is checked.  Uncheck the box if the department is not active anymore in your school.
* *Department Members* (child table): to add the department members.  Just the employee link is necessary.
* *Philosophy*: to write down your dpt. philosophy (in case you have one)


# 3. Documents linked to the the department

* [Meeting](/docs/user/manual/en/education-settings/06_collaboration)
* [Course](/docs/user/manual/en/schedule/01_course)

## 4. Awesomeness, validation rules and other default behaviors

Once your department is set with its members, you can now update the Email Group List (email of all members in the department). And you can start writing elaborate emails or newsletter to your own team.  You can also access directly the meeting page.

![Quick access to other resources](/docs/assets/img/school-settings/department-email-group.png)

Here are some of the validation rules we have put in place to ensure the integrity of the data.

* unique name for department within the same school.  That means you can have 2 "Arts Dpt." but they have to be in 2 different school
* not twice the same department member in the child table

Other default behavior

* title is automatically created by concatenating the dpt. name and the school abbreviation
* filtering out department members already picked to not picked twice the same person.



{next}
