import streamlit as st

st.set_page_config(layout="wide")

if 'kontrol' not in st.session_state:
    st.session_state['kontrol']={'kover':True, 'pertemuan1':False, 'pertemuan2':False, 'pertemuan3':False,
                                 'pertemuan4':False,'pertemuan5':False,'pertemuan6':False,'pertemuan7':False,
                                 'pertemuan8':False,'pertemuan9':False,'pertemuan10':False}

class tulisan:
    def __init__(self, tulis, ukuran):
        self.tulis = tulis
        self.ukuran = ukuran
    def tampilkan(self):
        st.components.v1.html(self.tulis,height=self.ukuran)

#===============================

def pendahuluan():
    tulisanHTML='<iframe src="https://martin-bernard26.github.io/landasanPendidikan/pendahuluan.html" width=100% height=1000px></iframe>'
    tampil = tulisan(tulisanHTML,1000)
    tampil.tampilkan()

def Pertemuan1():
    tulisanHTML='<iframe src="https://martin-bernard26.github.io/landasanPendidikan/Bab1.html" width=100% height=1000px></iframe>'
    tampil = tulisan(tulisanHTML,1000)
    tampil.tampilkan()

def Pertemuan2():
    tulisanHTML='<iframe src="https://martin-bernard26.github.io/landasanPendidikan/Bab2.html" width=100% height=1000px></iframe>'
    tampil = tulisan(tulisanHTML,1000)
    tampil.tampilkan()

def Pertemuan3():
    tulisanHTML='<iframe src="https://martin-bernard26.github.io/landasanPendidikan/pertemuan3.html" width=100% height=1000px></iframe>'
    tampil = tulisan(tulisanHTML,1000)
    tampil.tampilkan()

def Pertemuan4():
    tulisanHTML='<iframe src="https://martin-bernard26.github.io/landasanPendidikan/pertemuan4.html" width=100% height=1000px></iframe>'
    tampil = tulisan(tulisanHTML,1000)
    tampil.tampilkan()

def Pertemuan5():
    tulisanHTML='<iframe src="https://martin-bernard26.github.io/landasanPendidikan/pertemuan5.html" width=100% height=1000px></iframe>'
    tampil = tulisan(tulisanHTML,1000)
    tampil.tampilkan()

def Pertemuan6():
    tulisanHTML='<iframe src="https://martin-bernard26.github.io/landasanPendidikan/pertemuan6b.html" width=100% height=1000px></iframe>'
    tampil = tulisan(tulisanHTML,1000)
    tampil.tampilkan()

def Pertemuan7():
    tulisanHTML='<iframe src="https://martin-bernard26.github.io/landasanPendidikan/pertemuan7b.html" width=100% height=1000px></iframe>'
    tampil = tulisan(tulisanHTML,1000)
    tampil.tampilkan()

def Pertemuan8():
    tulisanHTML='<iframe src="https://drive.google.com/file/d/1qj1UonNudVcdgmGP3h0RXS3wTBYGiSuW/preview" width=100% height=1000px></iframe>'
    tampil = tulisan(tulisanHTML,1000)
    tampil.tampilkan()
    st.write("Pengumpulan Tugas Ujian Tengah Semester")
    tulisanHTML='<iframe src="https://martin-bernard26.github.io/landasanPendidikan/UTS.html" width=100% height=500px></iframe>'
    tampil = tulisan(tulisanHTML,500)
    tampil.tampilkan()

def Pertemuan9():
    tulisanHTML='<iframe src="https://martin-bernard26.github.io/landasanPendidikan/pertemuan8.html" width=100% height=1000px></iframe>'
    tampil = tulisan(tulisanHTML,1000)
    tampil.tampilkan()

def Pertemuan10():
    tulisanHTML='<iframe src="https://martin-bernard26.github.io/landasanPendidikan/teopen.html" width=100% height=1000px></iframe>'
    tampil = tulisan(tulisanHTML,1000)
    tampil.tampilkan()
#================================

if st.session_state['kontrol']['kover']:
    pendahuluan()
if st.session_state['kontrol']['pertemuan1']:
    Pertemuan1()
if st.session_state['kontrol']['pertemuan2']:
    Pertemuan2()
if st.session_state['kontrol']['pertemuan3']:
    Pertemuan3()
if st.session_state['kontrol']['pertemuan4']:
    Pertemuan4()
if st.session_state['kontrol']['pertemuan5']:
    Pertemuan5()
if st.session_state['kontrol']['pertemuan6']:
    Pertemuan6()
if st.session_state['kontrol']['pertemuan7']:
    Pertemuan7()
if st.session_state['kontrol']['pertemuan8']:
    Pertemuan8()
