<span><h2 style="text-align: center;">Класс BirthInfo 🌶️</h2>

<p>Реализуйте класс <code>BirthInfo</code>, описывающий данные о дате рождения.&nbsp;При создании экземпляра класс должен принимать один аргумент:</p>

<ul>
	<li><code>birth_date</code>&nbsp;— дата рождения, представленная в одном из следующих вариантов:</li>
</ul>

<ol>
	<li>экземпляр класса&nbsp;<code>date</code></li>
	<li>строка с датой в ISO формате</li>
	<li>список или кортеж из трех целых чисел: года, месяца и дня</li>
</ol>

<p>Если дата рождения является некорректной или представлена в каком-либо другом формате, должно быть возбуждено исключение <code>TypeError</code> с текстом:</p>

<pre style="position: relative;"><code class="language-no-highlight hljs">Аргумент переданного типа не поддерживается</code><button class="copy-code-btn st-button_style_none copy-code-btn__code-block" type="button" title="Скопировать код"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                      <path d="M19.2 3H10.2C9.2073 3 8.4 3.8073 8.4 4.8V8.4H4.8C3.8073 8.4 3 9.2073 3 10.2V19.2C3 20.1927 
                      3.8073 21 4.8 21H13.8C14.7927 21 15.6 20.1927 15.6 19.2V15.6H19.2C20.1927 15.6 21 14.7927 21 13.8V4.8C21 3.8073 
                      20.1927 3 19.2 3ZM4.8 19.2V10.2H13.8L13.8018 19.2H4.8ZM19.2 13.8H15.6V10.2C15.6 9.2073 14.7927 8.4 13.8 8.4H10.2V4.8H19.2V13.8Z" fill="#777777"></path>
                  </svg>
                  </button></pre>

<p>Экземпляр класса&nbsp;<code>BirthInfo</code> должен иметь один атрибут:</p>

<ul>
	<li><code>birth_date</code> — дата&nbsp;рождения&nbsp;в виде экземпляра класса <code>date</code></li>
</ul>

<p>Класс&nbsp;<code>BirthInfo</code> должен иметь одно свойство:</p>

<ul>
	<li><code>age</code>&nbsp;— свойство, доступное только для чтения, возвращающее&nbsp;текущий возраст в годах, то есть количество полных лет,&nbsp;прошедших с даты рождения&nbsp;на сегодняшний день</li>
</ul>

<p><strong>Примечание 1. </strong>Возраст в годах должен вычисляться так же, как и обычный возраст человека, то есть в день рождения его возраст увеличивается на один год.</p>

<p>Приведенный ниже код:</p>

<pre style="position: relative;"><code class="language-python hljs" data-highlighted="yes">birthinfo = BirthInfo(date(<span class="hljs-number">2023</span>, <span class="hljs-number">2</span>, <span class="hljs-number">26</span>))

<span class="hljs-built_in">print</span>(birthinfo.age)</code><button class="copy-code-btn st-button_style_none copy-code-btn__code-block" type="button" title="Скопировать код"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                      <path d="M19.2 3H10.2C9.2073 3 8.4 3.8073 8.4 4.8V8.4H4.8C3.8073 8.4 3 9.2073 3 10.2V19.2C3 20.1927 
                      3.8073 21 4.8 21H13.8C14.7927 21 15.6 20.1927 15.6 19.2V15.6H19.2C20.1927 15.6 21 14.7927 21 13.8V4.8C21 3.8073 
                      20.1927 3 19.2 3ZM4.8 19.2V10.2H13.8L13.8018 19.2H4.8ZM19.2 13.8H15.6V10.2C15.6 9.2073 14.7927 8.4 13.8 8.4H10.2V4.8H19.2V13.8Z" fill="#777777"></path>
                  </svg>
                  </button></pre>

<p>в <code>2024-02-25</code> должен выводить:</p>

<pre style="position: relative;"><code class="language-no-highlight hljs">0</code><button class="copy-code-btn st-button_style_none copy-code-btn__code-block" type="button" title="Скопировать код"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                      <path d="M19.2 3H10.2C9.2073 3 8.4 3.8073 8.4 4.8V8.4H4.8C3.8073 8.4 3 9.2073 3 10.2V19.2C3 20.1927 
                      3.8073 21 4.8 21H13.8C14.7927 21 15.6 20.1927 15.6 19.2V15.6H19.2C20.1927 15.6 21 14.7927 21 13.8V4.8C21 3.8073 
                      20.1927 3 19.2 3ZM4.8 19.2V10.2H13.8L13.8018 19.2H4.8ZM19.2 13.8H15.6V10.2C15.6 9.2073 14.7927 8.4 13.8 8.4H10.2V4.8H19.2V13.8Z" fill="#777777"></path>
                  </svg>
                  </button></pre>

