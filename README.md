# Mypy Issue

Error: `api/serializers.py:10: error: Incompatible types in assignment (expression has type "CharField", base class "Field" defined the type as "Callable[..., Any] | str | None")  [assignment]`

Run: `make mypy`

If you edit `api/serializers.py` and comment out line 10 and uncomment 11, the error dissappears.
