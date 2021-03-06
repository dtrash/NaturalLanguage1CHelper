﻿
&НаСервере
Функция ДернутьСервисНаСервере()
	
	ИмяСервера = "martyshin-s";
	ПортСервера = 5000;
	ХТТПСоединение = Новый HTTPСоединение(ИмяСервера, ПортСервера);
	
	СтрокаЗапроса = "/GetHelp";
	Запрос = Новый HTTPЗапрос(СтрокаЗапроса);
	Запрос.Заголовки.Вставить("Content-type", "application/json");
	
	JSON = "{ ""query"": """ + ВопросПользователя + """ }";
	Запрос.УстановитьТелоИзСтроки(JSON, КодировкаТекста.UTF8);
	
	Ответ = ХТТПСоединение.ОтправитьДляОбработки(Запрос);
	
	ОтветСтрокой = Ответ.ПолучитьТелоКакСтроку();
	
	//Сообщить("Код результат: " + Ответ.КодСостояния);
	//Сообщить("Ответ: " + ОтветСтрокой);
	
	Джейсон = Новый ЧтениеJSON;
	Джейсон.УстановитьСтроку(ОтветСтрокой);
	
	ДанныеСервиса = ПрочитатьJSON(Джейсон);
	Для Каждого ЭлементДанныхСервиса Из ДанныеСервиса Цикл
		Если ЭлементДанныхСервиса.Ключ = "form" Тогда
			Возврат ЭлементДанныхСервиса.Значение;
		КонецЕсли;
	КонецЦикла;
	
	Возврат Неопределено;
	
КонецФункции

&НаКлиенте
Процедура ДернутьСервис(Команда)
	
	ИмяОткрываемойФормы = ДернутьСервисНаСервере();
	Если ИмяОткрываемойФормы <> Неопределено Тогда
		ОткрытьФорму(ИмяОткрываемойФормы);
	Иначе
		Сообщить("Ничем не могу помочь :(");
	КонецЕсли;
	
КонецПроцедуры
