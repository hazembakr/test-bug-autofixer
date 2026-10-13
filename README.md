# test-bug-autofixer

Test repo with a deliberate bug for the bug-autofixer-agent end-to-end test.

## Bug

`process_user(None)` raises `TypeError: 'NoneType' object is not subscriptable`
because `get_user_name` doesn't check for None.

## Tests

```bash
python -m unittest test_user_service -v
```
