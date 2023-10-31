#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>

#define ERR_ARRAY_OVERFLOW 1
#define  ERR_INPUT_ERROR 2
#define ERR_EMPTY_ARRAY 3

typedef struct student 
{
    char last_name[16];
    int mark;
}student_t;

void print_one_student(const student_t *const students)
{
    printf("%s", students->last_name);
    printf("%d\n", students->mark);
}

void print_students(const student_t *const students, int students_size)
{
    for (int i = 0; i < students_size; i++)
        print_one_student(&students[i]);
}

int init_students(student_t *const students,  
int *const students_size)
{ 
    student_t student;

    int i = 0;
    while (i < 6)
    {
        fgets(student.last_name, sizeof(student.last_name), stdin);
        char space;
        if (scanf("%d%c", &(student.mark), &space) != 2)
        {
            puts("Input error");
            return ERR_INPUT_ERROR;
        }
        if (!strcmp(student.last_name, "STOP\n"))
            return EXIT_SUCCESS;

        if (i >= 5)
        {
            printf("Array overflow\n");
            return ERR_ARRAY_OVERFLOW;
        }
        (*students_size)++;

        students[i] = student;
        i++;
    }
    return EXIT_SUCCESS;
}

void delete_student(student_t *const students, int *const students_size, const int number)
{
    for (int i = 0; i < *students_size; i++)
    {
        if (students[i].mark < number)
        {
            for (int j = i; j < *students_size; j++)
                students[j] = students[j + 1];
            (*students_size)--;
            i--;
        }
    }
}

int main(void)
{

    student_t students[5];
    int students_size;

    int rc;

    if ((rc = init_students(students, &students_size))!= 0)
        return rc;

    int number;
    scanf("%d", &number);

    delete_student(students, &students_size, number);
    if (students_size == 0)
    {
        puts("Empty array");
        return ERR_EMPTY_ARRAY;
    }

    puts("\nStudents after delete:");
    print_students(students, students_size);
    return 0;
}