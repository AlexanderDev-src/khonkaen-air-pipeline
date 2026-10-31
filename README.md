# Khon Kaen Air Pipeline

ติดตามค่าฝุ่น PM2.5 และสภาพอากาศของจังหวัดขอนแก่น ด้วยข้อมูลจาก Open-Meteo

## โครงสร้าง

```
khonkaen-air/
├── pipeline/
│   ├── config.py      ค่าตั้งต้น เช่น พิกัด เขตเวลา path
│   ├── extract.py     ดึงข้อมูลจาก API
│   ├── transform.py   แปลงและรวมข้อมูล
│   ├── load.py        บันทึกข้อมูลลงฐานข้อมูล
│   └── __main__.py    จุดเริ่มรัน pipeline
├── data/
│   ├── raw/           ข้อมูลดิบจาก API
│   └── warehouse/     ฐานข้อมูลที่ผ่านการแปลงแล้ว
├── notebooks/         EDA และกราฟ
└── tests/             เทส
```

## แหล่งข้อมูล

- Air Quality API: https://open-meteo.com/en/docs/air-quality-api
- Weather Forecast API: https://open-meteo.com/en/docs
