# InverseTrackerAPI

<b>Документация по отправке запросов на InverseTrackerAPI.</b>

<ul>

<li><b>api/users/auth/users/</b>
    <ul>
        <li>GET-запрос - получить всех пользователей (только учителей и админов).</li>
        <li>POST-запрос - создать пользователя (только для учителей и админов).</li>
    </ul>
</li>

<br>

<li><b>api/users/auth/users/me/</b>
    <ul>
        <li>GET-запрос - получить свой аккаунт.</li>
    </ul>
</li>

<br>

<li><b>api/users/auth/token/login/</b>
    <ul>
        <li>POST-запрос - залогиниться в аккаунт и получить токен авторизации.</li>
    </ul>
</li>

<br>

<li><b>api/users/auth/token/logout/</b>
    <ul>
        <li>POST-запрос - выйти из аккаунта.</li>
    </ul>
</li>

<br>

<li><b>api/courses/</b>
    <ul>
        <li>GET-запрос - получить все курсы.</li>
        <li>POST-запрос - создать новый курс.</li>
    </ul>
</li>

<br>

<li><b>api/courses/int:pk/</b>
    <ul>
        <li>GET-запрос - получить курс</li>
        <li>PATCH-запрос - обновить курс (только для учителей и админов).</li>
        <li>DELETE-запрос - удалить курс (только для учителей и админов).</li>
    </ul>
</li>

<br>

<li><b>api/courses/category/int:pk/</b>
    <ul>
        <li>GET-запрос - получить курсы с категорией pk.</li>
    </ul>
</li>

<br>

<li><b>api/courses/categories/</b>
    <ul>
        <li>GET-запрос - получить все категории.</li>
    </ul>
</li>

<br>

<li><b>api/courses/categories/int:pk/</b>
    <ul>
        <li>GET-запрос - получить категорию pk.</li>
    </ul>
</li>

<br>

<li><b>api/courses/groups/int:pk/applications/send/</b>
    <ul>
        <li>POST-запрос - отправить заявку на курс pk (application.status=1).</li>
    </ul>
</li>

<br>

<li><b>api/courses/groups/int:pk/applications/</b>
    <ul>
        <li>GET-запрос - получить все заявки в группу pk (только для учителей и админов).</li>
    </ul>
</li>

<br>

<li><b>api/courses/groups/int:group_pk/applications/confirm/int:pk/</b>
    <ul>
        <li>UPDATE-запрос - принять заявку на в группу group_pk (application.status=2) (только для учителей и админов).</li>
    </ul>
</li>

<br>

<li><b>api/courses/groups/int:group_pk/applications/reject/int:pk/</b>
    <ul>
        <li>UPDATE-запрос - отклонить заявку в группу group_pk (только для учителей и админов).</li>
    </ul>
</li>

<br>

<li><b>api/courses/int:pk/groups/create/</b>
    <ul>
        <li>POST-запрос - создать группу и добавить в курс pk.</li>
    </ul>
</li>

<br>

<li><b>api/courses/groups/int:pk/</b>
    <ul>
        <li>GET-запрос - получить группу</li>
        <li>PATCH-запрос - обновить группу.</li>
        <li>DELETE-запрос - удалить группу.</li>
    </ul>
</li>

<br>

<li><b>api/courses/groups/int:pk/schedules/create/</b>
    <ul>
        <li>POST-запрос - создать расписание и добавить в группу pk.</li>
    </ul>
</li>

<br>

<li><b>api/courses/groups/schedules/int:pk/</b>
    <ul>
        <li>GET-запрос - получить расписание.</li>
        <li>PATCH-запрос - обновить расписание.</li>
        <li>DELETE-запрос - удалить расписание.</li>
    </ul>
</li>

<br>

<li><b>api/courses/groups/int:pk/lessons/create/</b>
    <ul>
        <li>POST-запрос - создать урок и добавить в группу pk.</li>
    </ul>
</li>

<br>

<li><b>api/courses/groups/lessons/int:pk/attendings/attendings?=1,2,3...</b>
    <ul>
        <li>UPDATE-запрос - создать присутсвия и добавить в урок pk.</li>
    </ul>
</li>

<br>

<li><b>api/courses/groups/lessons/int:pk/</b>
    <ul>
        <li>GET-запрос - получить урок.</li>
        <li>PATCH-запрос - обновить урок.</li>
        <li>DELETE-запрос - удалить урок.</li>
    </ul>
</li>

<br>

<li><b>api/courses/groups/lessons/int:pk/homeworks/create/</b>
    <ul>
        <li>POST-запрос - создать ДЗ и добавить в урок pk.</li>
    </ul>
</li>

<br>

<li><b>api/courses/groups/lessons/homeworks/int:pk/passed/passed?=1,2,3...</b>
    <ul>
        <li>UPDATE-запрос - создать список пользователей, сдавших ДЗ, и добавить в ДЗ pk.</li>
    </ul>
</li>

<br>

