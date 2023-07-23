import streamlit as st
from streamlit_option_menu import option_menu

st.title('Menghitung Luas Bangun')

#bagian sidebar
with st.sidebar :
    selected = option_menu('Hitung Luas bangun', 
    ['Hitung Luas Persegi',
    'Hitung Luas Persegi Panjang',
    'Hitung Luas Segitiga'],
    default_index = 0)

#hitung luas persegi
if (selected == 'Hitung Luas Persegi') :
    st.title('Hitung luas persegi')

    col1, col2 = st.columns(2)

    with col1 :
        sisi_1 = st.number_input('Masukkan luas sisi 1', 0)

    with col2 :
        sisi_2 = st.number_input('Masukkan luas sisi 2', 0)
    
    hitung = st.button('Hitung')

    if hitung :
        sisi = sisi_1 * sisi_2
        st.write('Luas persegi = ', sisi)
        st.success(f'Perhitungan berhasil, hasilnya {sisi}')

#hitung luas persegi panjang
if (selected == 'Hitung Luas Persegi Panjang') :
    st.title('Hitung luas persegi panjang')

    panjang = st.number_input('Masukkan nilai panjang', 0)
    lebar = st.number_input('Masukkan nilai lebar', 0)
    hitung = st.button('Hitung')

    if hitung :
        luas = panjang * lebar
        st.write('Luas persegi panjang = ', luas)
        st.success(f'Perhitungan berhasil, hasilnya {luas}')


#hitung luas segitiga
if (selected == 'Hitung Luas Segitiga') :
    st.title('Hitung luas segitiga')

    alas = st.slider('Masukkan nilai alas', 0, 100)
    tinggi = st.slider('Masukkan nilai tinggi', 0, 100)
    hitung = st.button('Hitung')

    if hitung :
        luas = 0.5 * alas * tinggi
        st.write('Luas segitiga = ', luas)
        st.success(f'Perhitungan berhasil, hasilnya {luas}')


