# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-12T11:22:24.447540+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.009` n `12`; crypto_alt avg `0.0663` n `230`; crypto_major avg `0.0698` n `8`; equity avg `-0.0572` n `113`; fx avg `0.0016` n `6`; index avg `-0.0069` n `25`; metal avg `-0.0031` n `20`; unknown avg `-0.0457` n `786`
- 1h: commodity avg `0.0245` n `12`; crypto_alt avg `0.0678` n `230`; crypto_major avg `0.0525` n `8`; equity avg `-0.1515` n `113`; fx avg `0.0016` n `6`; index avg `-0.0137` n `25`; metal avg `0.0116` n `20`; unknown avg `-0.0336` n `786`
- 4h: commodity avg `-0.0822` n `12`; crypto_alt avg `0.0655` n `230`; crypto_major avg `0.5294` n `8`; equity avg `0.3873` n `113`; fx avg `-0.0428` n `6`; index avg `0.0769` n `25`; metal avg `0.2185` n `20`; unknown avg `-0.0939` n `786`
- 24h: commodity avg `0.2744` n `12`; crypto_alt avg `-1.0363` n `230`; crypto_major avg `0.8203` n `8`; equity avg `2.0743` n `113`; fx avg `0.0536` n `6`; index avg `0.1749` n `25`; metal avg `0.2039` n `20`; unknown avg `-0.1486` n `769`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.245`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.2341`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.2084`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1925`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1798`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1578`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1502`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1381`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1343`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1294`, n `668`, weak_sample_signal
