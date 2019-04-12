# django-bug-21777
Reproduce Django bug 21777


## Requirements
`pip install django`

## Reproduce
Run the server and notice the shown error is the second one, not the primary.
Uncheck `DEBUG` to verify the same behaviour in the admin exception emailing.
