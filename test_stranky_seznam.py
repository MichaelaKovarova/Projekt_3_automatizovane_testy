#otevření okna pro přihlášení do emailu
def test_email(page):
    with page.expect_popup() as popup:
        page.get_by_text("Přihlásit se").click()

    login_page = popup.value
    login_page.wait_for_load_state()

    assert login_page.url.startswith("https://login.szn.cz")

#test načtení mapy     
def test_map(page):   
    with page.expect_popup() as popup:
        page.get_by_role("link", name="Mapy").click()
    
    new_page = popup.value
    new_page.wait_for_load_state("networkidle")
    assert popup.value.url.startswith("https://mapy.com")
 

 
 #test vyhledávání na stránce https://www.seznam.cz/ 
def test_vyhledavani(page):
    page.click('[data-title="Internet"]')
    text_input = page.locator(".search-form__input")
    text_input.fill("školní prázdniny")

    button = page.locator('[data-dot="search-button"]')
    button.press("Enter")

    assert page.url.startswith("https://search.seznam.cz/")
