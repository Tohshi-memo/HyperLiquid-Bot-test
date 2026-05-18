# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-18T06:52:16.739065+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0755` n `12`; crypto_alt avg `0.1356` n `228`; crypto_major avg `0.1655` n `8`; equity avg `0.0676` n `66`; fx avg `0.0003` n `5`; index avg `0.0876` n `23`; metal avg `0.1873` n `18`; unknown avg `0.9433` n `383`
- 1h: commodity avg `0.1793` n `12`; crypto_alt avg `-0.2992` n `228`; crypto_major avg `-0.2598` n `8`; equity avg `-0.071` n `66`; fx avg `-0.0251` n `5`; index avg `-0.0514` n `23`; metal avg `0.2862` n `18`; unknown avg `1.034` n `363`
- 4h: commodity avg `0.0614` n `12`; crypto_alt avg `-0.4887` n `228`; crypto_major avg `-0.3027` n `8`; equity avg `0.0463` n `66`; fx avg `-0.03` n `5`; index avg `0.2069` n `23`; metal avg `0.3996` n `18`; unknown avg `0.7827` n `363`
- 24h: commodity avg `2.7322` n `12`; crypto_alt avg `-11.3009` n `228`; crypto_major avg `-3.7452` n `8`; equity avg `-3.0783` n `65`; fx avg `-0.1116` n `5`; index avg `-1.7212` n `23`; metal avg `-5.9501` n `18`; unknown avg `-0.3591` n `357`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1455`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1209`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1083`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1019`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0958`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0934`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0931`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0923`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0869`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0854`, n `668`, weak_sample_signal
