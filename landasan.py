import streamlit as st

st.set_page_config(layout="wide")

if 'kontrol' not in st.session_state:
    st.session_state['kontrol']={'kover':True, 'pertemuan1':False, 'pertemuan2':False, 'pertemuan3':False,
                                 'pertemuan4':False,'pertemuan5':False,'pertemuan6':False,'pertemuan7':False,
                                 'pertemuan8':False,'pertemuan9':False,'pertemuan10':False,'pertemuan11':False,
                                 'pertemuan12':False,'pertemuan13':False}

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

def Pertemuan11():
    tulisanHTML='<iframe src="https://martin-bernard26.github.io/landasanPendidikan/permasalahan.html" width=100% height=1000px></iframe>'
    tampil = tulisan(tulisanHTML,1000)
    tampil.tampilkan()

def Pertemuan12():
    menu  = st.tabs(['Beban Kognitif','Memory Kerja'])
    with menu[0]:
        tulisanHTML='<iframe src="https://drive.google.com/file/d/12nRSgRhXNhmAwOTiAb7l3jZMe7uGOlWh/preview" width=100% height=1000px></iframe>'
        tampil = tulisan(tulisanHTML,1000)
        tampil.tampilkan()
    with menu[1]:
        tulisanHTML='<iframe src="https://drive.google.com/file/d/1PG-qT0QgL5CtpbFMrzWe9xyefrkHyBDg/preview" width=100% height=1000px></iframe>'
        tampil = tulisan(tulisanHTML,1000)
        tampil.tampilkan()

def Pertemuan13():
    tulisanHTML='<iframe src="https://drive.google.com/file/d/10nQR4IrdRL_S86ej-m1USrD2f8B9GgiW/preview" width=100% height=1000px></iframe>'
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
if st.session_state['kontrol']['pertemuan11']:
    Pertemuan11()
if st.session_state['kontrol']['pertemuan12']:
    Pertemuan12()
if st.session_state['kontrol']['pertemuan13']:
    Pertemuan13()

#===============================

if st.sidebar.button("Pendahuluan"):
    st.session_state['kontrol']={'kover':True, 'pertemuan1':False, 'pertemuan2':False,
                                 'pertemuan3':False,'pertemuan4':False,'pertemuan5':False,
                                 'pertemuan6':False,'pertemuan7':False,
                                 'pertemuan8':False,'pertemuan9':False,'pertemuan10':False,'pertemuan11':False,
                                 'pertemuan12':False,'pertemuan13':False
                                 }
    st.rerun()

if st.sidebar.button("Bab 1"):
    st.session_state['kontrol']={'kover':False, 'pertemuan1':True, 'pertemuan2':False,
                                 'pertemuan3':False,'pertemuan4':False,'pertemuan5':False,
                                 'pertemuan6':False,'pertemuan7':False,
                                 'pertemuan8':False,'pertemuan9':False,'pertemuan10':False,'pertemuan11':False,
                                 'pertemuan12':False,'pertemuan13':False}
    st.rerun()

if st.sidebar.button("Bab 2"):
    st.session_state['kontrol']={'kover':False, 'pertemuan1':False, 'pertemuan2':True,
                                 'pertemuan3':False,'pertemuan4':False,'pertemuan5':False,
                                 'pertemuan6':False,'pertemuan7':False,
                                 'pertemuan8':False,'pertemuan9':False,'pertemuan10':False,'pertemuan11':False,
                                 'pertemuan12':False,'pertemuan13':False}
    st.rerun()
if st.sidebar.button("Bab 3"):
    st.session_state['kontrol']={'kover':False, 'pertemuan1':False, 'pertemuan2':False,
                                 'pertemuan3':True,'pertemuan4':False,'pertemuan5':False,
                                 'pertemuan6':False,'pertemuan7':False,
                                 'pertemuan8':False,'pertemuan9':False,'pertemuan10':False,'pertemuan11':False,
                                 'pertemuan12':False,'pertemuan13':False}
    st.rerun()
if st.sidebar.button("Bab 4"):
    st.session_state['kontrol']={'kover':False, 'pertemuan1':False, 'pertemuan2':False,
                                 'pertemuan3':False,'pertemuan4':True,'pertemuan5':False,
                                 'pertemuan6':False,'pertemuan7':False,
                                 'pertemuan8':False,'pertemuan9':False,'pertemuan10':False,'pertemuan11':False,
                                 'pertemuan12':False,'pertemuan13':False}
    st.rerun()
