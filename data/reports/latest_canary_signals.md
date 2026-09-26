# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-26T19:52:29.321657+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.022` n `12`; crypto_alt avg `0.0261` n `234`; crypto_major avg `0.0261` n `8`; equity avg `0.0224` n `141`; fx avg `0.0087` n `6`; index avg `0.0004` n `26`; metal avg `0.0002` n `20`; unknown avg `0.9087` n `961`
- 1h: commodity avg `0.002` n `12`; crypto_alt avg `-0.1071` n `234`; crypto_major avg `0.0308` n `8`; equity avg `0.021` n `141`; fx avg `0.0087` n `6`; index avg `0.0006` n `26`; metal avg `0.0078` n `20`; unknown avg `4.677` n `959`
- 4h: commodity avg `0.0428` n `12`; crypto_alt avg `-1.1933` n `234`; crypto_major avg `-0.7293` n `8`; equity avg `-0.0329` n `141`; fx avg `0.0158` n `6`; index avg `-0.0122` n `26`; metal avg `0.0088` n `20`; unknown avg `9.1354` n `945`
- 24h: commodity avg `0.3587` n `12`; crypto_alt avg `1.2959` n `234`; crypto_major avg `-0.716` n `8`; equity avg `-0.0309` n `141`; fx avg `0.0219` n `6`; index avg `-0.0538` n `26`; metal avg `-0.0379` n `20`; unknown avg `3.0642` n `814`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.18`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1587`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1533`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1508`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1367`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1288`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1216`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1004`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0907`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0901`, n `668`, weak_sample_signal
