# NAMA : MUHAMMAD HANIF RAMADHANI
# NIM : 312510291
# MATA KULIAH : MATEMATIKA DISKRIT
# Jenis Project UAS :Implementasi Graph Menggunakan Python dengan Algoritma DFS dan BFS
-
-
Proyek ini dibuat untuk memenuhi tugas **Ujian Akhir Semester (UAS) Mata Kuliah Matematika Diskrit**.   Program ini mengimplementasikan struktur data **Graph** menggunakan bahasa pemrograman **Python** dengan representasi **Adjacency List** serta menerapkan algoritma traversal **Depth First Search (DFS)** dan **Breadth First Search (BFS)**.

# Konsep Dasar Graph
Graph adalah struktur data yang terdiri dari:
- **Vertex (Simpul)** → merepresentasikan objek
- **Edge (Sisi)** → merepresentasikan hubungan antar objek

Secara matematis, graph dapat dituliskan sebagai:
G = (V, E)
Pada proyek ini digunakan graph tidak berarah (undirected graph), di mana setiap edge dapat dilalui dua arah
Implementasi Program
# 1. Class Graph dan Adjacency List
Graph direpresentasikan menggunakan Adjacency List, yaitu setiap simpul menyimpan daftar simpul tetangganya.
 Kode Implementasi Class Graph, DFS Rekursif, dan DFS Iteratif
 <img width="697" height="838" alt="Screenshot 2026-01-13 002523" src="https://github.com/user-attachments/assets/6059c85a-970c-4f98-9d07-95da2ae34407" />
 
Penjelasan:
self.V menyimpan jumlah simpul
self.graph menyimpan adjacency list
add_edge(u, v) menambahkan sisi dua arah
DFS rekursif menelusuri graph secara mendalam
DFS iteratif menggunakan stack sebagai pengganti rekursi

# BFS dan Main Program

Algoritma Breadth First Search (BFS) digunakan untuk menelusuri graph berdasarkan tingkat kedalaman (level).
Implementasi BFS dan Main Program
<img width="694" height="439" alt="Screenshot 2026-01-13 002535" src="https://github.com/user-attachments/assets/a93ac011-f824-46b7-8bc8-05debc5c307d" />

Penjelasan:
BFS menggunakan struktur data queue
Setiap simpul dikunjungi satu kali
Cocok untuk pencarian jalur terpendek pada graph tidak berbobot

Cara Menjalankan Program
Pastikan Python sudah terinstal
Jalankan program dengan perintah: python graph.py

Hasil Output Program
Hasil Output DFS dan BFS
<img width="690" height="276" alt="Screenshot 2026-01-13 002555" src="https://github.com/user-attachments/assets/9b2f3638-d85c-4cba-b7a2-c701b04d75d8" />
Contoh hasil traversal:

Depth First Traversal (DFS):
0 1 2 3
Breadth First Traversal (BFS):
0 1 2 3
Hasil output menunjukkan bahwa algoritma DFS dan BFS berhasil berjalan sesuai dengan teori graph.

Video Penjelasan
Link video penjelasan proyek:


Kesimpulan

Program ini berhasil mengimplementasikan struktur data graph menggunakan adjacency list serta menerapkan algoritma DFS dan BFS. Implementasi ini sesuai dengan konsep graph dalam Matematika Diskrit dan dapat membantu memahami proses traversal graph secara praktis.
