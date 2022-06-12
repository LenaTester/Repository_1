https://quotes.toscrape.com/

XPath Axes
1. //div[@class="row header-box"]
2. //div[@class="row header-box"]/ancestor::*
3. //div[@class="row header-box"]/ancestor::div
4. //div[@class="col-md-8"]/ancestor::div[@class="row header-box"]
5. $x('//div[@class="col-md-8"]/attribute::class')
6. //div[@class="col-md-8"]/child::h1
7. //div[@class="col-md-8"]/h1/descendant::a
8. //div[@class="col-md-8"]/following::div
9. //div[@class="col-md-8"]/following::div[@class="quote"]
10. //div[@class="col-md-8"]/following-sibling::*
11. //div[@class="col-md-8"]/parent::*
12. //div[@class="col-md-8"]/parent::div/parent::*
13. //span[@class="text" and @itemprop="text"]
14. //a[text() = "Login"]
15. //*[contains(@class, "quote")]
16. //span[text() = '❤']
17. //span/small[@class = "author" and text() = "Albert Einstein"]
18. //span/small[@class = "author" and text() = "Albert Einstein"]/ancestor::*
19. //span/small[@class = "author" and text() = "Albert Einstein"]/ancestor::div
20. //span/small[@class = "author" and text() = "Albert Einstein"]/ancestor::div[@class="quote"]
21. //span/small[@class = "author" and text() = "Albert Einstein"]/following::a
22. //span/small[@class = "author" and text() = "Albert Einstein"]/following::div[@class = "quote"]
23. //span/small[@class = "author" and text() = "Albert Einstein"]/following-sibling::*
24. //span/small[@class = "author" and text() = "Albert Einstein"]/parent::*
25. //*[contains(@class, "copyright")]
26. //*[contains(@class, "copyright")]/ancestor::div
27. //*[contains(@class, "copyright")]/child::span
28. //*[contains(@class, "copyright")]/parent::*
29. //a[text() = "Scrapinghub"]
30. //footer[@class="footer"]

CSS locators for first 10 XPath
1. $$('div[class="row header-box"]')
2. $$('html[lang="en"]')
3. $$("html body div")
4. $$("html body div div")
5. $$('div[class="col-md-8"]')
6. $$('div[class="col-md-8"] h1')
7. $$('div[class="col-md-8"] h1 a')
8. $$('div[class="col-md-8"] div')
9. $$('div[class="col-md-8"] div[class="Quote"]')
10. $$('div[class="col-md-8"] div[class="col-md-4"]')