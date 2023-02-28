class elem():
    base_url = "https://opensource-demo.orangehrmlive.com/"
    location_url = "https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewLocations"
    username = "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input"
    password = "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input"
    btn_login = "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button"
    menu_admin = "//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a"
    dropdown = "//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[3]/span"
    dp_location = "//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[3]/ul/li[2]/a"
    header = "//*[@id='app']/div[1]/div[1]/header/div[1]/div[1]/span"
    header_loct = "//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[1]/div[1]"


    #btn
    btn_add = "//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[1]/div/button"
    btn_save = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[3]/button[2]"
    btn_cancel = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[3]/button[1]"
    btn_edit = "//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[1]/div/div[7]/div/button[2]"
    modal = "//*[@id='app']/div[3]/div/div/div"

    #add data
    name = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div/div/div[2]/input"
    city = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[1]/div/div[2]/input"
    province = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[2]/div/div[2]/input"
    zip = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[3]/div/div[2]/input"
    country = "oxd-select-text-input"
    phone = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[5]/div/div[2]/input"
    fax = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[6]/div/div[2]/input"
    address = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[7]/div/div[2]/textarea"
    notes = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[8]/div/div[2]/textarea"


    #respon add data
    req_name = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div/div/span"
    req_country = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[4]/div/span"
    val_phone = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[5]/div/span"
    val_fax = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[6]/div/span"
    # alert = "oxd-text oxd-text--p oxd-text--toast-message oxd-toast-content-text" 
    # alert = "//*[@id='oxd-toaster_1']" 
    alert = "//*[@id='oxd-toaster_1']/div/div[1]/div[2]/p[2]"
# <p class="oxd-text oxd-text--p oxd-text--toast-message oxd-toast-content-text" data-v-7588b244="" data-v-89ccd62c="">Successfully Saved</p>
# //*[@id="oxd-toaster_1"]/div/div[1]/div[2]/p[2]

    #search data
    btn_search = "//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]"
    btn_reset = "//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[1]"
    s_name = "//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/input"
    s_city = "//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/input"
    s_country = "oxd-select-text-input"
    h_name = "//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div/div/div[2]/div"
    h_city = "//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div/div/div[3]/div"
    h_country = "//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[2]/div/div[4]/div"
    resp_country = "oxd-text oxd-text--span"
    resp_no_found = "//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[2]/div/span"

    #edit data
    # btn_edit_save = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[3]/button[2]"
    # btn_edit_cancel = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[3]/button[1]"
    # e_name = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div/div/div[2]/input"
    # e_city = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[1]/div/div[2]/input"
    # e_province = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[2]/div/div[2]/input"
    # e_zip = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[3]/div/div[2]/input"
    # e_country = "oxd-select-text-input"
    # e_phone = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[5]/div/div[2]/input"
    # e_fax = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[6]/div/div[2]/input"
    # e_address = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[7]/div/div[2]/textarea"
    # e_notes = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[8]/div/div[2]/textarea"

    #respon edit data
    # e_req_name = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div/div/span"
    # e_req_country = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[4]/div/span"
    # e_val_phone = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[5]/div/span"
    # e_val_fax = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[6]/div/span"
    # e_alert_success = "//*[@id='oxd-toaster_1']" 


    #delete
    btn_delete = "//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[1]/div/div[7]/div/button[1]"
    c_delete = "//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[2]/div/div[1]/div"
    all_delete = "//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[1]/div/div[1]/div"
    btn_selected ="//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[2]/div/div/button"
    btn_yes_delete = "//*[@id='app']/div[3]/div/div/div/div[3]/button[2]"
    btn_no_cancel = "//*[@id='app']/div[3]/div/div/div/div[3]/button[1]"
