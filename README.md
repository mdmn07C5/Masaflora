# Masaflora
Website for restaurants (or anything you can catalogue and customize to order really)
 - Display menus for each store
 - Customize order
 - Checkout (paypal, stripe)

## Set up
### Install and activate venv
```
$python -m venv .venv
$.venv/bin/Activate 
```

### Install dependencies
```
$pip install -r requirements.txt
```

### Make migrations
```
$make makemigrations
```

### Run migrations
```
$make migrate
```

## Run Development server
```
$make run
```


