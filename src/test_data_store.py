import data_store as ds


def test_set():
    populate_kv_store()
    assert 'key1' in ds.get_kv_store()
    assert 'key2' in ds.get_kv_store()


def test_delete():
    populate_kv_store()
    assert 'key1' in ds.get_kv_store()
    ds.delete('key1')
    assert 'key1' not in ds.get_kv_store()


def test_display_max_vf_store():
    populate_kv_store()
    assert max(ds.get_vf_store(), key=ds.get_vf_store().get) == 'value'
    ds.delete('key1')
    assert max(ds.get_vf_store(), key=ds.get_vf_store().get) == 'value'
    ds.delete('key2')
    assert not ds.get_vf_store()


def test_is_json():
    assert ds.is_json('{"key": "value"}')
    assert not ds.is_json("{'key': 'value'}")
    assert not ds.is_json('not a json')


def test_decrement_vf_store():
    populate_kv_store()
    assert ds.get_vf_store().get('value') == 3
    ds.decrement_vf_store(ds.get_kv_store().get('key1'))
    assert ds.get_vf_store().get('value') == 2
    ds.decrement_vf_store(ds.get_kv_store().get('key2'))
    assert ds.get_vf_store().get('value') is None


def test_update_vf_store():
    ds.set('key1', 'a value')
    ds.update_vf_store(ds.get_kv_store().get(('key1')))
    assert ds.get_vf_store().get('a') == 1
    ds.update_vf_store(ds.get_kv_store().get(('key2')))
    assert ds.get_vf_store().get('value') == 3


# Helper functions
def populate_kv_store():
    ds.set('key1', 'a value')
    ds.set('key2', '{"nestedKey1": "nested value", "nestedKey2": {"nestederKey": "Double-nested value"}}')
