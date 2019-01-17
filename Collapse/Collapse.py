class CollapsibleContainer(object):
    def __init__(self, container, collapse_button_locator_type, collapse_button_locator_value,
                 inner_container_locator_type, inner_container_locator_value):

        self.section = container
        self.collapse_button_locator = collapse_button_locator_type
        self.collapse_button_locator_value = collapse_button_locator_value

        self.inner_container_locator_type = inner_container_locator_type
        self.inner_container_locator_value = inner_container_locator_value

    @property
    def collapse_button(self):
        return self.section.find_element(self.collapse_button_locator, self.collapse_button_locator_value)

    @property
    def inner_container(self):
        return self.section.find_element(self.inner_container_locator_type, self.inner_container_locator_value)

    def is_inner_container_open(self):
        return 'in' in self.inner_container.get_attribute('class')

    def open_inner_container(self):
        if self.is_inner_container_open():
            return

        self.collapse_button.click()

    def close_inner_container(self):
        if not self.is_inner_container_open():
            return

        self.collapse_button.click()
