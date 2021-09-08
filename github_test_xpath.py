from pages.github import GithubMain


def test_github_main(browser):
    phones_page = GithubMain()
    phones_page.test_main_page(browser)
