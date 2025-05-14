from telegram import Bot
from datetime import datetime
import random
import os

TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")
THREAD_ID = os.getenv("THREAD_ID")  # kalau pakai topik di grup

motivasi_list = [
    "1 tweet hari ini bisa jadi $1,000 nanti. Fokus farming, bukan ngeluh.",
    "Lelahmu hari ini akan dibayar saat listing nanti. Jangan nyerah!",
    "Rezeki nggak instan, tapi effort lo hari ini bisa jadi cuan seumur hidup.",
    "Airdrop itu bukan hoki, tapi hasil dari disiplin dan konsisten.",
    "Kalo orang lain bisa dapet ratusan juta dari airdrop, kenapa lo enggak?",
    "Lo sibuk ngeluh, orang lain sibuk farming. Siapa yang bakal cuan?",
    "Nggak semua orang paham airdrop, makanya cuma sedikit yang panen.",
    "Dari satu klik, lahirlah dompet yang tebal. Lanjut terus!",
    "Waktu luang + disiplin = Airdrop berjuta-juta.",
    "Skip hari ini = skip peluang. Gaskan walau cuma 1 tugas.",
    "Capek itu wajar, tapi jangan berhenti. Snapshot bisa terjadi kapan aja.",
    "Airdrop hunter sejati bukan yang paling banyak akun, tapi paling konsisten.",
    "Lo nggak harus perfect, yang penting jalan terus tiap hari.",
    "Eksekusi lebih penting daripada mikir terlalu banyak.",
    "Konsistensi kecil tiap hari = cuan besar di akhir jalan.",
    "Jangan tunggu semangat, yang penting gerak dulu.",
    "Satu form hari ini bisa jadi ETH nanti. Isi aja dulu.",
    "Snapshot itu nggak nunggu lo mood. Farming terus!",
    "Proyek nggak nanya lo capek, tapi nanya lo eligible apa nggak.",
    "Airdrop itu kayak investasi waktu, hasilnya nggak instan tapi nyata.",
    "Lebih baik farming 1 tugas daripada ngestalk orang dapet $10K.",
    "Lo nggak gagal, lo cuma butuh lanjut farming sedikit lagi.",
    "Banyak yang nyerah sebelum hadiahnya turun. Jangan jadi salah satu.",
    "Capek itu bonus, snapshot itu tujuan.",
    "Kalau project-nya scam, lo belajar. Kalau legit, lo cuan.",
    "Yang penting gerak. Bukan yang paling pinter yang panen, tapi yang paling rajin.",
    "Setiap klik itu doa lo buat masa depan lebih cuan.",
    "Kerja keras farming hari ini = ngopi santai waktu token listing.",
    "Yang nyesel itu bukan yang gagal, tapi yang nyerah di tengah jalan.",
    "1 thread, 1 like, 1 quote bisa jadi tiket ke bullrun.",
    "Banyak akun tanpa aksi = nol. Sedikit akun tapi disiplin = dolar.",
    "Nggak ada yang ngasih airdrop buat yang mager.",
    "Lo ngeluh? Snapshot tetap jalan, eligible tetap orang yang gerak.",
    "Jangan kebanyakan nunggu signal, lebih baik farming real.",
    "Tweet lo hari ini bisa jadi tabungan cuan minggu depan.",
    "Orang sabar pantang nyerah. Hunter sejati pantang skip.",
    "Mending gagal karena nyoba, daripada nyesel karena skip.",
    "Lo butuh cuma 1 proyek legit buat balikin semuanya.",
    "Rezeki lo mungkin ke-10 form, tapi lo harus mulai dari form pertama.",
    "Lo bukan farming buat dapet 1 token, tapi buat buka pintu rezeki baru.",
    "Bukan karena lo nggak bisa, tapi karena lo belum cukup niat.",
    "Duit bisa dicari, tapi snapshot nggak bisa diulang.",
    "Males sejam = lost opportunity 1 ETH. Gasken terus!",
    "Lo sibuk nyari alasan, orang lain sibuk nyari alokasi.",
    "Nggak ikut snapshot? Salah sendiri. Siapa suruh mager?",
    "Project-nya ngasih jutaan, lo malah ngasih alasan.",
    "Waktu lo scroll TikTok, orang lain farming ratusan akun.",
    "Rezeki nggak datang ke yang niat rebahan.",
    "Yang lo butuh bukan motivasi, tapi mental baja buat gas tiap hari.",
    "Snapshot nggak akan nungguin yang insecure.",
    "Males satu hari, nyesel satu season.",
    "Orang sibuk bikin wallet baru, lo sibuk mikirin 'worth it nggak ya?'.",
    "Tweet 3 detik, eligible 3 juta. Tapi lo lebih milih scroll drama.",
    "Konsisten itu berat, tapi jauh lebih ringan dari rasa nyesel pas nggak dapet.",
    "Setiap klik itu bukan capek, itu investasi cuan masa depan.",
    "Nunggu mood datang? Airdrop-nya keburu listing.",
    "Project baru rilis, bukan buat ditonton tapi dikerjain.",
    "Lo bisa ngabisin 2 jam nge-game, tapi ngisi 1 form aja ogah?",
    "Lo ngiri liat orang dapet 5K? Dia gas tiap hari, lo baru mulai pas viral.",
    "Ngarep cuan kayak mereka? Kerja kayak mereka dulu.",
    "Skill lo udah cukup, yang kurang cuma konsistensi dan niat.",
    "Bukan nggak bisa, lo aja yang kebanyakan mikir dan mager.",
    "Setiap lo ragu, ingat: snapshot itu nggak pernah ngasih second chance.",
    "Yang dapet cuan bukan yang banyak gaya, tapi banyak gas.",
    "Airdrop itu bukan soal hoki, tapi soal siapa yang bener-bener niat.",
    "Pas orang dapet alokasi gede, lo masih nanya: ‘worth it gak ya project ini?’",
    "Banyak yang pengen hasilnya, tapi gak sanggup jalanin prosesnya.",
    "Mental kaya itu dimulai dari disiplin farming hari ini.",
    "Hunter sejati ngerjain bukan karena semangat, tapi karena tanggung jawab ke masa depan.",
    "Farm dulu, liburan menyusul. Gaskan tiap hari!"
]

def kirim_motivasi():
    bot = Bot(token=TOKEN)
    motivasi = random.choice(motivasi_list)
    tanggal = datetime.now().strftime("%Y-%m-%d")
    message = f"{motivasi}"
    
    if THREAD_ID:
        bot.send_message(chat_id=CHAT_ID, message_thread_id=int(THREAD_ID), text=message)
    else:
        bot.send_message(chat_id=CHAT_ID, text=message)

if __name__ == "__main__":
    kirim_motivasi()