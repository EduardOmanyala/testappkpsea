# Generated by Django 4.2.3 on 2023-07-11 15:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='QuizCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('description', models.CharField(choices=[('Questions 1 - 25', 'Questions 1 - 25'), ('Questions 1 - 25', 'Questions 1 - 25'), ('All 50 Questions', 'All 50 Questions')], default='Questions 1 - 25', max_length=20)),
                ('subject', models.CharField(choices=[('English', 'English'), ('Maths', 'Maths'), ('Kiswahili', 'Kiswahili'), ('Science', 'Science'), ('Social', 'Social'), ('Christian', 'Christian'), ('Hindu', 'Hindu'), ('Islam', 'Islam')], default='English', max_length=20)),
                ('year', models.CharField(choices=[('2022', '2022'), ('2021', '2021'), ('2020', '2020'), ('2019', '2019'), ('2018', '2018'), ('2017', '2017'), ('2016', '2016'), ('2015', '2015'), ('2014', '2014'), ('2013', '2013'), ('2012', '2012'), ('2011', '2011')], default='2022', max_length=4)),
                ('paper_type', models.CharField(choices=[('national', 'national'), ('nairobi', 'nairobi'), ('mombasa', 'mombasa'), ('kakamega', 'kakamega'), ('nakuru', 'nakuru')], default='national', max_length=20)),
                ('section', models.CharField(choices=[('one', 'one'), ('two', 'two'), ('full', 'full')], default='one', max_length=20)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='QuizQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('opt_1', models.CharField(max_length=200)),
                ('opt_2', models.CharField(max_length=200)),
                ('opt_3', models.CharField(max_length=200)),
                ('opt_4', models.CharField(max_length=200)),
                ('right_opt', models.CharField(max_length=200)),
                ('questionimage', models.ImageField(blank=True, null=True, upload_to='questionimages/')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.quizcategory')),
            ],
            options={
                'verbose_name_plural': 'Questions',
            },
        ),
        migrations.CreateModel(
            name='UserSubmittedAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('right_answer', models.CharField(max_length=200)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.quizquestion')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'User Submitted Answers',
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phoneno', models.CharField(max_length=10, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Payment',
            },
        ),
    ]