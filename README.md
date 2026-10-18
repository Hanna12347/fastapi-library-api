یه api کتابخونه ساده که با fastapi ساخته شده 
pip install -r requirements.txt
uvicorn main:app --reload

http://127.0.0.1:8000/docs با این باز میشه 

BaseModel یک کلاس از pydantic هست که اون کلاس یک قالب داده می‌شه که خودش نوع‌ها رو چک می‌کنه داده‌ها رو تبدیل می‌کنه و ورودی اشتباه رو رد می‌کنه