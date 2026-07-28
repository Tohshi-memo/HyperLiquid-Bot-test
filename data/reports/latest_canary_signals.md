# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-28T13:07:31.519354+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0336` n `12`; crypto_alt avg `0.0162` n `230`; crypto_major avg `0.0733` n `8`; equity avg `0.0848` n `102`; fx avg `0.0121` n `6`; index avg `0.0073` n `25`; metal avg `-0.0174` n `20`; unknown avg `-0.0937` n `774`
- 1h: commodity avg `-0.0689` n `12`; crypto_alt avg `0.2145` n `230`; crypto_major avg `0.2198` n `8`; equity avg `0.1171` n `102`; fx avg `0.0096` n `6`; index avg `0.0248` n `25`; metal avg `0.0835` n `20`; unknown avg `0.1426` n `774`
- 4h: commodity avg `0.0823` n `12`; crypto_alt avg `0.2087` n `230`; crypto_major avg `0.0123` n `8`; equity avg `-0.5359` n `102`; fx avg `-0.0338` n `6`; index avg `-0.0036` n `25`; metal avg `-0.0821` n `20`; unknown avg `0.0201` n `774`
- 24h: commodity avg `-0.782` n `12`; crypto_alt avg `-3.32` n `230`; crypto_major avg `-3.5081` n `8`; equity avg `-4.1108` n `102`; fx avg `-0.1476` n `6`; index avg `-0.7987` n `25`; metal avg `-0.3921` n `20`; unknown avg `1225.2884` n `758`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1568`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1099`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1057`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1007`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0946`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0893`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.084`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.075`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0707`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0681`, n `668`, weak_sample_signal
