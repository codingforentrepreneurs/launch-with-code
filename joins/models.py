from django.db import models

# Create your models here.

class Join(models.Model):
	email = models.EmailField()
	friend = models.ForeignKey("self", related_name='referral', null=True, blank=True, on_delete=models.SET_NULL)
	ref_id = models.CharField(max_length=120, default='ABC', unique=True)
	ip_address = models.CharField(max_length=120, default='ABC')
	timestamp = models.DateTimeField(auto_now_add = True, auto_now=False)
	updated = models.DateTimeField(auto_now_add = False, auto_now=True)

	def __unicode__(self):
		return "%s" %(self.email)

	class Meta:
		unique_together = ("email", "ref_id",)


# class JoinFriends(models.Model):
# 	email = models.OneToOneField(Join, related_name="Sharer")
# 	friends = models.ManyToManyField(Join, related_name="Friend", \
# 										null=True, blank=True)
# 	emailall = models.ForeignKey(Join, related_name='emailall')

# 	def __unicode__(self):
# 		print "friends are ", self.friends.all()
# 		print self.emailall
# 		print self.email
# 		return self.email.email
#To see the guide on using south, go here: 
#https://github.com/codingforentrepreneurs/Guides/blob/master/using_south_in_django.md

