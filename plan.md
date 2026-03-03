1. **Add new inputs to the Salary Modal:**
   - Add a field for "Günlük Etkinlik Saati" (Daily Activity Hours).
   - Add a field for "Kulüp Grup (sınıf) Sayısı" (Club Group/Class Count).
   - Add a field for "Devlet Memuru Aylığı" (highest state civil servant monthly gross), default to 13.184,77.

2. **Update calculation logic in `renderSalaries`:**
   - Instead of calculating pool distributions *only*, we will calculate max gross salary cap for each role based on multipliers (Manager: 2.75, Deputy: 2.5, Teacher: 4.0, Usta Öğretici: 4.0, Accounting/Cleaning: 2.0).
   - If the calculated percentage-based gross exceeds the maximum cap, the gross is capped at the maximum allowed amount.
   - The school's determined monthly fee is `saat ücreti * günlük etkinlik saati * aylık iş günü sayısı`.
   - Update `renderSalaries` to apply these rules when the "Hesapla" button (`#btnCalcSalaries`) is clicked.

3. **Add new row entries to Personnel Data:**
   - When calculating the salaries and the distributions, add two new rows inside the table:
     - "Temel Giderler" (%26 cut from total pool).
     - "Denetleme Yetkilisi" (%1 cut from total pool).
   - These will visually appear at the bottom of the table like staff members but read-only.

4. **Complete Pre-Commit Steps:**
   - Ensure `pre_commit_instructions` tests are run and the frontend UI changes are verified via Playwright screenshot.
5. **Submit changes:**
   - Request user approval.
