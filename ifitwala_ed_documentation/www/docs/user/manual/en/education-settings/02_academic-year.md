<!-- add-breadcrumbs -->
# Academic Year

**An academic year is a period of time that educational institutes uses to graduate students from one year to another.**

To access the academic year doctype, go to:

> Home > School Settings > Academic Year

An academic year comprises several academic terms.  Although start and end of academic year are not mandatory fields, we do strongly encourage to set up dates for these 2 fields to ensure the integrity of your data.  Many validation rules in other documents are based on these dates.  

List View
 ![Academic Year List View](/docs/assets/img/school-settings/academic-year-listview3.png)

Document View
![Academic Year Document View](/docs/assets/img/school-settings/academic-year-docview3.png)

If you set up the *current academic year* in the [education settings](/docs/user/manual/en/education-settings/education-settings) document, this will become the default academic year in new documents that are calling for that field.

## 1. Before to fill in the Academic Year
It is preferable to fill in first the

* [The School](/docs/user/manual/en/education-settings/01_school) doctype

## 2. Fields to fill in the Academic Year  

![Academic Year Fields in standard view](/docs/assets/img/school-settings/academic-year-fields-3.png)

Or in quick view.
![Academic Year Fields in quick view](/docs/assets/img/school-settings/academic-year-fields-2.png)

* *Academic Year Name*: How you want to call your academic year. You would choose something like 2020-2021, or 2020 (if in Southern Hemisphere countries).
* *Year Start Date*: the first day of your academic year.
* *Year End Date*: the last day of your academic year.
* *School*: Your school can have several sections such as Kindergarten, Primary Schools and Secondary Schools. The Academic year of each of these sections might not totally align.  

## 3. Documents linked to Academic Year

* [Academic Term](/docs/user/manual/en/education-settings/03_academic-term)
* [School Calendar](/docs/user/manual/en/education-settings/04_school-calendar)
* [Education Settings](/docs/user/manual/en/education-settings/education-settings)
* [Program Enrollment](/docs/user/manual/en/schedule/program-enrollment)
* [Student Group](/docs/user/manual/en/schedule/05_student-group)
* [Student Schedule](/docs/user/manual/en/schedule/07_course-schedule)
* [Student Log](/docs/user/manual/en/student/04_student-log)

## 4.  Roles and permissions

The following roles have permissions on the Academic Year.
![Permissions for Academic Year](/docs/assets/img/school-settings/academic-year-permission.png)

When the academic year is linked to a school, only the employees of that school (or its children) will have permission to read the DocType.

## 5. Awesomeness, validation rules and other default behaviors

* two all-day school events are created in the [School Event](/docs/user/manual/en/education-settings/07_school-event) Calendar.  One for the start of the academic year and one for its end. These events are public and will be visible to everyone belonging to that school.
![Academic Year School Event](/docs/assets/img/school-settings/academic-year-calendar.png)

Here are some of the validation rules we have put in place to ensure the integrity of the data.

* unique name for the academic year for a given school
* the start of the academic year cannot be after the end of the academic year (or vice-versa)

Other default behaviors

* title for academic year is automatically created by concatenating the name of the academic year and the abbreviation of the school.  

{next}
