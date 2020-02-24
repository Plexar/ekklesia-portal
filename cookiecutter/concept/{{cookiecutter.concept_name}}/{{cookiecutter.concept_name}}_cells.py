from {{ cookiecutter.app_name }}.app import App
from {{ cookiecutter.app_name }}.concepts.{{ cookiecutter.app_name }}.cell.layout import LayoutCell
from {{ cookiecutter.app_name }}.concepts.{{ cookiecutter.app_name }}.cell.form import NewFormCell, EditFormCell
from {{ cookiecutter.app_name }}.database.datamodel import {{ cookiecutter.ConceptName }}
from {{ cookiecutter.app_name }}.permission import CreatePermission, EditPermission
#from .{{ cookiecutter.concept_name }}_helper import items_for_{{cookiecutter.concept_name}}_select_widgets
from .{{ cookiecutter.concept_names }} import {{ cookiecutter.ConceptNames }}


@App.cell({{ cookiecutter.ConceptNames }})
class {{ cookiecutter.ConceptNames }}Cell(LayoutCell):

    def {{ cookiecutter.concept_names }}(self):
        return list(self._model.{{ cookiecutter.concept_names }}(self._request.q))

    # Methods from this class can be called from the template.

    # Methods with only the self argument can be used without call parentheses and their result value is cached.
    def show_new_button(self):
        return self.options.get('show_new_button') and self._request.permitted_for_current_user(self._model, CreatePermission)


@App.cell({{ cookiecutter.ConceptName }})
class {{ cookiecutter.ConceptName }}Cell(LayoutCell):

    # Model attributes included here are available as variables in the template:
    # = name
    # model_properties = ['name']

    def show_edit_button(self):
        return self.options.get('show_edit_button') and self._request.permitted_for_current_user(self._model, EditPermission)


@App.cell({{ cookiecutter.ConceptNames }}, 'new')
class New{{ cookiecutter.ConceptName }}Cell(NewFormCell):
    pass

    # def _prepare_form_for_render(self):
        # By default, the form's prepare_for_render() method is called without arguments.
        # You can pass additional args, for example to set values for select fields like this:

        # items = items_for_{{cookiecutter.concept_name}}_select_widgets(self._model)
        # self._form.prepare_for_render(items)


@App.cell({{ cookiecutter.ConceptName }}, 'edit')
class Edit{{ cookiecutter.ConceptName }}Cell(EditFormCell):
    pass

    # def _prepare_form_for_render(self):
        # By default, all fields from the model as given by to_dict() are passed to the form.
        # You can customize the behaviour (inherited from the base class) here:

        # form_data = self._model.to_dict()
        # self.set_form_data(form_data)

        # By default, the form's prepare_for_render() method is called without arguments.
        # You can pass additional args, for example to set values for select fields like this:

        # items = items_for_{{cookiecutter.concept_name}}_select_widgets(self._model)
        # self._form.prepare_for_render(items)
