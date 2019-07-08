import pytesseract
from PIL import Image, ImageEnhance
import keyboard
from os import path
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-warp\tesseract.exe"



try:
    import obspython as obs
except:
    print("Initializing")

enabled = True

#def script_load(settings):
#    hotkey_id = obs.obs_hotkey_register_frontend("Set Neron Bar Trigger", "Neron Bar", neron_bar)
#    hotkey_save_array = obs.obs_data_get_array(settings, "neron_bar.trigger")
#    obs.obs_hotkey_load(hotkey_id, hotkey_save_array)
#    obs.obs_data_array_release(hotkey_save_array)



def script_update(settings):
    global source_name
    
    source_name = obs.obs_data_get_string(settings, "source")








def script_properties():
    props = obs.obs_properties_create()
    obs.obs_properties_add_text(props, "hotkey", "Trigger Key (WIP)", obs.OBS_TEXT_DEFAULT)


    p = obs.obs_properties_add_list(props, "source", "Text Source", obs.OBS_COMBO_TYPE_EDITABLE, obs.OBS_COMBO_FORMAT_STRING)
    sources = obs.obs_enum_sources()
    if sources is not None:
        for source in sources:
            source_id = obs.obs_source_get_id(source)
            if source_id == "text_gdiplus" or source_id == "text_ft2_source":
                name = obs.obs_source_get_name(source)
                obs.obs_property_list_add_string(p, name, name)

        obs.source_list_release(sources)


    obs.obs_properties_add_button(props, "button", "Reload", refresh_pressed)
    
    return props


def refresh_pressed(props, prop):
    global im_width
    global im_height
    global img
    PATH_img = path.expandvars(r'%TEMP%\snapshot.png')
    img = Image.open(path.expandvars(r'%TEMP%\snapshot.png'))
    im_width, im_height = img.size
    update_bar()
    print(title(), id(), maker(), likes(), plays())



def script_description():
    return "(Alpha) Neron Bar by Ripstikerpro"



def title(): #done
    x1 = im_width * 0.166
    y1 = im_height * 0.259
    x2 = im_width * 0.801
    y2 = im_height * 0.305
    title_img = img.crop((x1,y1,x2,y2))
    #title_img.show()
    title_text = pytesseract.image_to_string(title_img, lang="eng")
    return title_text


def id():
    x1 = im_width * 0.318
    y1 = im_height * 0.438
    x2 = im_width * 0.426
    y2 = im_height * 0.474
    id_img = img.crop((x1,y1,x2,y2))
    #id_img = id_img.convert('1', dither=Image.NONE)
    id_width, id_height = id_img.size
    id_img = id_img.resize((id_width*5,id_height*5), Image.ANTIALIAS)
    #id_img = ImageEnhance.Contrast(id_img).enhance(1.5)
    #id_img.show()
    id_text = pytesseract.image_to_string(id_img, lang="eng", config='--psm 10')
    return id_text

def maker(): #semidone
    x1 = im_width * 0.239
    y1 = im_height * 0.360
    x2 = im_width * 0.424
    y2 = im_height * 0.400
    maker_img = img.crop((x1,y1,x2,y2))
    maker_width, maker_height = maker_img.size
    maker_img = maker_img.resize((maker_width * 5, maker_height * 5), Image.NEAREST)
    maker_img = ImageEnhance.Contrast(maker_img).enhance(2.5)
    #maker_img.show()
    maker_text = pytesseract.image_to_string(maker_img, lang="eng", config='--psm 10')
    return maker_text


def likes(): #semidone
    x1 = im_width * 0.540
    y1 = im_height * 0.407
    x2 = im_width * 0.643
    y2 = im_height * 0.462
    likes_img = img.crop((x1,y1,x2,y2))
    likes_width, likes_height = likes_img.size
    likes_img = likes_img.resize((likes_width*4,likes_height*4), Image.NEAREST)
    likes_img = ImageEnhance.Contrast(likes_img).enhance(2.0)
    #likes_img.show()
    likes_text = pytesseract.image_to_string(likes_img, lang="eng", config='--psm 10 digits')
    return likes_text


def plays(): #semidone
    x1 = im_width * 0.540
    y1 = im_height * 0.462
    x2 = im_width * 0.643
    y2 = im_height * 0.504
    plays_img = img.crop((x1,y1,x2,y2))
    plays_width, plays_height = plays_img.size
    plays_img = plays_img.resize((plays_width*4,plays_height*4), Image.NEAREST)
    plays_img = ImageEnhance.Contrast(plays_img).enhance(2.0)
    #plays_img.show()
    plays_text = pytesseract.image_to_string(plays_img, lang="eng", config='--psm 13 digits')
    return plays_text


def update_bar():
    source = obs.obs_get_source_by_name(source_name)
    if source is not None:
        text = title() + "                                      Maker: " + maker() + "      Likes: " + likes() + "  Plays: " + plays() + "      " + id()
        
        settings = obs.obs_data_create()
        obs.obs_data_set_string(settings, "text", text)
        obs.obs_source_update(source, settings)
        obs.obs_data_release(settings)
    obs.obs_source_release(source)
