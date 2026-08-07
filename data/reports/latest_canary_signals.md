# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-07T09:22:25.518558+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0398` n `12`; crypto_alt avg `-0.0296` n `230`; crypto_major avg `0.0961` n `8`; equity avg `0.0578` n `112`; fx avg `0.0018` n `6`; index avg `0.0086` n `25`; metal avg `0.0205` n `20`; unknown avg `-0.0195` n `782`
- 1h: commodity avg `-0.1271` n `12`; crypto_alt avg `0.0017` n `230`; crypto_major avg `0.5016` n `8`; equity avg `0.1451` n `112`; fx avg `-0.0076` n `6`; index avg `0.041` n `25`; metal avg `0.0699` n `20`; unknown avg `0.0114` n `782`
- 4h: commodity avg `-0.183` n `12`; crypto_alt avg `0.2486` n `230`; crypto_major avg `0.9368` n `8`; equity avg `0.8619` n `112`; fx avg `-0.0514` n `6`; index avg `0.1051` n `25`; metal avg `0.4344` n `20`; unknown avg `0.0294` n `766`
- 24h: commodity avg `0.464` n `12`; crypto_alt avg `0.4663` n `230`; crypto_major avg `-0.2067` n `8`; equity avg `2.1095` n `109`; fx avg `-0.0792` n `6`; index avg `0.0916` n `25`; metal avg `0.2757` n `20`; unknown avg `110.8194` n `765`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1113`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1015`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0999`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0899`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0754`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0692`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0657`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0618`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0595`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.058`, n `668`, weak_sample_signal
