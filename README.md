# Student-Course-Feedback-Evaluation
An Unsupervised Learning Problem

**Problem Statement -**
Students has attended the multiple courses. At the end students provided the feedback on the course, instructor by answer the 30 Question. Given the feedback as a dataset, we have analysed the data using various Clustering Techiques.

About Dataset-This dataset is based on an evaluation form filled out by students for different courses. It has different attributes including attendance, difficulty, score for each evaluation question, among others.The dataset has 5820 rows and 33 columns.

Description-

COLUMN NAME   |        DESCRIPTION                                                                                         | VALUES

instr         Instructor’s identifier                                                                                      {1,2,3}

class         Course code                                                                                                  {1-13}

nb.repeat     Number of times the student is taking this course                                                            {1,2,3}

attendance    Code of the level of attendance                                                                              {0,1,2,3}

difficulty    Level of the difficulty of the course                                                                        {1,2,3,4,5}

Q1            The semester course content, teaching method and evaluation system were provided at the start.               {1,2,3,4,5}

Q2            The course aims and objectives were clearly stated at the beginning of the period.                           {1,2,3,4,5}

Q3            The course was worth the amount of credit assigned to it.                                                    {1,2,3,4,5}

Q4            The course was taught according to the syllabus announced on the first day of class.                         {1,2,3,4,5}

Q5            The class discussions, homework assignments, applications and studies were satisfactory.                     {1,2,3,4,5}

Q6            The textbook and other courses resources were sufficient and up to date.                                     {1,2,3,4,5}

Q7            The course allowed field work, applications, laboratory,discussion and other studies.                        {1,2,3,4,5}

Q8            The quizzes, assignments, projects and exams contributed to helping and learning.                            {1,2,3,4,5}

Q9            I greatly enjoyed the class and was eager to actively participate during the lectures.                       {1,2,3,4,5}

Q10           My initial expectations about the course were met at the end of the period or year.                          {1,2,3,4,5}

Q11           The course was relevant and beneficial to my professional development.                                       {1,2,3,4,5}

Q12           The course helped me look at life and the world with a new perspective.                                      {1,2,3,4,5}

Q13           The instructor’s knowledge was relevant and up to date.                                                      {1,2,3,4,5}

Q14           The instructor came prepared for classes.                                                                    {1,2,3,4,5}

Q15           The instructor taught in accordance with the announced lesson plan.                                          {1,2,3,4,5}

Q16           The instructor was committed to the course and was understandable.                                           {1,2,3,4,5}

Q17           The instructor arrived on time for classes.                                                                  {1,2,3,4,5}

Q18           The instructor has a smooth and easy to follow delivery/speech.                                              {1,2,3,4,5}

Q19           The instructor made effective use of class hours.                                                            {1,2,3,4,5}

Q20           The instructor explained the course and was eager to be helpful to students.                                 {1,2,3,4,5}

Q21           The instructor demonstrated a positive approach to students.                                                 {1,2,3,4,5}

Q22           The instructor was open and respectful of the views of students about the course.                            {1,2,3,4,5}

Q23           The instructor encouraged participation in the course.                                                       {1,2,3,4,5}

Q24           The instructor gave relevant homework assignments/projects, and helped/guided students.                      {1,2,3,4,5}

Q25           The instructor responded to questions about the course inside and outside of the course.                     {1,2,3,4,5}

Q26           The instructor’s evaluation system (midterm and final questions, projects, assignments, etc.) effectively measured the course objectives.                                 {1,2,3,4,5}
              
Q27           The instructor provided solutions to exams and discussed them with students.                                 {1,2,3,4,5}

Q28           The instructor treated all students in a right and objective manner.                                         {1,2,3,4,5}
