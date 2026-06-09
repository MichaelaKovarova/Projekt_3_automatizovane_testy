#test přesun na začátek stránky https://www.seznam.cz/ přes tlačítko
def test_scroll(page):
    locator = page.locator(".atm-scroll-up-button__icon")
    locator.scroll_into_view_if_needed()
    scroll_position = page.evaluate("window.scrollY")
    assert scroll_position == 0



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
    text_input = page.locator("#main-content > div.drag-and-drop > div.main-content > div > div > div > header > div > div > div > div.ogm-search > div > form > div > label > input")
    text_input.fill("školní prázdniny")

    button = page.locator('[data-dot="search-button"]')
    button.press("Enter")

    assert page.url.startswith("https://search.seznam.cz/")
