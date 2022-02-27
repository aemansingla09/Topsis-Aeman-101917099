from distutils.core import setup


setup(
    name = 'Topsis-Aeman-101917099',         
    version = '0.0.1',      
    license='MIT',        
    description = 'Calculate the topsis score for different models',   
    author = 'Aeman Singla',                  
    author_email = 'aemansingla09@gmail.com',     
    #url = 'https://github.com/user/reponame', 
    #download_url = 'https://github.com/user/reponame/archive/v_01.tar.gz',    
    keywords = ['Topsis','Aeman Singla'],  
    install_requires=[           
            'pandas',
        ],
    classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    py_modules=['Topsis_Aeman_101917099'],
    package_dir={'':'src'},
)
