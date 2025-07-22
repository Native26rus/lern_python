<span><h2 style="text-align: center;">FAKE NEWS&nbsp;🌶️</h2>

<p>Команда BEEGEEK планирует выпустить свой новый курс&nbsp;<code>08.11.2022</code>&nbsp;ровно в <code>12:00</code>. Напишите программу, которая принимает на вход текущие дату и время и определяет, сколько времени осталось до выхода курса.</p>

<p><strong>Формат входных данных</strong><br>
На вход программе подаются текущие дата и время в формате <code>DD.MM.YYYY HH:MM</code>.</p>

<p><strong>Формат выходных данных</strong><br>
Программа должна вывести текст с указанием количества дней и часов, оставшихся до выхода курса, в следующем формате:</p>

<pre><code class="language-no-highlight hljs">До выхода курса осталось: &lt;кол-во дней&gt; дней и &lt;кол-во часов&gt; часов</code></pre>

<p>Если в данном случае количество часов равно нулю, то вывести нужно только дни.</p>

<p>Если количество дней равно нулю, то вывести нужно только часы и минуты в следующем формате:</p>

<pre><code class="language-no-highlight hljs">До выхода курса осталось: &lt;кол-во часов&gt; часов и &lt;кол-во минут&gt; минут</code></pre>

<p>Если в данном случае количество минут равно нулю, то вывести нужно только часы.&nbsp;Аналогично, если&nbsp;количество часов равно нулю, то вывести нужно только минуты.</p>

<p>Если введенные дата и время больше либо равны&nbsp;<code>08.11.2022 12:00</code>, программа должна вывести текст:&nbsp;</p>

<pre><code class="language-no-highlight hljs">Курс уже вышел!</code></pre>

<p><strong>Примечание 1.&nbsp;</strong>Программа должна подбирать правильную форму для существительных&nbsp;«день» и «минута». Для этого можете смело взять свою функцию&nbsp;<code>choose_plural()</code>&nbsp;из <a href="https://stepik.org/lesson/569748/step/14?unit=564262" rel="noopener noreferrer nofollow">этой задачи</a>.</p>

<p><strong>Примечание 2.</strong> Тестовые данные доступны по ссылкам:</p>

<ul>
	<li><a href="https://stepik.org/media/attachments/lesson/571244/tests_2506742.zip" rel="noopener noreferrer nofollow">Архив с тестами</a></li>
	<li><a href="https://github.com/python-generation/Professional/tree/main/Module_3/Module_3.5/Module_3.5.8" rel="noopener noreferrer nofollow" target="_blank">GitHub</a></li>
</ul></span>