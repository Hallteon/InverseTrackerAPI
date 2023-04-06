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

<li><b>api/courses/</b>
    <ul>
        <li>GET-запрос - получить все курсы.</li>
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

<li><b>api/courses/applications/send/</b>
    <ul>
        <li>POST-запрос - отправить заявку на курс.</li>
    </ul>
</li>

<br>

<li><b>api/courses/applications/course/int:pk/</b>
    <ul>
        <li>GET-запрос - получить все заявки на курс (только для учителей и админов).</li>
    </ul>
</li>

<br>


<li><b>api/courses/applications/confirm/int:pk/</b>
    <ul>
        <li>DELETE-запрос - принять заявку на курс (только для учителей и админов).</li>
    </ul>
</li>

<br>

<li><b>api/courses/applications/reject/int:pk/</b>
    <ul>
        <li>DELETE-запрос - отклонить заявку на курс (только для учителей и админов).</li>
    </ul>
</li>

<br>

<li><b>api/courses/homeworks/create/</b>
    <ul>
        <li>POST-запрос - создать домашнюю работу (только для учителей и админов).</li>
    </ul>
</li>

<br>

<li><b>api/courses/homeworks/course/int:pk/</b>
    <ul>
        <li>GET-запрос - получить все домашки на курсе.</li>
    </ul>
</li>

<br>

<li><b>api/courses/homeworks/int:pk/</b>
    <ul>
        <li>GET-запрос - получить домашку.</li>
        <li>PATCH-запрос - обновить домашку (только для учителей и админов).</li>
        <li>DELETE-запрос - удалить домашку (только для учителей и админов).</li>
    </ul>
</li>

<br>

<li><b>api/classes/</b>
    <ul>
        <li>GET-запрос - получить все классы (только для учителей и админов).</li>
    </ul>
</li>

</ul>

<br>

<b>Модели базы данных InverseTrackerAPI.</b>

<ul>
    
<li><b>Курсы:</b>
<ul>

<li><b>Course (модель курсов):</b>
    <ul>
        <li><b>name</b> - название курса.</li>
        <li><b>description</b> - описание курса.</li>
        <li><b>members</b> - участники курса.</li>
        <li><b>teacher</b> - учитель на курсе.</li>
        <li><b>time</b> - график занятий на курсе.</li>
        <li><b>category</b> - категория курса.</li>
    </ul>
</li>

<br>

<li><b>Application (модель заявок):</b>
    <ul>
        <li><b>sender</b> - отправитель заявки.</li>
        <li><b>course</b> - курс.</li>
    </ul>
</li>

<br>

<li><b>Homework (модель домашних работ):</b>
    <ul>
        <li><b>teacher</b> - учитель.</li>
        <li><b>course</b> - курс.</li>
        <li><b>text</b> - текст домашки.</li>
        <li><b>time</b> - время выполнения домашки.</li>
    </ul>
</li>

</ul>
</li>

<br>

<li><b>Пользователи:</b>
<ul>

<li><b>CustomUser (модель пользователей):</b>
    <ul>
        <li><b>email</b> - почта пользователя.</li>
        <li><b>firstname</b> - имя пользователя.</li>
        <li><b>lastname</b> - фамилия пользователя.
        <li><b>patronymic</b> - отчество пользователя.</li>
        <li><b>age</b> - возраст пользователя.</li>
        <li><b>school_class</b> - школа пользователя.</li>
        <li><b>role</b> - роль пользователя.</li>
        <li><b>password</b> - пароль пользователя.</li>
    </ul>
</li>

<br>

<li><b>Class (модель классов):</b>
    <ul>
        <li><b>number</b> - цифра класса.</li>
        <li><b>litera</b> - литера класса.</li>
    </ul>
</li>

<br>

<li><b>Role (модель ролей):</b>
    <ul>
        <li><b>name</b> - название роли.</li>
    </ul>
</li>

</ul>
</li>

</ul>

