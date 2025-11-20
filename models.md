course:
    title
    lesson_time
    lesson_duration
    number_of_students
    type_of_education
    level
    language
    image
    price
    logo

course_descriptions_group:
    title
    course (FK)

course_description:
    title
    description
    group (FK)

course_icon:
    icon
    course(FK)

teachers
    full_name
    specialty
    photo

images:
    image

partners:
    logo
    title

blog:
    title
    description
    image
    video
    video_url
    create_at


faq:
    title:
    answer: