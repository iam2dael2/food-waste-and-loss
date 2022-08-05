import numpy as np
import streamlit as st
import pandas as pd
import altair as alt
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(layout='wide')
st.image(
    './header.jpg',
    caption="Indonesia memproduksi sampah makanan hingga mencapai 115-184 kilogram per kapita per tahun selama tahun 2000-2019 (Bappenas, 2021)",
    width=1080)
st.title("Food Waste and Loss Terus Memperparah Indonesia, 59 Persen Masyarakat Indonesia Menyatakan Bencana Tersebut Tidak Mengancam")
st.caption("Kerugian ekonomi dan lingkungan selalu membebani Indonesia. Produksi sampah makanan di Indonesia diperkirakan mencapai 23-48 juta ton/tahun. Pemerintah telah melancarkan beberapa program untuk meminimalisir Food Waste and Loss. Akan tetapi, kesadaran dan perhatian masyarakat Indonesia akan masalah tersebut relatif rendah.")
# Latar Belakang (Lead)
st.text('"Habisin makanannya, kalau engga nanti mubazir"')
st.markdown('Ucapan tersebut mungkin pernah kita dapatkan dari orang tua. Hal tersebut mengajarkan kita untuk menghargai apa yang kita makan. Terkadang, kita terlintas untuk **lebih baik membuangnya** karena sudah tidak bisa lagi menampung makanan yang sudah diberikan. Secara tidak langsung, pembuangan sampah makanan secara masif berdampak kepada kondisi ekonomi, lingkungan, dan gizi. Sayangnya, kesadaran masyarakat Indonesia akan masalah tersebut tergolong rendah.')
# Lead Lanjutan
st.text('Tahukah kamu?')
flw = pd.read_csv('./Data/flw.csv')
data = pd.melt(flw, id_vars=["nama_alias"])
text1, _, chart1 = st.columns([2,1,5])
with chart1:
    st.subheader("Produksi Sampah Makanan Negara G20 (2021)")
    # Horizontal stacked bar chart
    x = data['nama_alias'].values
    fig = px.bar(
        data,
        x="value", 
        y="nama_alias", 
        color="variable",
        labels={'nama_alias': 'Negara', 'value': 'Total Produksi Sampah Makanan (kg per orang per tahun)'},
        category_orders={"nama_alias": ["Arab Saudi", "Amerika Serikat", "Meksiko", "Turki", "Perancis", "Australia", "Tiongkok", "Indonesia", 'Kanada', "Argentina", "Korea Selatan", "Brasil", "Jerman", "Britania Raya", "Italia", "India", "Jepang", "Afrika Selatan", "Rusia"]},)
    fig.update_layout(barmode='stack', xaxis={'categoryorder': 'total ascending'})
    st.plotly_chart(fig)
    st.caption('Sumber: Barilla Center Food and Nutritions, 2021')
with text1:
    st.write('')
    st.write('')
    # Tambahin lagi kalimatnya, entah memperjelas Indonesia peringkat 7 dan rincian2 sampahnya kg/orang/tahun
    st.markdown(
    '''
    Berdasarkan **Barilla Center Food and Nutritions (2021)**, 
    **Indonesia** termasuk salah satu dari 10 besar negara G20 dalam hal membuang makanan.

    Dalam hal ini, **Indonesia** menduduki **peringkat ketujuh sebagai negara G20 yang memproduksi sampah makanan terbanyak**.
    Berikut merupakan total produksi sampah makanan di Indonesia berdasarkan sumber sampah terbanyak:
    - Rumah Tangga: 77 kg per orang per tahun
    - Restoran: 28 kg per orang per tahun
    - Retail: 16 kg per orang per tahun
    ''')
st.text('')
st.markdown(
    '''
    Nyatanya, sampah rumah tangga di Indonesia mencapai **lebih dari 2 kali lipat** daripada sampah 
    pasar tradisional **(Kementerian Lingkungan Hidup dan Kehutanan, 2020)**. Maka dari itu, pihak 
    rumah tangga harus lebih bijaksana dalam memasak makanan dengan porsi yang secukupnya. Selain itu, 
    sampah makanan terbanyak di Indonesia pada peringkat ke- 1 dan 2 berturut-turut adalah sayuran dan 
    nasi (The Economist Intelligence Unit, Bappenas, Surplus, Global Hunger Index 2021). Hal ini berarti 
    **sampah makanan yang diproduksi paling banyak terdapat pada sektor pertanian**.
    '''
)

# Body 1
# Komposisi Sampah Nasional
komposisi = pd.read_csv('./Data/komposisi.csv')
# Sampah Makanan
sampah = pd.read_csv('./Data/sampah_makanan.csv')
# Gabungan Keduanya
chart1, chart2 = st.columns(2)
with chart1:
    st.subheader("Komposisi Sampah Nasional Berdasarkan Sumber Sampah (2020)")
    old_labels = komposisi['Komposisi'].values
    sizes = komposisi['Persentase'].values
    labels = []
    for label, size in zip(old_labels, sizes):
        labels.append(f'{label} ({size}%)')
    explode = [0 if i != komposisi['Persentase'].max() else 0.1 for i in komposisi['Persentase']]

    fig1, ax1 = plt.subplots(figsize=(10,8))
    patches = ax1.pie(sizes, explode=explode, shadow=True, startangle=90)
    ax1.legend(patches[0], labels, loc="upper left", bbox_to_anchor=(0.85, 1.0), fontsize=16)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    st.pyplot(fig1)
    st.caption('Sumber: Kementerian Lingkungan Hidup dan Kehutanan')
with chart2:
    st.subheader("Sampah Makanan Terbanyak di Indonesia (2021)")
    sampah = sampah.sort_values('Persentase', ascending=False)
    fig1, ax1 = plt.subplots(figsize=(10,6.3))
    sns.set_palette("Paired")
    sns.set_theme(style="whitegrid")
    sns.barplot(
        data=sampah,
        x="Persentase",
        y="Sampah makanan",
        ax=ax1
    )
    ax1.set_xlabel('Persentase (%)', fontsize=16)
    ax1.set_ylabel('Sampah Makanan', fontsize=16)
    st.pyplot(fig1, use_container_width=True)
    st.caption('Sumber: The Economist Intelligence Unit, Bappenas, Surplus, Global Hunger Index 2021')

st.markdown(
    '''
    Menurut hasil penelitian Food Lost and Waste (FWL) Waste4Change, sampah makanan Indonesia
    mencapai total 48 juta ton dalam setahun. Jumlah makanan tersebut setara dengan pemberian
    makanan sebanyak 125 juta orang untuk mengentaskan kemiskinan dan penanganan stunting di Indonesia.
    Ironis sekali, tingkat kelaparan Indonesia berada peringkat ke-3 di Asia Tenggara (2021). Terlebih
    lagi, Food Waste and Loss (FWL) memberikan dampak negatif yang sangat signifikan terutama bagi
    Indonesia, diantaranya:
    - Dampak Efek Rumah Kaca
    - Dampak Ekonomi
    - Dampak Gizi
    '''
)

# Pilih Dampak
option = st.selectbox(
    "Pilih dampak yang ingin diketahui untuk dijelaskan lebih lanjut",
    ("Dampak Efek Rumah Kaca", "Dampak Ekonomi", "Dampak Gizi"))

# Body 2 Dampak Efek Rumah Kaca
if option == "Dampak Efek Rumah Kaca":
    # Timbulan FLW Nasional Tahun 2000-2019 per Tahap Rantai Pasok Pangan (dalam Juta Ton)
    timbulan = pd.read_csv('./Data/timbulan.csv').set_index('Category')
    # Kontribusi 5 Tahap Rantai Pasok Pangan terhadap Total Emisi GRK FLW per Tahun (dalam MT CO2-ek)
    kontribusi = pd.read_csv('./Data/kontribusi.csv').set_index('Category')

    chart1, text1 = st.columns(2)
    with chart1:
        st.subheader("Timbulan Food Waste and Loss (FLW) Nasional Tahun 2000-2019 Per Tahap Rantai Pasok Pangan (dalam Juta Ton)")
        st.bar_chart(timbulan)
        st.caption("Sumber: Kementerian Perencanaan Pembangunan Nasional/Bappenas")
    with text1:
        for i in range(12):
            st.write('')
        st.markdown(
            '''
            Berdasarkan grafik di samping, diperoleh tahap **Konsumsi** menyebabkan timbulan Food Waste
            and Loss di Indonesia paling banyak pada rantai pasok pangan dengan total 19,413 juta ton (2019).
            Kemudian, disusul oleh tahap **Produksi** yang memberikan kontribusi pada timbulan Food Waste and 
            Loss di Indonesia sebesar 11,18 juta ton (2019)
            '''
        )
    st.markdown(
        '''
        Timbulan FLW di tahapan rantai pasok yang semakin panjang akan memiliki beban emisi yang lebih 
        besar dibandingkan beban emisi timbulan FLW yang timbul pada tahapan sebelumnya. Hal ini karena 
        beban emisi di rantai pasok yang semakin dekat dengan akhir hidup (end-of-life) mencakup beban 
        emisi dari tahapan-tahapan sebelumnya.

        Berdasarkan kajian oleh Bappenas,  total potensi dampak pemanasan global yang dihasilkan dari 
        FLW di Indonesia selama 20 tahun terakhir diestimasikan sebesar 1.702,9 Mton CO2-ek atau **setara 
        dengan 7,29% rata-rata emisi Gas Rumah Kaca (GRK) di Indonesia selama 20 tahun**.
        '''
    )
    st.write('')
    text2, chart2 = st.columns(2)
    with text2:
        for i in range(8):
            st.write('')
        st.markdown(
            '''
             Selama tahun 2000-2019, dampak pemanasan global mengalami titik puncak pada **tahun 2018**.
             Kontribusi total emisi Gas Rumah Kaca oleh FLW terbanyak terjadi pada **tahap Konsumsi**.
             
             **Tahap Konsumsi memberi kontribusi lebih banyak daripada akumulasi total emisi pada 4 tahap
             lainnya**. 
            '''
        )
    with chart2:
        st.subheader("Kontribusi 5 Tahap Rantai Pasok Pangan terhadap Total Emisi Gas Rumah Kaca FLW per Tahun (dalam MT CO2-ek)")
        st.bar_chart(kontribusi)
        st.caption("Sumber: Kementerian Perencanaan Pembangunan Nasional/Bappenas")

# Body 3 Dampak Ekonomi 
elif option == 'Dampak Ekonomi':
    # Perbandingan % FLW terhadap Kehilangan Ekonomi pada 5 Sektor Pangan
    sektor_5 = pd.read_csv('./Data/flw_lima.csv')
    # Perbandingan % FLW terhadap Kehilangan Ekonomi pada 11 Sektor Pangan
    sektor_11 = pd.read_csv('./Data/flw_sebelas.csv')

    # Catatan: Pakai Select Box, terus Pake Scatter Plot
    st.markdown(
        '''
        Menurut Bappenas (2021), besarnya timbulan FLW di Indonesia pada tahun 2000–2019 yang mencapai 
        23–48 juta ton/tahun berdampak pada terjadinya kehilangan ekonomi yaitu sebesar 213–551 triliun 
        rupiah/tahun atau setara dengan 4%-5% PDB Indonesia/tahun. Kehilangan ekonomi sangat mungkin untuk berpotensi lebih besar, 
        karena data yang digunakan dalam perhitungan kehilangan ekonomi menggunakan data harga pangan 
        yang tersedia yaitu 64-88 komoditas dari total 146 komoditas yang terdapat di Neraca Bahan 
        Makanan (NBM).
        '''
    )
    option = st.selectbox("Potensi Kehilangan Ekonomi di Indonesia Akibat FLW", ('5 Sektor Pangan', '11 Sektor Pangan'))
    if option == '5 Sektor Pangan':
        chart1, _, text1 = st.columns([2,2,2])
        with chart1:
            st.subheader('Perbandingan % FLW terhadap Kehilangan Ekonomi pada 5 Sektor Pangan')
            plot = px.scatter(sektor_5, x="Kehilangan Ekonomi", y="Persentase FLW", color="Sektor")
            st.plotly_chart(plot)
            st.caption("Sumber: Kementerian Perencanaan Pembangunan Nasional/Bappenas")
        with text1:
            for i in range(11):
                st.write('')
            st.markdown(
                '''
                Tanaman pangan memiliki nilai kehilangan ekonomi paling tinggi sebesar 56.88 triliun
                rupiah per tahun, meskipun persentase FLW relatif rendah.
                '''
            )
            for i in range(2):
                st.write('')
            st.markdown(
                '''
                Tanaman hortikultura memiliki nilai persentase FLW yang paling tinggi, serta beriringan
                dengan nilai kehilangan ekonomi yang relatif tinggi. Namun, kehilangan ekonomi tanaman 
                hortikultura tidak sebesar tanaman pangan.
                '''
            )
    else:
        chart2, _, text2 = st.columns([2,2,2])
        with chart2:
            st.subheader('Perbandingan % FLW terhadap Kehilangan Ekonomi pada 11 Sektor Pangan')
            plot = px.scatter(sektor_11, x="Kehilangan Ekonomi", y="Persentase FLW", color="Sektor")
            st.plotly_chart(plot)
            st.caption("Sumber: Kementerian Perencanaan Pembangunan Nasional/Bappenas")
        with text2:
            for i in range(9):
                st.write('')
            st.markdown(
                '''
                 Padi-padian memiliki nilai kehilangan ekonomi paling besar, namun jenis ini telah 
                 memiliki efisiensi proses yang baik sehingga proporsi padi-padian terbuang lebih kecil 
                 daripada proporsi padi-padian yang terkonsumsi.

                 Sementara itu, sayur-sayuran nilai kehilangan ekonominya tidak sebesar tanaman pangan/padi-padian, 
                 namun efisiensi prosesnya masih kurang baik sehingga menyebabkan proporsi sayur-sayuran terbuang 
                 sangat tinggi dibandingkan dengan sayur-sayuran yang terkonsumsi.
                '''
            )

# Body 4 Dampak Gizi
else:
    st.markdown(
        '''
        Berdasarkan Bappenas (2021), Timbulan FLW di Indonesia sebesar 23–48 juta ton/tahun pada tahun 2000-2019 menyebabkan 
        terjadinya kehilangan kandungan zat gizi, yakni  kehilangan kandungan energi, protein, 
        vitamin A, dan zat besi. Kehilangan energi akibat FLW pada tahun 2000-2019 sebesar 618 – 989 
        kkal/kapita/hari setara dengan porsi makan 61 – 125 juta orang per tahun. 
        Kandungan protein yang hilang dari FLW adalah sebesar 18 – 32 gram/kapita/hari atau setara 
        dengan kebutuhan protein 68 – 149 juta rata-rata orang per tahun. Angka ini mencakup 
        kebutuhan 30-50% populasi Indonesia). Sementara itu, kehilangan vitamin A akibat FLW adalah 
        sebesar 360 – 953 Ug RE/kapita/hari yang setara dengan kebutuhan vitamin A 134 – 441 juta orang 
        per tahun (63-166% populasi Indonesia). Terakhir, kandungan zat besi yang hilang dari FLW yaitu 
        sebesar 4 – 7 mg/kapita/hari atau setara dengan kebutuhan zat besi 96 – 189 juta orang per 
        tahun (46 – 72% populasi Indonesia).
        '''
    )
# Note: Narasi ae

# Body 5 Perhatian Masyarakat terhadap FWL
st.header("Perhatian Masyarakat Indonesia terhadap FWL")
st.markdown(
    '''
    Survei WWF yang dilakukan oleh YouGov ini melibatkan 11.000 orang di Indonesia, Australia, Brasil, Kolombia, India, Malaysia, Belanda, Afrika Selatan, Inggris dan Amerika Serikat. Negara-negara ini teridentifikasi menghadapi ancaman keamanan pangan terbesar karena kerusakan alam, sekaligus menyebabkan dampak kerusakan yang signifikan melalui produksi, konsumsi, atau limbah makanan.
    '''
)

jumlah = pd.read_csv('./Data/ancaman_all_jumlah.csv')
anc_all_persen = pd.read_csv('./Data/ancaman_all_persentase.csv')
tind_all_persen = pd.read_csv('./Data/tindakan_all_persentase.csv')
anc_ind_persen = pd.read_csv('./Data/ancaman_ind_persentase.csv')
tind_ind_persen = pd.read_csv('./Data/tindakan_ind_persentase.csv')
jumlah_ind = anc_ind_persen[['Pilihan', 'Jumlah']]
# Pakai st.columns (2) => ancaman_all_jumlah.csv & ancaman_all_persentase.csv
# Khusus ancaman_all_persentase => bakal dibuat selectbox khusus golongan umur
# NOTE PENTING: TEKANKAN BERAPA PERSEN YANG PILIH TIDAK PENTING & KURANG PENTING

# Ancaman All Jumlah
chart1, chart2 = st.columns(2)
with chart1:
    st.subheader("Survei Australia, Brasil, Kolombia, India, Indonesia, Malaysia, Belanda, Afrika Selatan, Inggris dan Amerika Serikat: Ancaman FWL terkait Lingkungan dan Planet Kita")
    old_labels = jumlah['Pilihan'].values
    sizes = jumlah['Jumlah'].values
    total = jumlah['Jumlah'].sum()
    labels = []
    for label, size in zip(old_labels, sizes):
        labels.append(f'{label}: {size} ({round(size/total*100, 2)}%)')
    explode = [0.1, 0.1, 0, 0]
    fig1, ax1 = plt.subplots(figsize=(10,8))
    patches = ax1.pie(sizes, explode=explode, shadow=True, startangle=90)
    ax1.legend(patches[0], labels, loc="upper left", bbox_to_anchor=(0.85, 1.0), fontsize=16)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    st.pyplot(fig1)
    st.caption('Sumber: WWF Indonesia')
with chart2:
    st.subheader("Survei Indonesia: Ancaman FWL terkait Lingkungan dan Planet Kita")
    st.write('')
    st.write('')
    st.write('')
    st.write('')
    old_labels = jumlah['Pilihan'].values
    sizes = jumlah_ind['Jumlah'].values
    labels = []
    for label, size in zip(old_labels, sizes):
        labels.append(f'{label} ({size}%)')
    explode = [0.1, 0.1, 0, 0]        
    fig1, ax1 = plt.subplots(figsize=(10,8))
    patches = ax1.pie(sizes, explode=explode,shadow=True, startangle=90)
    ax1.legend(patches[0], labels, loc="upper left", bbox_to_anchor=(0.85, 1.0), fontsize=16)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    st.pyplot(fig1)
    st.caption('Sumber: WWF Indonesia')

st.markdown(
    '''
    Berdasarkan grafik di atas, diperoleh bahwa negara-negara menganggap FWL mengancam kehidupan negara,
    terutama pada sektor pangan dan lingkungan. Sebanyak 39% responden dari negara-negara
    tersebut menganggap FWL tidak mengancam. Dalam hal ini, mayoritas masyarakat negara sudah melihat
    potensi buruk dari FLW.

    Akan tetapi, di dalam 39% responden tersebut, terdapat 59% responden di Indonesia yang menilai bahwa
    FWL tidak mengancam kesejahteraan negara. Dengan demikian, sebagian besar masyarakat Indonesia memiliki
    kesadaran yang kurang atas isu seperti hal ini.
    '''
)
option = st.selectbox('Pilih Golongan Umur untuk Melihat Tingkat Ancaman FWL yang Dipilih Sesuai Golongan Umur:', ('18-24', '25-34', '35-44', '45-54', '55+'))
chart1, chart2 = st.columns(2)
with chart1:
    st.subheader("Survei  Australia, Brasil, Kolombia, India, Indonesia, Malaysia, Belanda, Afrika Selatan, Inggris dan Amerika Serikat: Ancaman FWL terkait Lingkungan dan Planet Kita")
    old_labels = anc_all_persen['Pilihan'].values
    sizes = anc_all_persen[option].values
    labels = []
    for label, size in zip(old_labels, sizes):
        labels.append(f'{label} ({size}%)')
    explode = [0.1, 0.1, 0, 0]
    fig1, ax1 = plt.subplots(figsize=(10,8))
    patches = ax1.pie(sizes, explode=explode, shadow=True, startangle=90)
    ax1.legend(patches[0], labels, loc="upper left", bbox_to_anchor=(0.85, 1.0), fontsize=16)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    st.pyplot(fig1)
    st.caption('Sumber: WWF Indonesia')
with chart2:
    st.subheader("Survei Indonesia: Ancaman FWL terkait Lingkungan dan Planet Kita")
    st.write('')
    st.write('')
    st.write('')
    st.write('')
    old_labels = anc_ind_persen['Pilihan'].values
    sizes = anc_ind_persen[option].values
    total = jumlah_ind['Jumlah'].sum()
    labels = []
    for label, size in zip(old_labels, sizes):
        labels.append(f'{label} ({size}%)')
    explode = [0.1, 0.1, 0, 0]        
    fig1, ax1 = plt.subplots(figsize=(10,8))
    patches = ax1.pie(sizes, explode=explode,shadow=True, startangle=90)
    ax1.legend(patches[0], labels, loc="upper left", bbox_to_anchor=(0.85, 1.0), fontsize=16)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    st.pyplot(fig1)
    st.caption('Sumber: WWF Indonesia')

