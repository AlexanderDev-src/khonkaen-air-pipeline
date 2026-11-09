# แผนงาน Khon Kaen Air Pipeline

ทำทีละรอบ เสร็จรอบไหนติ๊ก `[x]` แล้ว commit

```
extract ──dict──▶ transform ──DataFrame──▶ load ──▶ data/warehouse/*.db
```

---

## ✅ รอบ 1: ตั้งโปรเจค

- [x] `uv init --bare` + `uv add requests pandas` ที่ root ของโปรเจค
- [x] `config.py`: พิกัด, `TIME_ZONE`, path ของ `data/`, URL กับ params ของทั้งสอง API

## ✅ รอบ 2: extract

- [x] `fetch_and_save_json` เรียก API, `raise_for_status()`, เซฟ JSON ลง `data/raw/`
- [x] ชื่อไฟล์มีชื่อแหล่งข้อมูลกับวันที่แบบ ISO เช่น `air_data_2026-11-01.json`
- [x] หาวันที่ข้างใน function ไม่ใช่ตอน import

## ✅ รอบ 3: transform (ครึ่งแรก)

- [x] transform รับ `data: dict` เข้ามา ไม่เรียก API เอง
- [x] `pd.DataFrame(...)` จากส่วน `hourly`
- [x] `pd.to_datetime` คอลัมน์ `time`
- [x] เช็ก shape: weather `(168, 7)`, air `(120, 3)`

---

## ✅ รอบ 4: transform (merge)

เป้าหมาย: รวม weather กับ air เป็นตารางเดียว

- [x] เขียน function ใหม่ใน `transform.py` ที่รับ DataFrame สองตัว แล้วคืน DataFrame ตัวเดียว
- [x] ใช้ `.merge(..., on="time", how=...)` แล้วเลือก `how` (weather มี 168 แถว air มี 120 แถว)
- [x] ตัดสินใจว่าจะทำยังไงกับแถวที่เป็น `NaN` (ดูด้วย `df.isna().sum()`)
- [x] ลองใน notebook ก่อน แล้วค่อยย้ายเข้า function

เสร็จเมื่อ: ได้ตารางเดียวที่มี `time`, ค่าอากาศ, `pm10`, `pm2_5` และจำนวนแถวตรงกับ `how` ที่เลือก

## ✅ รอบ 5: load

เป้าหมาย: เซฟตารางที่ merge แล้วลง SQLite

- [x] เพิ่ม path ของไฟล์ `.db` ใน `config.py` (ใน `data/warehouse/`)
- [x] `load.py`: function รับ DataFrame แล้วเขียนลงฐานข้อมูล
- [x] ใช้ `sqlite3.connect`, `df.to_sql(name, con, if_exists=..., index=False)`, `con.close()`
- [x] เลือก `if_exists`: เริ่มด้วย `"replace"` ก่อน (`"append"` รันซ้ำแล้วข้อมูลจะซ้ำ)

เสร็จเมื่อ: `pd.read_sql("SELECT * FROM ...", con)` อ่านกลับมาได้ครบทุกแถว

## ✅ รอบ 6: `__main__.py`

เป้าหมาย: สั่งคำสั่งเดียวแล้วรันครบทุกขั้น

- [x] import function จาก extract, transform, load
- [x] เรียกตามลำดับ extract → transform → merge → load
- [x] ใส่ `print(...)` บอกว่ากำลังทำขั้นไหนอยู่

เสร็จเมื่อ: รัน `uv run python -m pipeline` จาก root แล้วได้ไฟล์ JSON ใหม่ใน `data/raw/` และไฟล์ `.db` ใน `data/warehouse/`

## ⬜ รอบ 7: tests

เป้าหมาย: test transform โดยไม่ต้องใช้เน็ต

- [ ] `uv add --dev pytest`
- [ ] `tests/test_transform.py`: สร้าง dict ปลอม 2-3 ชั่วโมง แล้วส่งเข้า transform
- [ ] `assert` จำนวนแถว, ชื่อคอลัมน์ และชนิดของ `time` ว่าเป็น datetime
- [ ] test merge ด้วย DataFrame ปลอมสองตัว

เสร็จเมื่อ: `uv run python -m pytest` ผ่านทุกตัว

## ⬜ รอบ 8: เก็บกวาด

- [ ] `transform.py`: สอง function เหมือนกันทุกบรรทัด รวมเหลือตัวเดียว
- [ ] ย้าย `jupyter` ไปเป็น dev dependency (`uv remove jupyter` แล้ว `uv add --dev jupyter`)
- [ ] notebook: ลบ `print(Path.cwd())` หรือ clear output ก่อน commit (output มี path ของเครื่องติดไปด้วย)
- [ ] `README.md`: เขียนวิธีติดตั้งและวิธีรัน

## ⬜ รอบ 9: ต่อยอด (ไม่บังคับ)

- [ ] notebook: วาดกราฟ PM2.5 เทียบกับอุณหภูมิหรือลม
- [ ] เปลี่ยนเป็น `"append"` แบบไม่ให้ข้อมูลซ้ำ (เรื่อง idempotency)
- [ ] ตั้งให้รันอัตโนมัติทุกวัน เช่นใช้ cron หรือ systemd timer
