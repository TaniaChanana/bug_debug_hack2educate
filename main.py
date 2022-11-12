def api(url, lang):
    import speech_recognition as sr 
    import moviepy.editor as mp
    from googletrans import Translator 
    from gtts import gTTS
    import os
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    import time
    from selenium.webdriver.chrome.options import Options
    from webdriver_manager.chrome import ChromeDriverManager
    import boto3


    #Downloading video from Youtube url
    options = Options()
    options.add_argument(f'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36')
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--disable-extensions")
    options.add_argument("--proxy-server='direct://'")
    options.add_argument("--proxy-bypass-list=*")
    options.add_argument("--start-maximized")
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--no-sandbox')
    options.add_argument("--enable-javascript")
    options.add_argument('--ignore-certificate-errors')
    options.add_argument("--incognito")
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

    download_dir = os.getcwd()
    profile = {"plugins.plugins_list": [{"enabled": False, "name": "Chrome PDF Viewer"}], # Disable Chrome's PDF Viewer
                "download.default_directory": download_dir}
    options.add_experimental_option("prefs", profile)

    website = "https://us.savefrom.net/"
    try:
        driver.get(website)
        mainHandle = driver.current_window_handle
    except Exception as e:
        print(e.args)
        driver.close()
        raise e

    driver.find_element(By.XPATH, "//input[@type='text']").send_keys(url)

    driver.find_element(By.XPATH, "//button[contains(text(), 'Download')]").click()
    time.sleep(2)

    driver.find_element(By.XPATH, "//a[contains(text(), 'Download')]").click()
    time.sleep(10)

    #Getting path of video
    for i in os.listdir(os.curdir):
        if i[-4::] == '.mp4':
            path = i
            break

    #Extracting audio from video
    clip = mp.VideoFileClip(path) 
    clip.audio.write_audiofile(r'converted.wav')

    #extracting text from audio and converting it to required language
    r = sr.Recognizer()
    audio = sr.AudioFile("converted.wav")

    with audio as source:
        audio_file = r.record(source)
    result = r.recognize_google(audio_file)

    dic = ('afrikaans', 'af', 'albanian', 'sq', 
       'amharic', 'am', 'arabic', 'ar',
       'armenian', 'hy', 'azerbaijani', 'az', 
       'basque', 'eu', 'belarusian', 'be',
       'bengali', 'bn', 'bosnian', 'bs', 'bulgarian',
       'bg', 'catalan', 'ca', 'cebuano',
       'ceb', 'chichewa', 'ny', 'chinese (simplified)',
       'zh-cn', 'chinese (traditional)',
       'zh-tw', 'corsican', 'co', 'croatian', 'hr',
       'czech', 'cs', 'danish', 'da', 'dutch',
       'nl', 'english', 'en', 'esperanto', 'eo', 
       'estonian', 'et', 'filipino', 'tl', 'finnish',
       'fi', 'french', 'fr', 'frisian', 'fy', 'galician',
       'gl', 'georgian', 'ka', 'german',
       'de', 'greek', 'el', 'gujarati', 'gu',
       'haitian creole', 'ht', 'hausa', 'ha',
       'hawaiian', 'haw', 'hebrew', 'he', 'hindi',
       'hi', 'hmong', 'hmn', 'hungarian',
       'hu', 'icelandic', 'is', 'igbo', 'ig', 'indonesian', 
       'id', 'irish', 'ga', 'italian',
       'it', 'japanese', 'ja', 'javanese', 'jw',
       'kannada', 'kn', 'kazakh', 'kk', 'khmer',
       'km', 'korean', 'ko', 'kurdish (kurmanji)', 
       'ku', 'kyrgyz', 'ky', 'lao', 'lo',
       'latin', 'la', 'latvian', 'lv', 'lithuanian',
       'lt', 'luxembourgish', 'lb',
       'macedonian', 'mk', 'malagasy', 'mg', 'malay',
       'ms', 'malayalam', 'ml', 'maltese',
       'mt', 'maori', 'mi', 'marathi', 'mr', 'mongolian',
       'mn', 'myanmar (burmese)', 'my',
       'nepali', 'ne', 'norwegian', 'no', 'odia', 'or',
       'pashto', 'ps', 'persian', 'fa',
       'polish', 'pl', 'portuguese', 'pt', 'punjabi', 
       'pa', 'romanian', 'ro', 'russian',
       'ru', 'samoan', 'sm', 'scots gaelic', 'gd',
       'serbian', 'sr', 'sesotho', 'st',
       'shona', 'sn', 'sindhi', 'sd', 'sinhala', 'si',
       'slovak', 'sk', 'slovenian', 'sl',
       'somali', 'so', 'spanish', 'es', 'sundanese',
       'su', 'swahili', 'sw', 'swedish',
       'sv', 'tajik', 'tg', 'tamil', 'ta', 'telugu',
       'te', 'thai', 'th', 'turkish',
       'tr', 'ukrainian', 'uk', 'urdu', 'ur', 'uyghur',
       'ug', 'uzbek',  'uz',
       'vietnamese', 'vi', 'welsh', 'cy', 'xhosa', 'xh',
       'yiddish', 'yi', 'yoruba',
       'yo', 'zulu', 'zu')

    lang = dic[dic.index(lang)+1]

    translator = Translator()
    text = translator.translate(result, dest=lang).text

    #converting translated text to audio
    speak = gTTS(text=text, lang=lang, slow=False)
    speak.save("captured_voice.mp3")

    #Adding translated audio to video
    clip = mp.VideoFileClip(path)
    audioclip = mp.AudioFileClip("captured_voice.mp3")
    videoclip = clip.set_audio(audioclip)
    videoclip.write_videofile("final.mp4")

    #Uploading dubbed video on s3 bucket
    s3 = boto3.resource('s3')
    upload_file = 'final.mp4'
    s3_client = boto3.client(
        's3',
        aws_access_key_id="AKIAXLEAGKOGX6KBSN5O",
        aws_secret_access_key="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"
    )
    s3.Bucket('bug-debug-h2e').upload_file(Key = upload_file, Filename = upload_file)
    url = f"https://bug-debug-h2e.s3.ap-south-1.amazonaws.com/{upload_file}"
    driver.quit()
    print(url)
    return url

#Passing link of youtube video and the desired language to be dubbed in
api('https://www.youtube.com/watch?v=h5gNSHcoVmQ', 'hindi')
