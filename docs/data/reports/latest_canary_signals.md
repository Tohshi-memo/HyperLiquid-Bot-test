# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-10T00:22:26.290968+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0735` n `12`; crypto_alt avg `0.3216` n `230`; crypto_major avg `0.2011` n `8`; equity avg `-0.0372` n `112`; fx avg `0.0332` n `6`; index avg `0.0041` n `25`; metal avg `-0.026` n `20`; unknown avg `0.0813` n `785`
- 1h: commodity avg `0.0403` n `12`; crypto_alt avg `0.1834` n `230`; crypto_major avg `0.1228` n `8`; equity avg `0.0703` n `112`; fx avg `0.0587` n `6`; index avg `0.0237` n `25`; metal avg `-0.0521` n `20`; unknown avg `0.002` n `785`
- 4h: commodity avg `0.3584` n `12`; crypto_alt avg `-0.661` n `230`; crypto_major avg `-0.5535` n `8`; equity avg `-0.092` n `112`; fx avg `0.048` n `6`; index avg `-0.0158` n `25`; metal avg `-0.1843` n `20`; unknown avg `0.024` n `785`
- 24h: commodity avg `0.466` n `12`; crypto_alt avg `0.744` n `230`; crypto_major avg `-0.2503` n `8`; equity avg `0.0982` n `112`; fx avg `0.0461` n `6`; index avg `0.0078` n `25`; metal avg `-0.1219` n `20`; unknown avg `-0.3864` n `752`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1827`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.15`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1395`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1363`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1351`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1347`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1292`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0981`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.091`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0901`, n `668`, weak_sample_signal
