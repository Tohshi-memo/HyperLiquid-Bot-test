# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-12T08:07:27.519107+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0251` n `12`; crypto_alt avg `0.1836` n `230`; crypto_major avg `0.2169` n `8`; equity avg `0.0325` n `92`; fx avg `-0.0006` n `6`; index avg `0.0085` n `25`; metal avg `0.0003` n `20`; unknown avg `0.0495` n `765`
- 1h: commodity avg `0.1049` n `12`; crypto_alt avg `0.0955` n `230`; crypto_major avg `0.1672` n `8`; equity avg `0.0182` n `92`; fx avg `-0.0015` n `6`; index avg `0.0291` n `25`; metal avg `-0.0127` n `20`; unknown avg `-0.1502` n `765`
- 4h: commodity avg `0.1419` n `12`; crypto_alt avg `-0.4935` n `230`; crypto_major avg `-0.3669` n `8`; equity avg `-0.1587` n `92`; fx avg `0.0015` n `6`; index avg `-0.0058` n `25`; metal avg `-0.0191` n `20`; unknown avg `0.1888` n `747`
- 24h: commodity avg `0.5503` n `12`; crypto_alt avg `-0.5634` n `230`; crypto_major avg `-0.537` n `8`; equity avg `-0.1663` n `92`; fx avg `0.0018` n `6`; index avg `-0.1198` n `25`; metal avg `-0.1067` n `20`; unknown avg `-0.0167` n `743`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1788`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1621`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1363`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.125`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1209`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1182`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1128`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1014`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0996`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0987`, n `668`, weak_sample_signal
