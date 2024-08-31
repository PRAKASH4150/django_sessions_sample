from django.shortcuts import render, redirect

def view_1(request):
   # Retrieve or generate data to pass to the template
    tab_id = request.GET.get('tab_id')
    
    if tab_id:
        request.session['tab_id'] = tab_id

    # Example data to pass to the template
    data_context = {
        'tab_id': tab_id,  # Passing the tab ID to the template
        'message': 'Welcome to the First Page!',  # A welcome message
        'user_name': 'John Doe',  # Dynamic user information
        'items': ['Item1', 'Item2', 'Item3']  # A list of items
    }

    # Render the template with the data context
    return render(request, 'view_1.html', data_context)


def view_2(request):
   # Retrieve or generate data to pass to the template
    tab_id = request.GET.get('tab_id')
    
    if tab_id:
        request.session['tab_id'] = tab_id

    # Example data to pass to the template
    data_context = {
        'tab_id': tab_id,  # Passing the tab ID to the template
        'message': 'Welcome to the Second Page!',  # A welcome message
        'user_name': 'John Doe',  # Dynamic user information
        'items': ['Item1', 'Item2', 'Item3']  # A list of items
    }

    # Render the template with the data context
    return render(request, 'view_2.html', data_context)


def view_3(request):
   # Retrieve or generate data to pass to the template
    tab_id = request.GET.get('tab_id')
    
    if tab_id:
        request.session['tab_id'] = tab_id

    # Example data to pass to the template
    data_context = {
        'tab_id': tab_id,  # Passing the tab ID to the template
        'message': 'Welcome to the Third Page!',  # A welcome message
        'user_name': 'John Doe',  # Dynamic user information
        'items': ['Item1', 'Item2', 'Item3']  # A list of items
    }

    # Render the template with the data context
    return render(request, 'view_3.html', data_context)