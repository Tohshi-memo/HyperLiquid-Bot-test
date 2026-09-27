# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-27T19:07:33.622868+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0227` n `12`; crypto_alt avg `-0.1526` n `234`; crypto_major avg `-0.1062` n `8`; equity avg `-0.0158` n `141`; fx avg `0.0014` n `6`; index avg `-0.0061` n `26`; metal avg `0.0003` n `20`; unknown avg `24.7199` n `958`
- 1h: commodity avg `-0.0284` n `12`; crypto_alt avg `0.422` n `234`; crypto_major avg `0.2989` n `8`; equity avg `0.0245` n `141`; fx avg `0.0041` n `6`; index avg `-0.0018` n `26`; metal avg `0.0024` n `20`; unknown avg `12.8436` n `958`
- 4h: commodity avg `0.0048` n `12`; crypto_alt avg `1.3609` n `234`; crypto_major avg `0.6018` n `8`; equity avg `0.1735` n `141`; fx avg `0.0061` n `6`; index avg `0.0208` n `26`; metal avg `0.0133` n `20`; unknown avg `7.5937` n `952`
- 24h: commodity avg `-0.1311` n `12`; crypto_alt avg `0.5968` n `234`; crypto_major avg `0.5452` n `8`; equity avg `0.3883` n `141`; fx avg `-0.0205` n `6`; index avg `0.0331` n `26`; metal avg `-0.0049` n `20`; unknown avg `117.6809` n `895`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1508`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1473`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1449`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1387`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1247`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1185`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1082`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1058`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0982`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0939`, n `668`, weak_sample_signal