# Put here
anc_all_persen['Group'] = "Survei Multinegara"
anc_ind_persen['Group'] = "Survei Indonesia"

data = pd.concat([anc_all_persen, anc_ind_persen], axis=0)
data = data.loc[data['Pilihan'].isin(['Bukan Ancaman Sama Sekali', 'Bukan Ancaman yang Begitu Penting'])]

# Mengurutkan Kolom
data = data[['Pilihan', 'Group', '18-24', '25-34', '35-44', '45-54', '55+']]
data = pd.melt(data, id_vars=['Pilihan', 'Group'])

# Merubah nama
data.rename(columns={'variable': 'Umur', 'value': 'Persentase'}, inplace=True)

data.drop('Pilihan', axis=1, inplace=True)
data["total"] = data.groupby(['Group', 'Umur'])['Persentase'].transform(lambda x: sum(x))
data = data.drop_duplicates(subset=['Group', 'Umur', 'total']).reset_index(drop=True).drop('Persentase', axis=1)

ind = data.loc[data['Group'] == 'Survei Indonesia']['total'].values
all = data.loc[data['Group'] == 'Survei Multinegara']['total'].values
x = data['Umur'].unique()

col1, col2, col3 = st.columns([1,6,1])
with col2:
    fig = px.bar(data, x="Umur", y="total",
                color='Group', barmode='group',
                height=400, labels={'total': 'Persentase (%)'})
    st.subheader("Proporsi Masyarakat Negara yang Menganggap FLW Tidak Mengancam")
    st.plotly_chart(fig)
    st.caption("Sumber: Data Diolah")


# Hal yang sama juga berlaku buat ancaman_ind.persentase.csv & tindakan_ind_persentase.csv
# st.columns(2) terus golong berdasarkan umur
# NOTE PENTING: TEKANKAN KALAU SELURUH DUNIA ITU LEBIH DIKIT MILIH YG KURANG MENGANCAM, 
# TAPI TERNYATA SEBAGIAN BESAR YANG MILIH ITU ADALAH ORANG INDONESIA, YAITU 61%
st.markdown(
    '''
    Berdasarkan grafik di atas, bisa dilihat bahwa adanya **korelasi negatif antara umur dan pandangan 
    masyarakat dunia (Survei Australia, Brasil, Kolombia, India, Indonesia, Malaysia, Belanda, Afrika 
    Selatan, Inggris dan Amerika Serikat) bahwa FWL tidak atau kurang mengancam**.

    Sebaliknya, **terdapat korelasi positif antara umur dan pandangan masyarakat Indonesia bahwa FWL
    tidak atau kurang mengancam**.
    '''
)
# PROGRAM PEMERINTAH
st.header("Kolaborasi Antara Masyarakat dan Pemerintah Indonesia")
chart1, _, text1 = st.columns([4,1,2])
with chart1:
    st.subheader("Survei Negara Indonesia: Tindakan Pemerintah untuk Memastikan Setiap Orang Memiliki Cukup Makanan dan Mencegah Kerusakan Alam")
    old_labels = tind_ind_persen['Pilihan'].values
    sizes = tind_ind_persen['Pemerintah'].values
    labels = []
    for label, size in zip(old_labels, sizes):
        labels.append(f'{label} ({size}%)')
    fig1, ax1 = plt.subplots(figsize=(10,8))
    patches = ax1.pie(sizes, shadow=True, startangle=90)
    ax1.legend(patches[0], labels, loc="upper left", bbox_to_anchor=(0.85, 1.0), fontsize=16)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    st.pyplot(fig1)
    st.caption('Sumber: WWF Indonesia')
with text1:
    for i in range(11):
        st.write('')
    st.markdown(
        '''
        Berdasarkan survei yang ditujukan untuk masyarakat Indonesia, diperoleh 51% responden melihat
        adanya aksi pemerintah untuk menjamin kesetaraan pangan dan mencegah kerusakan alam.
        '''
    )
st.write(
    '''
    Berbagai upaya pemerintah telah dilakukan untuk merealisasi pengelolaan FLW. Akan tetapi, 
    kesungguhan pemerintah ini tidak akan berjalan baik tanpa kerja sama dari masyarakat Indonesia.
    Masalah tersebut tidak bisa diselesaikan hanya dengan sederet kebijakan pemerintah, tetapi 
    persoalan itu rupanya dapat pula dicegah melalui memperbaiki kebiasaan kita sendiri.
    '''
)
