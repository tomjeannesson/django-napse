# Generated by Django 4.1.7 on 2023-08-08 13:47

from django.db import migrations, models
import django.db.models.deletion
import django_napse.utils.constants
import django_napse.utils.findable_class
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Architechture",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
            ],
            bases=(models.Model, django_napse.utils.findable_class.FindableClass),
        ),
        migrations.CreateModel(
            name="Bot",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "uuid",
                    models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
                ),
                ("name", models.CharField(default="Bot", max_length=100)),
                ("can_trade", models.BooleanField(default=False)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="BotConfig",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "uuid",
                    models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
                ),
                ("immutable", models.BooleanField(default=False)),
            ],
            bases=(models.Model, django_napse.utils.findable_class.FindableClass),
        ),
        migrations.CreateModel(
            name="Cluster",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Connection",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("enabled", models.BooleanField(default=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "bot",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="connections",
                        to="django_napse_core.bot",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="DefaultFleetOperator",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Exchange",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=200, unique=True)),
                ("description", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="ExchangeAccount",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=200, unique=True)),
                ("testing", models.BooleanField(default=True)),
                ("description", models.TextField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "exchange",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="accounts",
                        to="django_napse_core.exchange",
                    ),
                ),
            ],
            bases=(models.Model, django_napse.utils.findable_class.FindableClass),
        ),
        migrations.CreateModel(
            name="Modification",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("applied", models.BooleanField(default=False)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("ignore_failed_order", models.BooleanField(default=False)),
                ("key", models.CharField(max_length=100)),
                ("value", models.CharField(max_length=100)),
                ("target_type", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="NapseAPIKey",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=200, unique=True)),
                ("description", models.TextField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("napse_API_key", models.CharField(max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="PermissionType",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=200, unique=True)),
                ("description", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="Strategy",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
            ],
            bases=(models.Model, django_napse.utils.findable_class.FindableClass),
        ),
        migrations.CreateModel(
            name="Wallet",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(default="Wallet", max_length=255)),
                ("locked", models.BooleanField(default=False)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
            bases=(models.Model, django_napse.utils.findable_class.FindableClass),
        ),
        migrations.CreateModel(
            name="BotModification",
            fields=[
                (
                    "modification_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="django_napse_core.modification",
                    ),
                ),
            ],
            bases=("django_napse_core.modification",),
        ),
        migrations.CreateModel(
            name="EmptyBotConfig",
            fields=[
                (
                    "botconfig_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="django_napse_core.botconfig",
                    ),
                ),
                ("setting_empty", models.BooleanField()),
            ],
            bases=("django_napse_core.botconfig",),
        ),
        migrations.CreateModel(
            name="EquilibriumFleetOperator",
            fields=[
                (
                    "defaultfleetoperator_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="django_napse_core.defaultfleetoperator",
                    ),
                ),
            ],
            bases=("django_napse_core.defaultfleetoperator",),
        ),
        migrations.CreateModel(
            name="SpecificSharesFleetOperator",
            fields=[
                (
                    "defaultfleetoperator_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="django_napse_core.defaultfleetoperator",
                    ),
                ),
            ],
            bases=("django_napse_core.defaultfleetoperator",),
        ),
        migrations.CreateModel(
            name="Transaction",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("amount", models.FloatField()),
                ("ticker", models.CharField(max_length=10)),
                (
                    "transaction_type",
                    models.CharField(default="TRANSFER", max_length=20),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "from_wallet",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="transactions_from",
                        to="django_napse_core.wallet",
                    ),
                ),
                (
                    "to_wallet",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="transactions_to",
                        to="django_napse_core.wallet",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Order",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("amount", models.FloatField()),
                ("price", models.FloatField()),
                ("pair", models.CharField(max_length=10)),
                ("side", models.CharField(max_length=10)),
                (
                    "status",
                    models.CharField(
                        default=django_napse.utils.constants.ORDER_STATUS["PENDING"],
                        max_length=15,
                    ),
                ),
                ("completed", models.BooleanField(default=False)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "connection",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="orders",
                        to="django_napse_core.connection",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="NapseSpace",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=200)),
                ("identifier", models.CharField(max_length=20, unique=True)),
                ("description", models.TextField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "exchange_account",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="spaces",
                        to="django_napse_core.exchangeaccount",
                    ),
                ),
            ],
            options={
                "unique_together": {("name", "exchange_account")},
            },
        ),
        migrations.AddField(
            model_name="modification",
            name="order",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="modifications",
                to="django_napse_core.order",
            ),
        ),
        migrations.CreateModel(
            name="Link",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "bot",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="link",
                        to="django_napse_core.bot",
                    ),
                ),
                (
                    "cluster",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="links",
                        to="django_napse_core.cluster",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="KeyPermission",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "key",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="permissions",
                        to="django_napse_core.napseapikey",
                    ),
                ),
                (
                    "permission_type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="django_napse_core.permissiontype",
                    ),
                ),
                (
                    "space",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="django_napse_core.napsespace",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Fleet",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "uuid",
                    models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
                ),
                ("name", models.CharField(default="Fleet", max_length=100)),
                ("running", models.BooleanField(default=False)),
                ("setup_finished", models.BooleanField(default=False)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "exchange_account",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="django_napse_core.exchangeaccount",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="defaultfleetoperator",
            name="fleet",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="operator",
                to="django_napse_core.fleet",
            ),
        ),
        migrations.CreateModel(
            name="Debit",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("amount", models.FloatField()),
                ("ticker", models.CharField(max_length=10)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "wallet",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="debits",
                        to="django_napse_core.wallet",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Credit",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("amount", models.FloatField()),
                ("ticker", models.CharField(max_length=10)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "wallet",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="credits",
                        to="django_napse_core.wallet",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Controller",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("pair", models.CharField(max_length=10)),
                ("base", models.CharField(max_length=10)),
                ("quote", models.CharField(max_length=10)),
                ("interval", models.CharField(max_length=10)),
                ("min_notional", models.FloatField(null=True)),
                ("min_trade", models.FloatField(null=True)),
                ("lot_size", models.IntegerField(null=True)),
                ("price", models.FloatField(null=True)),
                ("last_price_update", models.DateTimeField(null=True)),
                ("last_settings_update", models.DateTimeField(null=True)),
                (
                    "space",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="controller",
                        to="django_napse_core.napsespace",
                    ),
                ),
            ],
            options={
                "unique_together": {("pair", "interval", "space")},
            },
        ),
        migrations.CreateModel(
            name="ConnectionSpecificArgs",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("key", models.CharField(max_length=100)),
                ("value", models.CharField(default="None", max_length=100)),
                ("target_type", models.CharField(default="None", max_length=100)),
                (
                    "connection",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="specific_args",
                        to="django_napse_core.connection",
                    ),
                ),
            ],
            options={
                "unique_together": {("connection", "key")},
            },
        ),
        migrations.AddField(
            model_name="connection",
            name="space",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="connections",
                to="django_napse_core.napsespace",
            ),
        ),
        migrations.AddField(
            model_name="cluster",
            name="fleet",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="clusters",
                to="django_napse_core.fleet",
            ),
        ),
        migrations.CreateModel(
            name="Candle",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("latest", models.BooleanField(default=False)),
                ("last_update", models.DateTimeField(auto_now=True)),
                ("open", models.FloatField()),
                ("high", models.FloatField()),
                ("low", models.FloatField()),
                ("close", models.FloatField()),
                ("volume", models.FloatField()),
                (
                    "controller",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="candles",
                        to="django_napse_core.controller",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="botconfig",
            name="space",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="bot_configs",
                to="django_napse_core.napsespace",
            ),
        ),
        migrations.AddField(
            model_name="bot",
            name="strategy",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="bot",
                to="django_napse_core.strategy",
            ),
        ),
        migrations.CreateModel(
            name="SpecificShare",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("share", models.FloatField()),
                (
                    "cluster",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="specific_shares",
                        to="django_napse_core.cluster",
                    ),
                ),
                (
                    "operator",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="specific_shares",
                        to="django_napse_core.defaultfleetoperator",
                    ),
                ),
            ],
            options={
                "unique_together": {("cluster", "operator")},
            },
        ),
        migrations.CreateModel(
            name="SpecificBreakPoint",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("scale_up_breakpoint", models.FloatField()),
                (
                    "cluster",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="specific_breakpoints",
                        to="django_napse_core.cluster",
                    ),
                ),
                (
                    "operator",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="specific_breakpoints",
                        to="django_napse_core.defaultfleetoperator",
                    ),
                ),
            ],
            options={
                "unique_together": {("cluster", "operator")},
            },
        ),
        migrations.CreateModel(
            name="SpecificAutoscale",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("autoscale", models.BooleanField(default=True)),
                (
                    "cluster",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="specific_autoscales",
                        to="django_napse_core.cluster",
                    ),
                ),
                (
                    "operator",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="specific_autoscales",
                        to="django_napse_core.defaultfleetoperator",
                    ),
                ),
            ],
            options={
                "unique_together": {("cluster", "operator")},
            },
        ),
        migrations.CreateModel(
            name="SpecificArgsModification",
            fields=[
                (
                    "modification_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="django_napse_core.modification",
                    ),
                ),
                (
                    "connection_specific_arg",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="modifications",
                        to="django_napse_core.connectionspecificargs",
                    ),
                ),
            ],
            bases=("django_napse_core.modification",),
        ),
        migrations.CreateModel(
            name="SpaceWallet",
            fields=[
                (
                    "wallet_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="django_napse_core.wallet",
                    ),
                ),
                (
                    "owner",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="wallet",
                        to="django_napse_core.napsespace",
                    ),
                ),
            ],
            bases=("django_napse_core.wallet",),
        ),
        migrations.CreateModel(
            name="SinglePairArchitechture",
            fields=[
                (
                    "architechture_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="django_napse_core.architechture",
                    ),
                ),
                (
                    "controller",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="single_pair_architechtures",
                        to="django_napse_core.controller",
                    ),
                ),
            ],
            bases=("django_napse_core.architechture",),
        ),
        migrations.CreateModel(
            name="OrderWallet",
            fields=[
                (
                    "wallet_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="django_napse_core.wallet",
                    ),
                ),
                (
                    "owner",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="wallet",
                        to="django_napse_core.order",
                    ),
                ),
            ],
            bases=("django_napse_core.wallet",),
        ),
        migrations.CreateModel(
            name="EmptyStrategy",
            fields=[
                (
                    "strategy_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="django_napse_core.strategy",
                    ),
                ),
                (
                    "architechture",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="strategy",
                        to="django_napse_core.singlepairarchitechture",
                    ),
                ),
                (
                    "config",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="strategy",
                        to="django_napse_core.emptybotconfig",
                    ),
                ),
            ],
            bases=("django_napse_core.strategy",),
        ),
        migrations.CreateModel(
            name="Currency",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("mbp", models.FloatField()),
                ("ticker", models.CharField(max_length=10)),
                ("amount", models.FloatField(default=0)),
                (
                    "wallet",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="currencies",
                        to="django_napse_core.wallet",
                    ),
                ),
            ],
            options={
                "unique_together": {("wallet", "ticker")},
            },
        ),
        migrations.CreateModel(
            name="ConnectionWallet",
            fields=[
                (
                    "wallet_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="django_napse_core.wallet",
                    ),
                ),
                (
                    "owner",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="wallet",
                        to="django_napse_core.connection",
                    ),
                ),
            ],
            bases=("django_napse_core.wallet",),
        ),
        migrations.AlterUniqueTogether(
            name="connection",
            unique_together={("space", "bot")},
        ),
        migrations.CreateModel(
            name="BinanceAccount",
            fields=[
                (
                    "exchangeaccount_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="django_napse_core.exchangeaccount",
                    ),
                ),
                ("public_key", models.CharField(max_length=200)),
                ("private_key", models.CharField(max_length=200)),
            ],
            options={
                "unique_together": {("public_key", "private_key")},
            },
            bases=("django_napse_core.exchangeaccount",),
        ),
    ]
