from django.shortcuts import render
from .utils import get_recommendations
# Create your views here.
def home(request):
    results = None
    cluster = None
    
    if request.method == "POST":
        # Get values from sliders
        user_features = [
            float(request.POST.get('nature')),
            float(request.POST.get('adventure')),
            float(request.POST.get('culture')),
            float(request.POST.get('altitude')),
        ]
        
        results, cluster = get_recommendations(user_features)

    return render(request, 'app/index.html', {'results': results, 'cluster': cluster})