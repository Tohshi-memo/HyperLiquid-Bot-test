# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-11T20:07:26.228052+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0198` n `12`; crypto_alt avg `0.3914` n `230`; crypto_major avg `0.473` n `8`; equity avg `0.0782` n `113`; fx avg `-0.0032` n `6`; index avg `0.0172` n `25`; metal avg `0.0145` n `20`; unknown avg `0.2667` n `785`
- 1h: commodity avg `0.0141` n `12`; crypto_alt avg `0.5945` n `230`; crypto_major avg `0.8494` n `8`; equity avg `0.3361` n `113`; fx avg `0.0023` n `6`; index avg `0.0441` n `25`; metal avg `0.0583` n `20`; unknown avg `1.1828` n `785`
- 4h: commodity avg `0.1093` n `12`; crypto_alt avg `0.7092` n `230`; crypto_major avg `0.9956` n `8`; equity avg `0.181` n `113`; fx avg `0.0081` n `6`; index avg `-0.0304` n `25`; metal avg `-0.0382` n `20`; unknown avg `0.6236` n `785`
- 24h: commodity avg `0.1616` n `12`; crypto_alt avg `-1.3642` n `230`; crypto_major avg `0.1692` n `8`; equity avg `0.7843` n `113`; fx avg `-0.0698` n `6`; index avg `0.089` n `25`; metal avg `-0.1941` n `20`; unknown avg `-0.2387` n `753`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2126`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.2069`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.2057`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.2021`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1899`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1462`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1295`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.123`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1029`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.087`, n `668`, weak_sample_signal