<p>в <code>2024-02-26</code>&nbsp;должен выводить:</p>

<pre style="position: relative;"><code class="language-no-highlight hljs">1</code><button class="copy-code-btn st-button_style_none copy-code-btn__code-block" type="button" title="Скопировать код"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                      <path d="M19.2 3H10.2C9.2073 3 8.4 3.8073 8.4 4.8V8.4H4.8C3.8073 8.4 3 9.2073 3 10.2V19.2C3 20.1927 
                      3.8073 21 4.8 21H13.8C14.7927 21 15.6 20.1927 15.6 19.2V15.6H19.2C20.1927 15.6 21 14.7927 21 13.8V4.8C21 3.8073 
                      20.1927 3 19.2 3ZM4.8 19.2V10.2H13.8L13.8018 19.2H4.8ZM19.2 13.8H15.6V10.2C15.6 9.2073 14.7927 8.4 13.8 8.4H10.2V4.8H19.2V13.8Z" fill="#777777"></path>
                  </svg>
                  </button></pre>

<p>в <code>2025-02-25</code>&nbsp;должен выводить:</p>

<pre style="position: relative;"><code class="language-no-highlight hljs">1</code><button class="copy-code-btn st-button_style_none copy-code-btn__code-block" type="button" title="Скопировать код"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                      <path d="M19.2 3H10.2C9.2073 3 8.4 3.8073 8.4 4.8V8.4H4.8C3.8073 8.4 3 9.2073 3 10.2V19.2C3 20.1927 
                      3.8073 21 4.8 21H13.8C14.7927 21 15.6 20.1927 15.6 19.2V15.6H19.2C20.1927 15.6 21 14.7927 21 13.8V4.8C21 3.8073 
                      20.1927 3 19.2 3ZM4.8 19.2V10.2H13.8L13.8018 19.2H4.8ZM19.2 13.8H15.6V10.2C15.6 9.2073 14.7927 8.4 13.8 8.4H10.2V4.8H19.2V13.8Z" fill="#777777"></path>
                  </svg>
                  </button></pre>

<p>&nbsp;в <code>2025-02-26</code>&nbsp;должен выводить:</p>

<pre style="position: relative;"><code class="language-no-highlight hljs">2</code><button class="copy-code-btn st-button_style_none copy-code-btn__code-block" type="button" title="Скопировать код"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                      <path d="M19.2 3H10.2C9.2073 3 8.4 3.8073 8.4 4.8V8.4H4.8C3.8073 8.4 3 9.2073 3 10.2V19.2C3 20.1927 
                      3.8073 21 4.8 21H13.8C14.7927 21 15.6 20.1927 15.6 19.2V15.6H19.2C20.1927 15.6 21 14.7927 21 13.8V4.8C21 3.8073 
                      20.1927 3 19.2 3ZM4.8 19.2V10.2H13.8L13.8018 19.2H4.8ZM19.2 13.8H15.6V10.2C15.6 9.2073 14.7927 8.4 13.8 8.4H10.2V4.8H19.2V13.8Z" fill="#777777"></path>
                  </svg>
                  </button></pre>

<p><strong>Примечание 2.</strong>&nbsp;Для проверки того, что свойство <code>age</code> возвращает верный возраст, мы используем собственную функцию <code>current_age()</code>, которая вычисляет возраст в годах на основе даты рождения и текущей даты.</p>

<p><strong>Примечание 3.&nbsp;</strong>Никаких ограничений касательно реализации класса&nbsp;<code>BirthInfo</code> нет, она может быть произвольной.</p>

<p><strong>Примечание 4.</strong> Тестовые данные доступны по ссылкам:</p>

<ul>
	<li><a href="https://stepik.org/media/attachments/lesson/802381/19.zip" rel="noopener noreferrer nofollow">Архив с тестами</a></li>
	<li><a href="https://github.com/python-generation/OOP/tree/main/Module_4/Module_4.8/Module_4.8.19" rel="noopener noreferrer nofollow" target="_blank">GitHub</a></li>
</ul></span>