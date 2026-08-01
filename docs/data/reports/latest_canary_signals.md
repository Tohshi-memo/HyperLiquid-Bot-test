# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-01T04:37:50.257796+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0302` n `12`; crypto_alt avg `0.0008` n `230`; crypto_major avg `-0.0417` n `8`; equity avg `-0.0137` n `102`; fx avg `0.0242` n `6`; index avg `-0.0075` n `25`; metal avg `-0.0099` n `20`; unknown avg `-0.058` n `781`
- 1h: commodity avg `-0.0343` n `12`; crypto_alt avg `0.166` n `230`; crypto_major avg `0.1183` n `8`; equity avg `-0.0123` n `102`; fx avg `0.0158` n `6`; index avg `0.007` n `25`; metal avg `-0.016` n `20`; unknown avg `0.3675` n `781`
- 4h: commodity avg `-0.0382` n `12`; crypto_alt avg `0.283` n `230`; crypto_major avg `0.1575` n `8`; equity avg `0.0619` n `102`; fx avg `0.015` n `6`; index avg `0.0429` n `25`; metal avg `-0.0176` n `20`; unknown avg `0.0851` n `781`
- 24h: commodity avg `0.9628` n `12`; crypto_alt avg `0.4513` n `230`; crypto_major avg `-1.3433` n `8`; equity avg `-2.4735` n `102`; fx avg `-0.1638` n `6`; index avg `-0.2445` n `25`; metal avg `-0.2702` n `20`; unknown avg `4.8849` n `747`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1036`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.102`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1003`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0856`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0744`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0735`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0701`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0688`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0671`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0648`, n `668`, weak_sample_signal
