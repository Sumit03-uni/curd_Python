from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from crudOperation.forms import EmployeeForm
from crudOperation.models import Employee
# Create your views here.
def create(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'Employee created successfully!')
                return redirect('show')
            except Exception as e:
                messages.error(request, f'Error creating employee: {str(e)}')
    else:
        form = EmployeeForm()
    return render(request, 'index.html', {'form': form})

def show(request):
    try:
        employees = Employee.objects.all()
        return render(request, "show.html", {'employees': employees})
    except Exception as e:
        messages.error(request, f'Error fetching employees: {str(e)}')
        return render(request, "show.html", {'employees': []})

def edit(request, id):
    try:
        employee = get_object_or_404(Employee, id=id)
        form = EmployeeForm(instance=employee)
        return render(request, 'edit.html', {'form': form, 'employee': employee})
    except Exception as e:
        messages.error(request, f'Error loading employee: {str(e)}')
        return redirect('show')

def update(request, id):
    try:
        employee = get_object_or_404(Employee, id=id)
        if request.method == "POST":
            form = EmployeeForm(request.POST, instance=employee)
            if form.is_valid():
                form.save()
                messages.success(request, 'Employee updated successfully!')
                return redirect('show')
            else:
                messages.error(request, 'Please correct the errors below.')
        else:
            form = EmployeeForm(instance=employee)
        return render(request, 'edit.html', {'form': form, 'employee': employee})
    except Exception as e:
        messages.error(request, f'Error updating employee: {str(e)}')
        return redirect('show')

def destroy(request, id):
    try:
        employee = get_object_or_404(Employee, id=id)
        employee.delete()
        messages.success(request, 'Employee deleted successfully!')
    except Exception as e:
        messages.error(request, f'Error deleting employee: {str(e)}')
    return redirect('show') 
