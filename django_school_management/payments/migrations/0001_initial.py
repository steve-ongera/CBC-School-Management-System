# Generated by Django 2.2.13 on 2021-02-25 06:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SSLPayment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('transaction_id', models.PositiveIntegerField()),
                ('payer', models.CharField(max_length=150, verbose_name='Name of the registrant')),
                ('received_amount', models.DecimalField(decimal_places=2, max_digits=8)),
                ('pay_reason', models.CharField(choices=[('admission', 'Online Admission'), ('midfee', 'Midterm Exam Fee'), ('finalfee', 'Final Exam Fee')], max_length=10)),
                ('payer_mobile', models.CharField(max_length=15)),
                ('payer_email', models.EmailField(max_length=254)),
                ('payer_city', models.CharField(max_length=85)),
                ('payer_country', models.CharField(max_length=55)),
            ],
            options={
                'ordering': ['-created', 'received_amount'],
            },
        ),
        migrations.CreateModel(
            name='SSLAdmissionPaymentVerfication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('status', models.PositiveSmallIntegerField(choices=[(0, 'Rejected'), (1, 'Verfied')], default=0)),
                ('payment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='verfied_payments', to='payments.SSLPayment')),
                ('verified_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='admission_pay_verifications', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
    ]
