import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('authorid', models.CharField(db_column='AuthorID', max_length=12, primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='Name', max_length=20)),
            ],
            options={
                'db_table': 'author',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Conferjournal',
            fields=[
                ('name', models.CharField(db_column='Name', max_length=512, primary_key=True, serialize=False)),
                ('conferorjournal', models.CharField(db_column='ConferOrJournal', max_length=1)),
                ('abbreviation', models.CharField(blank=True, db_column='Abbreviation', max_length=50, null=True)),
                ('ruclevel', models.CharField(db_column='RUCLevel', max_length=2)),
                ('ccflevel', models.CharField(db_column='CCFLevel', max_length=2)),
                ('ccfchinalevel', models.CharField(db_column='CCFChinaLevel', max_length=2)),
                ('issn', models.CharField(blank=True, db_column='ISSN', max_length=50, null=True)),
            ],
            options={
                'db_table': 'conferjournal',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Tmppaper',
            fields=[
                ('paperid', models.BigAutoField(db_column='PaperID', primary_key=True, serialize=False)),
                ('title', models.CharField(db_column='Title', max_length=1024)),
                ('conferorjournal', models.CharField(db_column='ConferOrJournal', max_length=1)),
                ('publishtime', models.DateField(db_column='PublishTime')),
                ('volume', models.IntegerField(blank=True, db_column='Volume', null=True)),
                ('issue', models.IntegerField(blank=True, db_column='Issue', null=True)),
                ('startpage', models.IntegerField(db_column='StartPage')),
                ('endpage', models.IntegerField(db_column='EndPage')),
                ('keywords', models.CharField(blank=True, db_column='Keywords', max_length=100, null=True)),
                ('conferencecountry', models.CharField(blank=True, db_column='ConferenceCountry', max_length=50, null=True)),
                ('conferencecity', models.CharField(blank=True, db_column='ConferenceCity', max_length=50, null=True)),
                ('papertype', models.CharField(db_column='PaperType', max_length=20)),
                ('language', models.CharField(blank=True, db_column='Language', max_length=1, null=True)),
                ('commitauthorid', models.ForeignKey(db_column='CommitAuthorID', on_delete=django.db.models.deletion.DO_NOTHING, to='apps.author')),
                ('conferjournalname', models.ForeignKey(db_column='ConferJournalName', on_delete=django.db.models.deletion.DO_NOTHING, to='apps.conferjournal')),
            ],
            options={
                'db_table': 'tmppaper',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Tmppa',
            fields=[
                ('paid', models.BigAutoField(db_column='PAID', primary_key=True, serialize=False)),
                ('authorname', models.CharField(db_column='AuthorName', max_length=20)),
                ('authorrank', models.IntegerField(db_column='AuthorRank')),
                ('authoridentity', models.CharField(db_column='AuthorIdentity', max_length=20)),
                ('authortype', models.CharField(db_column='AuthorType', max_length=20)),
                ('paperid', models.ForeignKey(db_column='PaperID', on_delete=django.db.models.deletion.CASCADE, to='apps.tmppaper')),
            ],
            options={
                'db_table': 'tmppa',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Paper',
            fields=[
                ('paperid', models.BigAutoField(db_column='PaperID', primary_key=True, serialize=False)),
                ('title', models.CharField(db_column='Title', max_length=1024)),
                ('conferorjournal', models.CharField(db_column='ConferOrJournal', max_length=1)),
                ('publishtime', models.DateField(db_column='PublishTime')),
                ('volume', models.IntegerField(blank=True, db_column='Volume', null=True)),
                ('issue', models.IntegerField(blank=True, db_column='Issue', null=True)),
                ('startpage', models.IntegerField(db_column='StartPage')),
                ('endpage', models.IntegerField(db_column='EndPage')),
                ('keywords', models.CharField(blank=True, db_column='Keywords', max_length=100, null=True)),
                ('conferencecountry', models.CharField(blank=True, db_column='ConferenceCountry', max_length=50, null=True)),
                ('conferencecity', models.CharField(blank=True, db_column='ConferenceCity', max_length=50, null=True)),
                ('papertype', models.CharField(db_column='PaperType', max_length=20)),
                ('language', models.CharField(blank=True, db_column='Language', max_length=1, null=True)),
                ('conferjournalname', models.ForeignKey(db_column='ConferJournalName', on_delete=django.db.models.deletion.DO_NOTHING, to='apps.conferjournal')),
            ],
            options={
                'db_table': 'paper',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Pa',
            fields=[
                ('paid', models.BigAutoField(db_column='PAID', primary_key=True, serialize=False)),
                ('authorname', models.CharField(db_column='AuthorName', max_length=20)),
                ('authorrank', models.IntegerField(db_column='AuthorRank')),
                ('authoridentity', models.CharField(db_column='AuthorIdentity', max_length=20)),
                ('authortype', models.CharField(db_column='AuthorType', max_length=20)),
                ('paperid', models.ForeignKey(db_column='PaperID', on_delete=django.db.models.deletion.DO_NOTHING, to='apps.paper')),
            ],
            options={
                'db_table': 'pa',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('create_time', models.DateField(auto_now_add=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': '用户表',
                'verbose_name_plural': '用户表',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
