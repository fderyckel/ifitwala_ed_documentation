<!-- add-breadcrumbs -->
# Academic Term

**An academic year is usually punctuated by several terms.  Depending of the school culture, these terms can be semesters, quarters, etc.**

To access the Academic Term doctype, go to:

> Home > School Settings > Academic Term

Usually, holidays are separating 2 academic terms.  Although start and end of academic term are not mandatory fields, we do strongly encourage to set up dates for these 2 fields to ensure the integrity of your data.  Many validation rules in other documents are based on these dates.  

List View
 ![Academic Term List View](/docs/assets/img/school-settings/academic-term-listview.png)

Document View
![Academic Term Document View](/docs/assets/img/school-settings/academic-term-docview.png)

If you set up the *current academic term* in the [education settings](/docs/user/manual/en/education-settings/education-settings) document, this will become the default academic term in new documents that are calling for that field.

## 1. Before to fill in the Academic Term
It is preferable to fill in first the

* [The School](/docs/user/manual/en/education-settings/01_school) doctype
* [The Academic Year](/docs/user/manual/en/education-settings/02_academic-year) doctype

## 2. Fields to fill in the Academic Term  

![Academic Term Fields in standard view](/docs/assets/img/school-settings/academic-term-fields.png)

Or in quick view.
![Academic Term Fields in quick view](/docs/assets/img/school-settings/academic-term-fields-2.png)

* *Academic Year*: a link to the Academic Year that this term belong to
* *Term Name*: the name to be given to the term.  For instance if you are having semesters as terms, you would call it S1 or S2.  If you are having quarters as terms, you could call it Q1 or Q2, etc.  You could also create a year long term for course that are year long.  
* *Term Start Date*: the first day of your academic term
* *Term End Date*: the last day of your academic term.

## 3. Documents linked to Academic Year

* [Education Settings](/docs/user/manual/en/education-settings/education-settings)
* [Program Enrollment](/docs/user/manual/en/schedule/program-enrollment)
* [Student Log](/docs/user/manual/en/student/student-log)

## 4. Validation rules
Here are some of the validation rules we have put in place to ensure the integrity of the data.

* unique name for academic term
* the start of the academic term cannot be after the end of the academic term (or vice-versa)
* an academic term has to be within its academic year.


{next}
