import data_store as ds


def test_ds_set_and_delete():
    populate_data_store()
    assert 'key1' in ds.get_kv_store()
    assert 'nestederKey' in ds.get_kv_store().get('key2', {}).get('nestedKey2')
    assert 'nestedKey1' in ds.get_kv_store().get('key2')

    ds.ds_set(['key1', 'anotherKey'], 'anotherValue')
    assert not isinstance(ds.get_kv_store().get('key1'), str)

    ds.ds_delete(['key1'])
    assert 'key1' not in ds.get_kv_store()

    ds.ds_delete(['key2', 'nestedKey', 'nestederKey'])
    assert 'nestedKey2' in ds.get_kv_store().get('key2', {})

    ds.ds_delete(['key2'])
    assert not ds.get_kv_store()

    ds.ds_delete(['fake_key'])
    assert not ds.get_kv_store()


def test_display_max_vf_store():
    populate_data_store()
    assert max(ds.get_vf_store(), key=ds.get_vf_store().get) == 'value'
    ds.ds_delete(['key1'])
    assert max(ds.get_vf_store(), key=ds.get_vf_store().get) == 'value'
    ds.ds_delete(['key2', 'nestedKey2', 'nestederKey'])
    ds.ds_set(['key2', 'nestedKey2'], 'nested')
    assert max(ds.get_vf_store(), key=ds.get_vf_store().get) == 'nested'
    ds.ds_delete(['key2'])
    assert not ds.get_vf_store()


def test_decrement_vf_store():
    populate_data_store()
    assert ds.get_vf_store().get('value') == 3
    ds.decrement_vf_store(ds.get_kv_store().get('key1'))
    assert ds.get_vf_store().get('value') == 2
    ds.decrement_vf_store(ds.get_kv_store().get('key2'))
    assert ds.get_vf_store().get('value') is None


def test_increment_vf_store():
    ds.ds_set(['key1'], 'a value')
    ds.increment_vf_store(ds.get_kv_store().get(('key1')))
    assert ds.get_vf_store().get('a') == 1
    ds.increment_vf_store(ds.get_kv_store().get(('key2')))
    assert ds.get_vf_store().get('value') == 3


# Helper functions
def populate_data_store():
    ds.ds_set(['key1'], 'a value')
    ds.ds_set(['key2', 'nestedKey2', 'nestederKey'], 'Double-nested value')
    ds.ds_set(['key2', 'nestedKey1'], 'nested value')
