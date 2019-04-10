Platform Tour XBlock
===========
This XBlock provides a tour of the platform at the click of a button!

Installation
------------
To install the Platform Tour XBlock within your edX python environment, simply run this command:

```bash
$ pip install -r requirements.txt
```

Enabling in Studio
------------------
Go to `Settings -> Advanced Settings` and set `Advanced Module List` to `["platformtour"]`.

Usage
------------------
Once the Platform Tour XBlock is enabled in Studio, you should see it a new Component button labeled `Advanced`:

Click the `Advanced` button and you should see the Platform Tour XBlock listed.

After you've selected the Platform Tour XBlock, a default set of steps will be inserted into your unit.

Customization
-------------
The button label, introduction, and steps can both be customized by clicking the `Edit` button on the component.

The steps of the platform tour are respresented as a set of checkboxes. Users in studio can uncheck checkboxes to
prevent steps from being shown to users in the LMS.

v1 features and limitations
---------------------------
- Checkbox selections are saved as a list of keys.
- Making any changes in Studio (or just clicking the Save button for the component in Studio) saves the list of
keys to the database, which effectively "locks" the list.
- This means the "order" and "step selection" of the list is saved, and does not automatically update with new
versions of the xBlock.
- Changes to the values corresponding to the following keys: `title`, `element`, `intro`, and `position` in the
`default_steps.py` file **DO** get applied even if the xblock is saved into the database in Studio.
- However, the order and choice selection **DOES NOT** update. (i.e. if the xblock is updated to change the order
in which the steps are displayed or a new step is added.)