<li><b>api/courses/groups/lessons/homeworks/int:pk/</b>
    <ul>
        <li>GET-запрос - получить ДЗ.</li>
        <li>PATCH-запрос - обновить ДЗ.</li>
        <li>DELETE-запрос - удалить ДЗ.</li>
    </ul>
</li>

<br>

<li><b>api/news/</b>
    <ul>
        <li>GET-запрос - получить все новости.</li>
        <li>POST-запрос - создать новость.</li>
    </ul>
</li>

<br>

<li><b>api/news/int:pk/</b>
    <ul>
        <li>GET-запрос - получить новость.</li>
        <li>PATCH-запрос - обновить новость.</li>
        <li>DELETE-запрос - удалить новость.</li>
    </ul>
</li>

<br>

<li><b>api/users/me/groups/</b>
    <ul>
        <li>GET-запрос - получить свои группы.</li>
    </ul>
</li>

<br>

<li><b>api/users/me/skips/</b>
    <ul>
        <li>GET-запрос - получить свои пропуски.</li>
    </ul>
</li>

<br>

<li><b>api/users/me/doubts/</b>
    <ul>
        <li>GET-запрос - получить свои долги.</li>
    </ul>
</li>

<br>

<br>

<li><b>api/users/me/teacher/courses/</b>
    <ul>
        <li>GET-запрос - получить свои курсы (для учителей).</li>
    </ul>
</li>

<br>

<li><b>api/users/me/student/courses/</b>
    <ul>
        <li>GET-запрос - получить свои курсы (для ученика).</li>
    </ul>
</li>


</ul>

<br>

<b>Модели базы данных InverseTrackerAPI.</b>

<ul>

<li><b>Course (модель курсов):</b>
    <ul>
        <li><b>name</b> - название курса.</li>
        <li><b>description</b> - описание курса.</li>
        <li><b>groups</b> - группы курса Group.</li>
        <li><b>teacher</b> - учитель на курсе CustomUser.</li>
        <li><b>category</b> - категория курса Category.</li>
        <li><b>place</b> - место проведения курса.</li>
        <li><b>document</b> - документ курса (передавать в base64).</li>
        <li><b>image</b> - картинка курса (передавать в base64).</li>
    </ul>
</li>

<br>

<li><b>Group (модель групп):</b>
    <ul>
        <li><b>name</b> - название группы.</li>
        <li><b>schedule</b> - расписание Schedule.</li>
        <li><b>members</b> - участники CustomUser.</li>
        <li><b>lessons</b> - урок Lesson.</li>
        <li><b>applications</b> - заявки Application.</li>
        <li><b>limit</b> - лимит записи.</li>
        <li><b>open</b> - группа открыта?</li>
    </ul>
</li>


<br>

<li><b>Application (модель заявок):</b>
    <ul>
        <li><b>student</b> - отправитель заявки CustomUser.</li>
        <li><b>document</b> - заполненный документ курса (передавать в base64).</li>
        <li><b>status</b> - статус заявки (1 - передана на рассмотрение; 2 - принята; 3 - отклонена).</li>
    </ul>
</li>

<br>

<li><b>Homework (модель домашних работ):</b>
    <ul>
        <li><b>task</b> - задание.</li>
        <li><b>passed</b> - пользователи CustomUser, сдавшие ДЗ.</li>
        <li><b>date</b> - дедлайн (%d-%m-%Y).</li>
    </ul>
</li>

<br>

<li><b>Category (модель категорий):</b>
    <ul>
        <li><b>name</b> - название категории.</li>
    </ul>
</li>

<br>

<li><b>Lesson (модель уроков):</b>
    <ul>
        <li><b>name</b> - название.</li>
        <li><b>homework</b> - ДЗ Homework.</li>
        <li><b>attendings</b> - присутствующие CustomUser.</li>
        <li><b>date</b> - дата проведения (%d-%m-%Y).</li>
    </ul>
</li>

<br>

<li><b>Schedule (модель расписаний):</b>
    <ul>
        <li><b>day</b> - день недели.</li>
        <li><b>time</b> - время (%H:%M).</li>
    </ul>
</li>

<br>

<li><b>CustomUser (модель пользователей):</b>
    <ul>
        <li><b>email</b> - почта пользователя.</li>
        <li><b>firstname</b> - имя пользователя.</li>
        <li><b>lastname</b> - фамилия пользователя.
        <li><b>patronymic</b> - отчество пользователя.</li>
        <li><b>age</b> - возраст пользователя.</li>
        <li><b>school_class</b> - класс пользователя.</li>
        <li><b>role</b> - роль пользователя.</li>
        <li><b>password</b> - пароль пользователя.</li>
    </ul>
</li>

<br>

<li><b>Role (модель ролей):</b>
    <ul>
        <li><b>name</b> - название роли.</li>
    </ul>
</li>

<br>

<li><b>https://dbdesigner.page.link/1nyQHEy34o8n8SnC9 - архитектура базы данных.</b></li>

</ul>

