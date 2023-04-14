
 سیسیتم کنترل و مدیریت تردد خودروها که با Django Rest Framework طراحی شده است و به شرح زیر میباشد: <br>
 
<p> این سیستم شامل موجودیت های راننده ، خودروهای سبک و سنگین ، ایستگاه های دریافت عوارض ، و شبکه
راه است که خودروها دارای سیستم تعیین موقعیت هستند.</P>
<p> در این سیستم خودروهای سنگین فقط می توانند در خیابان های با عرض بیشتر از بیست متر تردد داشته باشند
و علاوه بر عوارض ثابتی که خودروهای سبک ملزم به پرداخت به ازای هر بار عبور هستند باید متناسب با وزن
قابل بارگیری خود عوارض پرداخت کنند.خودروهای سنگین به ازای هر کیلوگرم وزن قابل بارگیری 300 تومان
باید بپردازند.</p>
<p> خودروها می توانند در رنگ و طول و مالک متفاوت باشند و هر نفر می تواند صاحب چندین ماشین سبک باشد
ولی فقط می تواند مالک تنها یک ماشین سنگین باشد. هر شخص هم دارای نام ، کد ملی و سن است. راه ها در
عرض و نام متمایز می شوند. </P>
<p> 
سرویس های restful طراحی شدند که نیاز کاربر را برطرف کنند.<br>
 دریافت لیست خودروهایی که رنگ قرمز و آبی دارند.<br>
 ثبت کاربر و خودرو<br>
 دریافت لیست خوردوهایی که سن مالک آنها بیشتر از 70 سال است.<br>
 دریافت لیست خوردروهای سنگین که در خیابان های کمتر از عرض مجاز بیست متر تردد داشته اند.<br>
 عوارض یک خوردو و مالک در طول مدت زمان معین<br>
 نام و کد ملی مالک هایی که تخلف عوارضی داشته اند به ترتیب میزان تخلف<br>
</p>
