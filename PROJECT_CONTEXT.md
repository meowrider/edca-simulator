# 🧠 EDCA Simulator - Master Project Context

**อัปเดตล่าสุด:** 15 มีนาคม 2026
**สถานะโปรเจกต์:** MVP (Production-Ready)
**Repository:** `meowrider/edca-simulator` (GitHub)
**Live URL (GitHub Pages):** https://meowrider.github.io/edca-simulator/

---

## 👥 บทบาทในทีม (Roles)
- **CEO (Boss / Paul Amornkul):** ผู้กำหนดวิสัยทัศน์, ออกแบบ Business Logic, ทำการตลาด, และทดสอบ Product (ไม่มีความรู้เชิง Technical ไม่ต้องยุ่งกับ Code/Server)
- **CTO (Meow-AI):** จัดการงาน Technical 100% (Coding, GitHub, Deploy, Server, Database) ตัดสินใจเชิงเทคนิคแทน CEO ได้เลย แต่ต้องขออนุญาตในเรื่องธุรกิจหรือสิทธิ์เข้าถึง

---

## 🎯 ภาพรวมโปรเจกต์ (Project Overview)
**"The Ultimate EDCA Simulator"** หรือ **Boss Quant** 
เครื่องมือช่วยนักลงทุนจำลองกลยุทธ์การลงทุนแบบ DCA ขั้นสูง (Enhanced DCA) เพื่อแก้ปัญหาการทำ DCA แบบเก่าที่ "ซื้อของแพงโดยไม่จำเป็น" และ "กระสุนหมดตอนตลาดพัง"

### 💡 Core Logic (กลยุทธ์หลัก 2 แบบ)
1. **Pure Value Averaging (Pure VA):**
   - **คอนเซปต์:** ซื้อเพื่อถมพอร์ตให้ถึงเป้าหมายที่ตั้งไว้ (Fix Target Portfolio Value)
   - **สูตร:** `Target = จำนวนงวด * เงินเป้าหมายต่องวด` -> `Deficit = Target - มูลค่าพอร์ตปัจจุบัน`
   - **Action:** ถ้า Deficit > 0 ให้ซื้อเท่ากับที่ขาด (ไม่เกินเงินสดที่มี) / ถ้า Deficit <= 0 ให้ "ถือ" (Hold) เพราะกำไรเกินเป้าแล้ว
2. **Multiplier EDCA (ดูตลาดด้วย SMA 200):**
   - **คอนเซปต์:** ปรับตัวคูณการซื้อ (Multiplier) ตามสภาวะตลาด โดยอ้างอิงจากเส้น SMA 200 วัน
   - **💥 ตลาดพัง (Crash):** ราคา < `SMA200 * 0.7` ➡️ **ซื้อ 5X**
   - **📉 ตลาดตก (Bear):** ราคา < `SMA200` ➡️ **ซื้อ 2X**
   - **🆗 ตลาดปกติ (Normal):** `SMA200` <= ราคา <= `SMA200 * 1.3` ➡️ **ซื้อ 1X**
   - **📈 ตลาดกระทิง (Bull):** ราคา > `SMA200 * 1.3` ➡️ **ซื้อ 0.5X**

---

## 🛠 Tech Stack & Architecture
- **Frontend:** HTML5, Tailwind CSS, Vanilla JavaScript (ออกแบบสไตล์ Glassmorphism หรูหรา)
- **Data Source:** ใช้ข้อมูลประวัติศาสตร์ BTC แบบ Static เก็บไว้ใน `btc_data.js` เพื่อความเร็วสูงสุด (ไม่ต้องรอ API)
  - มีสคริปต์ `fetch_data.js` (Node) และ `make_excel.py` (Python) ไว้สำหรับดึงข้อมูลกราฟอัปเดต
- **Database (MVP Phase):** เชื่อมต่อฟอร์มสมัคร Early Access เข้ากับ **Google Sheets** ผ่าน Webhook (Google Apps Script) ฟรีและเร็ว
- **Integration:** มีระบบ Generate โค้ด **Pine Script v5** แบบ Custom ตามค่าที่ลูกค้ากรอก เพื่อให้ลูกค้าก๊อปปี้ไปวางใน TradingView (Strategy Tester) ได้ทันที

---

## 📁 โครงสร้างไฟล์ปัจจุบัน (File Structure)
1. `index.html` - Landing Page อธิบาย Pain point และเปิดรับสมัคร Early Access
2. `simulator.html` - หน้า Core Product สำหรับจำลองแผนลงทุน และ Gen Pine Script
3. `auth.html` - หน้าล็อกอิน (UI สำหรับเตรียมขยายผล)
4. `btc_data.js` - ก้อนข้อมูลกราฟ BTC ย้อนหลัง
5. `EDCA_NextSteps.md` & `EDCA_Sniper_V1.pine` - ไฟล์แผนงานและโค้ด Pine Script ต้นฉบับ

---

## 🚀 แผนการ Deploy (Deployment Strategy)
- **Phase 1 (MVP - ปัจจุบัน):** โฮสต์ฟรีผ่าน **GitHub Pages** (ตอนนี้ออนไลน์แล้วที่ `https://meowrider.github.io/edca-simulator/`) เพื่อให้ CEO ส่งลิงก์เทสและหา Feedback จากคนรอบข้าง
- **Phase 2 (Scale-up - อนาคต):** เมื่อพร้อมทำระบบสมาชิกเก็บเงิน CTO จะจัดการเช่า **VPS / Vercel** และเขียน Backend (Node.js) + Database (PostgreSQL/MongoDB) เต็มรูปแบบ