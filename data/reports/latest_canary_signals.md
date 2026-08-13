# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-13T01:07:23.961213+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0376` n `12`; crypto_alt avg `-0.1451` n `230`; crypto_major avg `-0.0519` n `8`; equity avg `0.0047` n `113`; fx avg `0.0165` n `6`; index avg `0.0064` n `25`; metal avg `-0.0227` n `20`; unknown avg `0.0118` n `786`
- 1h: commodity avg `-0.0993` n `12`; crypto_alt avg `0.0247` n `230`; crypto_major avg `0.0211` n `8`; equity avg `-0.0994` n `113`; fx avg `-0.0162` n `6`; index avg `-0.018` n `25`; metal avg `0.0781` n `20`; unknown avg `0.0275` n `786`
- 4h: commodity avg `-0.15` n `12`; crypto_alt avg `-0.2714` n `230`; crypto_major avg `-0.2084` n `8`; equity avg `0.3553` n `113`; fx avg `-0.0534` n `6`; index avg `0.0553` n `25`; metal avg `0.1305` n `20`; unknown avg `-0.0018` n `786`
- 24h: commodity avg `-0.258` n `12`; crypto_alt avg `-1.3466` n `230`; crypto_major avg `-0.6098` n `8`; equity avg `2.9323` n `113`; fx avg `-0.0257` n `6`; index avg `0.4147` n `25`; metal avg `0.2021` n `20`; unknown avg `0.0086` n `770`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2393`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.2046`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1915`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1903`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1863`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1726`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1588`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1477`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1417`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1379`, n `668`, weak_sample_signal
