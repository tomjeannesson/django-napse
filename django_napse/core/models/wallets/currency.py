from django.db import models


class Currency(models.Model):
    wallet = models.ForeignKey("Wallet", on_delete=models.CASCADE, related_name="currencies")
    mbp = models.FloatField()
    ticker = models.CharField(max_length=10)
    amount = models.FloatField(default=0)

    class Meta:
        unique_together = ("wallet", "ticker")

    def __str__(self):  # pragma: no cover
        return f"{self.ticker} - {self.amount} - {self.wallet.pk}"

    def info(self, verbose=True, beacon=""):
        string = ""
        string += f"{beacon}Currency ({self.pk=}):\n"
        string += f"{beacon}Args:\n"
        string += f"{beacon}\t{self.wallet=}\n"
        string += f"{beacon}\t{self.mbp=}\n"
        string += f"{beacon}\t{self.ticker=}\n"
        string += f"{beacon}\t{self.amount=}\n"

        if verbose:  # pragma: no cover
            print(string)
        return string

    @property
    def testing(self):
        return self.wallet.testing
