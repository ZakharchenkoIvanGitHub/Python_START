quest = (
    ('Для чего в Python используется встроенная функция enumerate()?',
     'A. Для определения количества элементов последовательности.',
     'B. Для одновременного итерирования по самим элементам и их индексам.',
     'C. Для сортировки элементов по значениям id.',
     'D. Для нумерации слов',
     'B',
     'Часто в коде начинающих разработчиков на Python можно встретить объявление for-цикла в виде for i in range(len(numbers)), когда можно обойтись for num in numbers. Если в коде действительно необходим и сам элемент, и его индекс, используйтеenumerate()'
     ),
    ('Необходимо собрать и вывести все уникальные слова из строки рекламного текста. Какой из перечисленных типов данных Python подходит лучше всего?',
     'A. кортеж (tuple)',
     'B. список (list)',
     'C. множество (set)',
     'D. словарь (dict)',
     'C',
     'Множество (set) хранит только уникальные значения. Поэтому такой тип данных является лучшим кандидатом для решения указанной задачи – все повторяющиеся (неуникальные) значения будут отброшены.'
    ),
    ('Как вывести список методов и атрибутов объекта x?',
     'A. help(x)',
     'B. info(x)',
     'C. ?x',
     'D. dir(x)',
     'D',
     'Правильный ответ – функция dir. Функция help выводит справку по объекту, доступную из строк документации, а остальные примеры не являются частью стандартной библиотеки Python.'
    ),
    (' Какая из перечисленных инструкций выполнится быстрее всего, если n = 10**6?',
     'A. a = list(i for i in range(n))',
     'B. a = [i for i in range(n)]',
     'C. a = (i for i in range(n))',
     'D. a = {i for i in range(n)}',
     'C',
     'В круглых скобках (i for i in range(n)) «чистое» выражение-генератор. Оно не загружает в память коллекцию, поэтому присваивание происходит быстрее остальных случаев, ведь сами элементы последовательности не создаются. В остальных случаях происходит создание коллекций «на месте».'
     ),
    ('С помощью Python нужно записать данные в файл, но только в том случае, если файла ещё нет. Какой режим указать в инструкции open()?',
     'A. "x"',
     'B. Никакой. Нужна предварительная проверка os.path.exists()',
     'C. "w"',
     'D. "r"',
     'A',
     'Режим 'r' используется для чтения, "w" – для записи, проверку os.path.exists(), конечно, можно использовать, но уже есть простой способ с режимом  "x". Если файл уже существует, будет вызвано исключение.'
     ),
)