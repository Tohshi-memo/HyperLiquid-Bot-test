# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-10T08:37:27.777426+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0265` n `12`; crypto_alt avg `0.01` n `230`; crypto_major avg `-0.1233` n `8`; equity avg `0.0046` n `112`; fx avg `0.0027` n `6`; index avg `-0.0003` n `25`; metal avg `-0.0409` n `20`; unknown avg `-0.0273` n `785`
- 1h: commodity avg `0.0923` n `12`; crypto_alt avg `0.0145` n `230`; crypto_major avg `-0.1525` n `8`; equity avg `0.0034` n `112`; fx avg `0.0129` n `6`; index avg `0.0045` n `25`; metal avg `-0.0644` n `20`; unknown avg `0.0192` n `785`
- 4h: commodity avg `0.0581` n `12`; crypto_alt avg `0.3557` n `230`; crypto_major avg `0.4006` n `8`; equity avg `0.3063` n `112`; fx avg `0.0997` n `6`; index avg `0.0682` n `25`; metal avg `0.0231` n `20`; unknown avg `57.2081` n `753`
- 24h: commodity avg `0.3709` n `12`; crypto_alt avg `0.9617` n `230`; crypto_major avg `0.1959` n `8`; equity avg `-0.0361` n `112`; fx avg `0.2192` n `6`; index avg `0.0792` n `25`; metal avg `-0.0931` n `20`; unknown avg `56.9609` n `753`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1882`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1434`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1375`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1353`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1247`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.122`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1178`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1165`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1038`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0978`, n `668`, weak_sample_signal
