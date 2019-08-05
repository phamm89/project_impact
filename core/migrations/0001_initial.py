# Generated by Django 2.2.4 on 2019-08-05 13:37

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('is_admin', models.BooleanField(default=False, verbose_name='admin status')),
                ('is_paired', models.BooleanField(default=False, verbose_name='paired status')),
                ('is_active', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('first_name', models.CharField(blank=True, help_text='Please enter your first name.', max_length=120)),
                ('family_name', models.CharField(blank=True, help_text='Please enter your family name.', max_length=120)),
                ('email_address', models.EmailField(blank=True, help_text='Please enter a valid email address.', max_length=254)),
                ('why', models.TextField(blank=True, help_text='Please briefly describe why you want to become a foster mentor.', max_length=200)),
                ('availability', models.TextField(blank=True, help_text='Please list the days and times you would be available to mentor.', max_length=200)),
                ('address', models.CharField(blank=True, help_text='Please enter your full address', max_length=80)),
                ('reference_name', models.CharField(blank=True, help_text='Please enter a professional reference.', max_length=30)),
                ('reference_phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, help_text="Please enter your professional reference's phone number.", max_length=128, region=None)),
                ('reference_name2', models.CharField(blank=True, help_text='Please enter a personal reference name.', max_length=30)),
                ('reference_phone2', phonenumber_field.modelfields.PhoneNumberField(blank=True, help_text="Please enter your personal reference's phone number.", max_length=128, region=None)),
                ('education', models.CharField(choices=[('High School / GED', 'High School / GED'), ('Some College', 'Some College'), ("Associate's Degree", "Associate's Degree"), ("Bachelor's Degree", "Bachelor's Degree"), ("Masters' Degree", "Master's Degree"), ('PhD', 'PhD'), ('None', 'None')], default='None', help_text='Please enter your highest level of education.', max_length=30)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter a resource category (e.g. Educational, Career)', max_length=200)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='core.Category')),
            ],
            options={
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Goal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=200, null=True)),
                ('completed', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(help_text='Please enter your first name.', max_length=120)),
                ('family_name', models.CharField(help_text='Please enter your family name.', max_length=120)),
                ('date_of_birth', models.DateField(help_text='Please enter your date of birth. (i.e. YYYY-MM-DD)')),
                ('email_address', models.EmailField(help_text='Please enter a valid email address.', max_length=254)),
                ('role', models.CharField(choices=[('mentor', 'mentor'), ('mentee', 'mentee')], max_length=100)),
                ('categories', models.ManyToManyField(to='core.Category')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('description', models.TextField()),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
                ('url_address', models.URLField(help_text='Enter the url for this resource', unique=True)),
                ('category', models.ForeignKey(help_text='Select a category for this resource', on_delete=django.db.models.deletion.CASCADE, to='core.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Pair',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mentee', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='mentee', to='core.Person')),
                ('mentor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='mentor', to='core.Person')),
            ],
        ),
        migrations.CreateModel(
            name='Forum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('description', models.TextField(max_length=500)),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Person')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(help_text='Enter a comment here', max_length=200)),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Person')),
                ('target_post', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Forum')),
            ],
            options={
                'ordering': ['-date_posted'],
            },
        ),
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=100)),
                ('slug', models.CharField(max_length=50)),
                ('pair', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Pair')),
            ],
        ),
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField(blank=True, null=True)),
                ('publish_date', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.Person')),
            ],
            options={
                'ordering': ['-publish_date'],
            },
        ),
        migrations.CreateModel(
            name='Questionnaire',
            fields=[
                ('person', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='core.Person')),
                ('email', models.EmailField(help_text='Please enter a valid email address.', max_length=254)),
                ('first_name', models.CharField(help_text='Please enter your first name.', max_length=120)),
                ('family_name', models.CharField(help_text='Please enter your family name.', max_length=120)),
                ('reference_name', models.CharField(help_text='Please enter a professional reference.', max_length=30)),
                ('reference_phone', phonenumber_field.modelfields.PhoneNumberField(help_text="Please enter your professional reference's phone number.", max_length=128, region=None)),
                ('reference_name2', models.CharField(help_text='Please enter a personal reference name.', max_length=30)),
                ('reference_phone2', phonenumber_field.modelfields.PhoneNumberField(help_text="Please enter your personal reference's phone number.", max_length=128, region=None)),
                ('date_of_birth', models.DateField(help_text='Please enter your date of birth. (i.e. YYYY-MM-DD)')),
                ('why', models.TextField(help_text='Please briefly describe why you want to become a foster mentor.', max_length=200)),
                ('availabilty', models.TextField(help_text='Please list the days and times you would be available to mentor.', max_length=200)),
                ('address', models.CharField(help_text='Please enter your full address', max_length=80)),
                ('education', models.CharField(choices=[('High School / GED', 'High School / GED'), ('Some College', 'Some College'), ("Associate's Degree", "Associate's Degree"), ("Bachelor's Degree", "Bachelor's Degree"), ("Masters' Degree", "Master's Degree"), ('PhD', 'PhD'), ('None', 'None')], default='None', max_length=30)),
                ('category', models.ManyToManyField(blank=True, help_text='Please select a skill speciality.', to='core.Category')),
            ],
        ),
    ]
