# Спецификация требований программного обеспечения
проект: gptNotes.
автор: Аникиев Ян.

## Introduction

### Purpose

Проект gptNotes направлен на реализацию веб-менеджера заметок с встроенными функциями работы с текстом посредством модели GPT. Проект выполняется одним человеком в рамках проектного семинара ФКН НИУ ВШЭ.

Сервис gptNotes будет представлять собой только сайт. Для работы с сайтом каждый пользователь должен пройти регистрацию. У каждого пользователя есть список его заметок и возможность создать новую. Заметки хранятся на сервере в базе данных. Заметка представляет собой текстовый заголовок и основное текстовое поле заметки. В поле не предусмотрена разметка и возможность добавления медиа-файлов. На сайте в режиме редактирования заметки должно быть выпадающее меню с кнопками обработки текущего текста в поле. По нажатию на кнопку текст поля копируется, отправляется в API GPT вместе с нужным промтом, ответ нейросети вставляется обратно в поле вместо изначального текста. Также на сайте должна быть предусмотрена кнопка отмены последнего действия GPT.

### Document conventions

**GPT** -- алгоритм обработки естественного языка от OpenAI.

**промпт** - текстовый запрос к GPT

**поле** - текстовое поле, в которое пользователь может вводить текст

**заметка** - совокупность текстового заголовка и текстового поля

### Intended Audience and Reading Suggestions

--

### Project scope

Веб-сайт

### References

https://devdocs.io/flask/

https://openai.com/

## Overall Description

### Product perspective

--

### Product features

1. Написать заметку
2. Обработать текст заметки

### User classes and characteristics

--

### Operating environment

--

### Design and implementation constraints

--

### User documentation

--

### Assumptions and dependencies

--

## System features

### System feature X (таких блоков может быть несколько)

--

### Description and priority

--

### Stimulus/Response sequences

--

### Functional requirements

--

## External interface requirements

### User interfaces

--

### Software interfaces

--

### Hardware interfaces

--

### Communication interfaces

--

## Non functional requirements

### Performance requirements

--

### Safety requirements

--

### Software quality attributes

--

### Security requirements

--

## Other requirements

--

## Appendix A: Glossary

--

## Appendix B: Analysis Models

--

## Appendix C: Issues list

--
