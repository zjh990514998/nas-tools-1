from lxml import etree
import re

class TestUtils:

    @staticmethod
    def clear_file_name(name):
        if not name:
            return None

        replacement_dict = {
            r"[*?\\/\"<>~|,，？]": "",
            r"[\s]+": " ",
        }

        cleaned_name = name
        for pattern, replacement in replacement_dict.items():
            cleaned_name = re.sub(pattern, replacement, cleaned_name, flags=re.IGNORECASE).strip()

        cleaned_name = cleaned_name.replace(":", "-").replace("：", "-")
        return cleaned_name

    @staticmethod
    def find_matching_tables_with_title(html):
        tree = etree.HTML(html)
        table_elements = tree.xpath('//table[contains(@class, "torrentname") and @width="100%"]')
        
        matching_tables = []
        for table_element in table_elements:
            title_element = table_element.xpath('.//a[contains(@title, "")]/@title')
            if title_element:
                matching_tables.append(title_element[0])
        
        return matching_tables

    @staticmethod
    def find_matching_tables_with_free(html):
        tree = etree.HTML(html)
        table_elements = tree.xpath('//img[contains(@class, "pro_free") and contains(translate(@alt, "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "abcdefghijklmnopqrstuvwxyz"), "free")]')

        matching_tables = []
        for table_element in table_elements:
            matching_tables.append(table_element.get('class'))
        
        return matching_tables

    @staticmethod
    def find_matching_tables_with_2xfree(html):
        tree = etree.HTML(html)
        table_elements = tree.xpath('//img[contains(translate(@class, "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "abcdefghijklmnopqrstuvwxyz"), "pro_2xfree") and contains(translate(@alt, "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "abcdefghijklmnopqrstuvwxyz"), "2xfree")]')

        matching_tables = []
        for table_element in table_elements:
            matching_tables.append(table_element.get('class'))
        
        return matching_tables