if st.session_state['kontrol']['pertemuan9']:
    Pertemuan9()
if st.session_state['kontrol']['pertemuan10']:
    Pertemuan10()

#===============================

if st.sidebar.button("Pendahuluan"):
    st.session_state['kontrol']={'kover':True, 'pertemuan1':False, 'pertemuan2':False,
                                 'pertemuan3':False,'pertemuan4':False,'pertemuan5':False,
                                 'pertemuan6':False,'pertemuan7':False,
                                 'pertemuan8':False,'pertemuan9':False,'pertemuan10':False}
    st.rerun()

if st.sidebar.button("Bab 1"):
    st.session_state['kontrol']={'kover':False, 'pertemuan1':True, 'pertemuan2':False,
                                 'pertemuan3':False,'pertemuan4':False,'pertemuan5':False,
                                 'pertemuan6':False,'pertemuan7':False,
                                 'pertemuan8':False,'pertemuan9':False,'pertemuan10':False}
    st.rerun()

if st.sidebar.button("Bab 2"):
    st.session_state['kontrol']={'kover':False, 'pertemuan1':False, 'pertemuan2':True,
                                 'pertemuan3':False,'pertemuan4':False,'pertemuan5':False,
                                 'pertemuan6':False,'pertemuan7':False,
                                 'pertemuan8':False,'pertemuan9':False,'pertemuan10':False}
    st.rerun()
if st.sidebar.button("Bab 3"):
    st.session_state['kontrol']={'kover':False, 'pertemuan1':False, 'pertemuan2':False,
                                 'pertemuan3':True,'pertemuan4':False,'pertemuan5':False,
                                 'pertemuan6':False,'pertemuan7':False,
                                 'pertemuan8':False,'pertemuan9':False,'pertemuan10':False}
    st.rerun()
if st.sidebar.button("Bab 4"):
    st.session_state['kontrol']={'kover':False, 'pertemuan1':False, 'pertemuan2':False,
                                 'pertemuan3':False,'pertemuan4':True,'pertemuan5':False,
                                 'pertemuan6':False,'pertemuan7':False,
                                 'pertemuan8':False,'pertemuan9':False,'pertemuan10':False}
    st.rerun()
if st.sidebar.button("Bab 5"):
    st.session_state['kontrol']={'kover':False, 'pertemuan1':False, 'pertemuan2':False,
                                 'pertemuan3':False,'pertemuan4':False,'pertemuan5':True,
                                 'pertemuan6':False,'pertemuan7':False,
                                 'pertemuan8':False,'pertemuan9':False,'pertemuan10':False}
    st.rerun()
if st.sidebar.button("Bab 6"):
    st.session_state['kontrol']={'kover':False, 'pertemuan1':False, 'pertemuan2':False,
                                 'pertemuan3':False,'pertemuan4':False,'pertemuan5':False,
                                 'pertemuan6':True,'pertemuan7':False,
                                 'pertemuan8':False,'pertemuan9':False,'pertemuan10':False}
    st.rerun()
if st.sidebar.button("Bab 7"):
    st.session_state['kontrol']={'kover':False, 'pertemuan1':False, 'pertemuan2':False,
                                 'pertemuan3':False,'pertemuan4':False,'pertemuan5':False,
                                 'pertemuan6':False,'pertemuan7':True,
                                 'pertemuan8':False,'pertemuan9':False,'pertemuan10':False}
    st.rerun()
if st.sidebar.button("Ujian Tengah Semester"):
    st.session_state['kontrol']={'kover':False, 'pertemuan1':False, 'pertemuan2':False,
                                 'pertemuan3':False,'pertemuan4':False,'pertemuan5':False,
                                 'pertemuan6':False,'pertemuan7':False,
                                 'pertemuan8':True,'pertemuan9':False,'pertemuan10':False}
    st.rerun()
if st.sidebar.button("Bab 8"):
    st.session_state['kontrol']={'kover':False, 'pertemuan1':False, 'pertemuan2':False,
                                 'pertemuan3':False,'pertemuan4':False,'pertemuan5':False,
                                 'pertemuan6':False,'pertemuan7':False,
                                 'pertemuan8':False,'pertemuan9':True,'pertemuan10':False}
    st.rerun()
if st.sidebar.button("Bab 9"):
    st.session_state['kontrol']={'kover':False, 'pertemuan1':False, 'pertemuan2':False,
                                 'pertemuan3':False,'pertemuan4':False,'pertemuan5':False,
                                 'pertemuan6':False,'pertemuan7':False,
                                 'pertemuan8':False,'pertemuan9':False,'pertemuan10':True}
    st.rerun()
