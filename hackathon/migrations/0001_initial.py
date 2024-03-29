# Generated by Django 5.0.2 on 2024-02-15 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Healthcare',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Stack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Hackathon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('supported_ages', models.CharField(choices=[('<20s', '>20s'), ('20s', '20s'), ("30's", "30's"), ("40's", "40's"), ("50's", "50's"), (">60's", ">60's")], max_length=255)),
                ('supported_years', models.CharField(choices=[('Zero', 'Zero'), ('1 - 2 Years', '1 - 2 Years'), ('3 - 5 Years', '3 - 5 Years'), ('More than 5 Years', 'More than 5 Years')], max_length=255)),
                ('sex_choices', models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('prefer not to say', 'Prefer not to say')], max_length=255)),
                ('participation', models.CharField(choices=[('yes', 'Yes'), ('no', 'No')], max_length=255)),
                ('experience', models.CharField(choices=[('yes', 'Yes'), ('no', 'No')], max_length=255)),
                ('hear_us', models.CharField(choices=[('word of mouth', 'Word of Mouth'), ('online advert', 'Online Advert'), ('social media', 'Social Media'), ('website', 'Website'), ('other', 'Other')], max_length=255)),
                ('linkedin', models.CharField(max_length=5000)),
                ('overview', models.CharField(max_length=5000)),
                ('other_problems', models.CharField(max_length=5000)),
                ('name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('number', models.IntegerField()),
                ('healthcare_problems', models.ManyToManyField(to='hackathon.healthcare')),
                ('software_stack', models.ManyToManyField(to='hackathon.stack')),
            ],
        ),
    ]
