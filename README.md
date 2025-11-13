# Code for `Primary Key Switch`

This is the repository for my [blog entry](https://fabianclemenz.github.io/posts/django-101-switching-primary-key-on-existing-models/) on switch from one Primary Key to another.

To set it up, run `pipenv install` and create the file `.env` with providing the `SECRET_KEY`.

## Initial Data

`0000_base_db_dump_before_pk_switch.json` contains a base dataset on which we can perform our migrations

`0001_db_dump_after_pk_switch.json` contains the data after the following migrations

### Step1 - add uuid field

Create the new UUID field on our wanted Model (`0002_testmodel_uuid.py`), fill unique uuids (`0003_set_unique_uuids`) and rework `null=True` to `unique=True` (`0004_set_unique_true_on_uuid`)

### Step 2 - add new ForeignKeys to other models

Create temporary FK field on other models which have already a FK relation to our TestModel, `null=True` (`0005_testforeignkeymodel_test_model_uuid`) is the key here, because we need to set the values directly in a migration
(`0006_uuid_fk_test_foreign_key_model`)

### Step 3 - add new Model for M2M

create a temporary Through Model for M2M relations (`0007_testthroughmodel_and_more`) and copy data

### Step 4 - delete old connections

remove old connections (`0009_remove_test_foreignkeymodel_test_model_and_more`)

### Step 5 - delete the db constrain an new FK fields

(`0010_alter_test_foreignkeymodel_test_model_uuid_and_more`)

### Step 6 - set new pk field on TestModel

set the uuid field as new pk (`0011_remove_testmodel_id_and_more`)

### Step 7 - rename fields, remove _uuid suffix

rename the fields and remove _uuid suffix - so these can be used as the fields before (`0012_rename_test_model_uuid_testforeignkeymodel_test_model_and_more`)

### Step 8 - remove unecessary options change related name

remove unecessary options and change related name to the normal value (`0013_alter_testforeignkeymodel_test_model_and_more`)

### MISC

if you don't want a ThroughModel you need to do the following 5 steps

#### Step 1 - add the "old" M2M

(`0014_testmanytomanymdoel_test_models_old`)

#### Step 2 - copy the values

(`0015_copy_m2m`)

#### Step 3 - delete the ThroughModel and M2M

(`0016_remove_testmanytomanymodel_test_models_and_more`)

#### Step 4 - rename the M2M

(`0017_rename_test_models_old_testmanytomanymodel_test_models`)

#### Step 5 - change back related_name

(`0018_alter_testmanytomanymodel_test_models`)