if st.sidebar.button("Bab 5"):
    st.session_state['kontrol']={'kover':False, 'pertemuan1':False, 'pertemuan2':False,
                                 'pertemuan3':False,'pertemuan4':False,'pertemuan5':True,
                                 'pertemuan6':False,'pertemuan7':False,
                                 'pertemuan8':False,'pertemuan9':False,'pertemuan10':False,'pertemuan11':False,
                                 'pertemuan12':False,'pertemuan13':False}
    st.rerun()
if st.sidebar.button("Bab 6"):
    st.session_state['kontrol']={'kover':False, 'pertemuan1':False, 'pertemuan2':False,
                                 'pertemuan3':False,'pertemuan4':False,'pertemuan5':False,
                                 'pertemuan6':True,'pertemuan7':False,
                                 'pertemuan8':False,'pertemuan9':False,'pertemuan10':False,'pertemuan11':False,
                                 'pertemuan12':False,'pertemuan13':False}
    st.rerun()
if st.sidebar.button("Bab 7"):
    st.session_state['kontrol']={'kover':False, 'pertemuan1':False, 'pertemuan2':False,
                                 'pertemuan3':False,'pertemuan4':False,'pertemuan5':False,
                                 'pertemuan6':False,'pertemuan7':True,
                                 'pertemuan8':False,'pertemuan9':False,'pertemuan10':False,'pertemuan11':False,
                                 'pertemuan12':False,'pertemuan13':False}
    st.rerun()
if st.sidebar.button("Ujian Tengah Semester"):
    st.session_state['kontrol']={'kover':False, 'pertemuan1':False, 'pertemuan2':False,
                                 'pertemuan3':False,'pertemuan4':False,'pertemuan5':False,
                                 'pertemuan6':False,'pertemuan7':False,
                                 'pertemuan8':True,'pertemuan9':False,'pertemuan10':False,'pertemuan11':False,
                                 'pertemuan12':False,'pertemuan13':False}
    st.rerun()
if st.sidebar.button("Bab 8"):
    st.session_state['kontrol']={'kover':False, 'pertemuan1':False, 'pertemuan2':False,
                                 'pertemuan3':False,'pertemuan4':False,'pertemuan5':False,
                                 'pertemuan6':False,'pertemuan7':False,
                                 'pertemuan8':False,'pertemuan9':True,'pertemuan10':False,'pertemuan11':False,
                                 'pertemuan12':False,'pertemuan13':False}
    st.rerun()
if st.sidebar.button("Bab 9"):
    st.session_state['kontrol']={'kover':False, 'pertemuan1':False, 'pertemuan2':False,
                                 'pertemuan3':False,'pertemuan4':False,'pertemuan5':False,
                                 'pertemuan6':False,'pertemuan7':False,
                                 'pertemuan8':False,'pertemuan9':False,'pertemuan10':True,'pertemuan11':False,
                                 'pertemuan12':False,'pertemuan13':False}
    st.rerun()
if st.sidebar.button("Bab 10"):
    st.session_state['kontrol']={'kover':False, 'pertemuan1':False, 'pertemuan2':False,
                                 'pertemuan3':False,'pertemuan4':False,'pertemuan5':False,
                                 'pertemuan6':False,'pertemuan7':False,
                                 'pertemuan8':False,'pertemuan9':False,'pertemuan10':False,'pertemuan11':True,
                                 'pertemuan12':False,'pertemuan13':False}
    st.rerun()
if st.sidebar.button("NeuroScience"):
    st.session_state['kontrol']={'kover':False, 'pertemuan1':False, 'pertemuan2':False,
                                 'pertemuan3':False,'pertemuan4':False,'pertemuan5':False,
                                 'pertemuan6':False,'pertemuan7':False,
                                 'pertemuan8':False,'pertemuan9':False,'pertemuan10':False,'pertemuan11':False,
                                 'pertemuan12':True,'pertemuan13':False}
    st.rerun()
if st.sidebar.button("Ujian Akhir Semester"):
    st.session_state['kontrol']={'kover':False, 'pertemuan1':False, 'pertemuan2':False,
                                 'pertemuan3':False,'pertemuan4':False,'pertemuan5':False,
                                 'pertemuan6':False,'pertemuan7':False,
                                 'pertemuan8':False,'pertemuan9':False,'pertemuan10':False,'pertemuan11':False,
                                 'pertemuan12':False,'pertemuan13':True}
    st.rerun()
