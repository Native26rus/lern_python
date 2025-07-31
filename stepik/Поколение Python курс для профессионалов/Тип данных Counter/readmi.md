<span><h2 style="text-align: center;">Функция&nbsp;print_bar_chart()</h2>

<p>Реализуйте функцию <code>print_bar_chart()</code>, которая принимает два аргумента в следующем порядке:</p>

<ul>
	<li><code>data</code>&nbsp;—&nbsp;строка или список строк</li>
	<li><code>mark</code>&nbsp;—&nbsp;одиночный символ</li>
</ul>

<p>Функция должна определять:</p>

<ul>
	<li>сколько раз встречается каждый символ в строке, если <code>data</code> является строкой</li>
	<li>сколько раз встречается каждая строка в списке, если <code>data</code>&nbsp;является списком</li>
</ul>

<p>Затем функция должна выводить результат в виде столбчатой диаграммы, указывая каждый символ (строку) и его количество. Количество отображается как повторение символа <code>mark</code> соответствующее число раз, например, если <code>mark='+'</code>, то количество, равное четырем, будет отображено как <code>++++</code>. Символы (строки) в диаграмме должны быть расположены в порядке уменьшения количества, при равных количествах&nbsp;— в своем исходном порядке, каждая на отдельной строке, в следующем формате:</p>

<pre><code class="language-no-highlight hljs">&lt;символ или строка&gt; |&lt;количество&gt;</code></pre>

<p><strong>Примечание 1.&nbsp;</strong>Обратите внимание на второй тест, функция должна добавлять нужное количество пробелов, если строка имеет меньшую длину, чем другие.</p>

<p><strong>Примечание 2.</strong>&nbsp;Программа должна учитывать регистр. То есть, например, строки&nbsp;<code>Python</code> и <code>python</code> считаются различными.</p>

<p><strong>Примечание 3.</strong>&nbsp;В тестирующую систему сдайте программу, содержащую только необходимую функцию&nbsp;<code>print_bar_chart()</code>, но не код, вызывающий ее.</p>

<p><strong>Примечание 4.</strong> Тестовые данные доступны по ссылкам:</p>

<ul>
	<li><a href="https://stepik.org/media/attachments/lesson/635441/tests_2609489.zip" rel="noopener noreferrer nofollow">Архив с тестами</a></li>
	<li><a href="https://github.com/python-generation/Professional/tree/main/Module_6/Module_6.8/Module_6.8.20" rel="noopener noreferrer nofollow" target="_blank">GitHub</a></li>
</ul></span>