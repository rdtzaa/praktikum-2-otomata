# Praktikum #2 — FSM Visualisation
**Mata Kuliah:** Otomata  
| Name           | NRP        | Kelas     |
| ---            | ---        | ----------|
| Raditya Zhafran Pranuja | 5025241120 | A |
| Erlangga Rizqi Dwi Raswanto | 5025241179 | A |
| Jalu Cahyo Senodiputro | 5025241155 | A |

---

## 📋 Deskripsi Tugas

Membuat program komputer untuk mengotomasi sebuah **Finite State Machine (FSM)** yang dapat menentukan apakah sebuah string merupakan anggota dari himpunan bahasa:

> **L = { x ∈ (0 + 1)⁺ | karakter terakhir pada string x adalah 1 dan x tidak memiliki substring 00 }**

Program harus memiliki user interface yang memudahkan pengguna untuk menginputkan string dan melihat proses identifikasi keanggotaannya.

---

## 🔧 Dependencies

- **Python 3**
- **Tkinter** : library GUI bawaan Python untuk antarmuka grafis
- **re** : library regex untuk validasi input

---

## 🗂️ Struktur FSM

### State

| State | Keterangan |
|-------|------------|
| **S** | Start state (initial state) |
<!-- | **A** | State setelah membaca `0` dari S | -->
| **B** | Final state — string diterima jika berakhir di sini |
| **C** | Dead/trap state — dicapai saat muncul substring `00` |

### Tabel Transisi

| State | Input `0` | Input `1` |
|-------|-----------|-----------|
| S | → A | → B |
| A | → C | → B |
| B | → A | → B |
| C | → C | → C |

> **Final State:** B   
> **Trap State/Dead State:** C

### Diagram FSM

```
        0           0
  S --------→ A --------→ C ↺ (0,1)
  |           ↑↓ 1
  | 1         |
  ↓       0   |
  B ←---------┘
  ↺ (1)
```

---

## Contoh Pengujian

| String | Jalur State | Hasil |
|--------|-------------|-------|
| `111` | S → B → B → B | ✅ **Accepted** |
| `101` | S → B → A → B | ✅ **Accepted** |
| `1001` | S → B → A → C → C | ❌ **Rejected** (ada substring `00`) |
| `0` | S → A | ❌ **Rejected** (tidak berakhir di B) |
| `10` | S → B → A | ❌ **Rejected** (karakter terakhir bukan `1`) |

---

## 💻 How to Run


```bash
python --version   # python 3.x
```

### Run Program

```bash
python praktikum_2.py
```

### How to Use (input)

1. Ketikkan string biner (hanya karakter `0` dan `1`) pada kolom input
2. Klik tombol **Load** untuk load string
3. Klik **Continue step** secara berulang untuk melihat proses transisi state satu per satu
4. State yang sedang aktif akan ditandai dengan warna **hijau** pada diagram
5. Setelah semua karakter diproses, program akan menampilkan hasil **Accepted** atau **Rejected**
6. Klik **Reset** untuk memulai ulang dengan string baru

---

## 🖥️ Fitur Program

- **Visualisasi FSM** — diagram state ditampilkan secara grafis di canvas
- **Step-by-step execution** — pengguna dapat melihat transisi state satu per satu
- **Highlight state** — state yang sedang dikunjungi disorot dengan warna hijau
- **Indikator karakter saat ini** — karakter yang sedang diproses ditandai dengan kurung siku `[x]`
- **Validasi input** — program menolak input yang bukan string biner
- **Pop-up hasil** — menampilkan popup Accepted/Rejected beserta final state

---

## 📁 Struktur File

```
praktikum_2/
└── praktikum_2.py    # source code
```

---
