notebook_name= 'IDL_Project_v1'

!apt-get install texlive texlive-xetex texlive-latex-extra pandoc > /dev/null 2>&1
!pip install pypandoc > /dev/null 2>&1
from google.colab import drive
drive.mount('/content/drive')
!cp 'drive/My Drive/Colab Notebooks/'$notebook_name'.ipynb' ./

!jupyter nbconvert --to PDF $notebook_name'.ipynb' > /dev/null 2>&1
!echo "pdf file generated"
!ls -la
!cp './'$notebook_name'.pdf' 'drive/My Drive/Colab Notebooks'
