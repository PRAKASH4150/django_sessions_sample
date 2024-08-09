from django.shortcuts import render, redirect

def view_1(request):
    tab_id = request.POST.get('tab_id')
    if tab_id:
        request.session[f'data_{tab_id}_view1'] = {'step1': f'data from view 1{tab_id}'}
    return render(request, 'view_1.html')

def view_2(request):
    tab_id = request.POST.get('tab_id')
    if tab_id:
        data = request.session.get(f'data_{tab_id}_view1')
        request.session[f'data_{tab_id}_view2'] = {'step2': f'data from view 2{tab_id}', 'prev_data': data}
    return render(request, 'view_2.html')

def view_3(request):
    tab_id = request.POST.get('tab_id')
    if tab_id:
        # Extract data for this specific tab
        data_view1 = request.session.get(f'data_{tab_id}_view1')
        data_view2 = request.session.get(f'data_{tab_id}_view2')
        # Pass the extracted data to the template context
        context = {
            'data_view1': data_view1,
            'data_view2': data_view2,
        }
    else:
        context = {
            'data_view1': None,
            'data_view2': None,
        }

    return render(request, 'view_3.html', context)