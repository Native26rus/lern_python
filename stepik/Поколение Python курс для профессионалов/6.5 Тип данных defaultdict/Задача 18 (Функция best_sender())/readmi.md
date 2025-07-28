<span><h2 style="text-align: center;">Функция best_sender()</h2>

<p>Рассмотрим два списка:</p>

<pre><code class="language-python hljs" data-highlighted="yes">messages = [<span class="hljs-string">'Hi, Linda'</span>, <span class="hljs-string">'Hi, Sam'</span>, <span class="hljs-string">'How are you doing?'</span>]

senders = [<span class="hljs-string">'Sam Fisher'</span>, <span class="hljs-string">'Linda'</span>, <span class="hljs-string">'Sam Fisher'</span>]</code></pre>

<p>Первый список представляет набор отправленных сообщений в некотором мессенджере, второй список&nbsp;— набор отправителей этих сообщений. Причем сообщение <code>messages[i]</code> отправлено пользователем <code>senders[i]</code>. Каждое сообщение представляет собой последовательность слов, разделенных пробелом (знаки препинания считаются частями слов). Количество слов&nbsp;— это общее число слов, отправленное пользователем. Обратите внимание, что каждый пользователь может отправлять более одного сообщения. Например, пользователь <code>Sam Fisher</code> отправил <span><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mn>2</mn></mrow><annotation encoding="application/x-tex">2</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 0.64444em; vertical-align: 0em;"></span><span class="mord">2</span></span></span></span></span> слова в первом сообщении и <span><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mn>4</mn></mrow><annotation encoding="application/x-tex">4</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 0.64444em; vertical-align: 0em;"></span><span class="mord">4</span></span></span></span></span> слова во втором, следовательно, его количество слов равно <span><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mn>2</mn><mo>+</mo><mn>4</mn><mo>=</mo><mn>6</mn></mrow><annotation encoding="application/x-tex">2 + 4 = 6</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 0.72777em; vertical-align: -0.08333em;"></span><span class="mord">2</span><span class="mspace" style="margin-right: 0.222222em;"></span><span class="mbin">+</span><span class="mspace" style="margin-right: 0.222222em;"></span></span><span class="base"><span class="strut" style="height: 0.64444em; vertical-align: 0em;"></span><span class="mord">4</span><span class="mspace" style="margin-right: 0.277778em;"></span><span class="mrel">=</span><span class="mspace" style="margin-right: 0.277778em;"></span></span><span class="base"><span class="strut" style="height: 0.64444em; vertical-align: 0em;"></span><span class="mord">6</span></span></span></span></span>.&nbsp;</p>

<p>Реализуйте функцию <code>best_sender()</code>, которая принимает два аргумента в следующем порядке:</p>

<ul>
	<li><code>messages</code>&nbsp;— список сообщений</li>
	<li><code>senders</code>&nbsp;— список имен отправителей</li>
</ul>

<p>Функция должна определять отправителя, имеющего наибольшее количество слов, и возвращать его имя. Если таких отправителей несколько, следует вернуть имя того, чье имя больше в лексикографическом сравнении.</p>

<p><strong>Примечание 1.&nbsp;</strong>Гарантируется, что длины передаваемых в функцию списков совпадают.</p>

<p><strong>Примечание 2.</strong> В тестирующую систему сдайте программу, содержащую только необходимую функцию <code>best_sender()</code>, но не код, вызывающий ее.</p>

<p><strong>Примечание 3.</strong> Тестовые данные доступны по ссылкам:</p>

<ul>
	<li><a href="https://stepik.org/media/attachments/lesson/590035/tests_3090787.zip" rel="noopener noreferrer nofollow">Архив с тестами</a></li>
	<li><a href="https://github.com/python-generation/Professional/tree/main/Module_6/Module_6.5/Module_6.5.24" rel="noopener noreferrer nofollow" target="_blank">GitHub</a></li>
</ul></span>