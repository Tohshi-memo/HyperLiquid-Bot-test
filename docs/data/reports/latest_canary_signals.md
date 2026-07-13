# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-13T01:37:28.163379+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.01` n `12`; crypto_alt avg `-0.1406` n `230`; crypto_major avg `-0.1522` n `8`; equity avg `-0.1704` n `92`; fx avg `0.0114` n `6`; index avg `-0.0058` n `25`; metal avg `0.1146` n `20`; unknown avg `0.0821` n `766`
- 1h: commodity avg `0.0988` n `12`; crypto_alt avg `-0.447` n `230`; crypto_major avg `-0.4384` n `8`; equity avg `-0.7452` n `92`; fx avg `0.006` n `6`; index avg `-0.1604` n `25`; metal avg `0.0815` n `20`; unknown avg `0.2042` n `766`
- 4h: commodity avg `-0.0466` n `12`; crypto_alt avg `-0.4945` n `230`; crypto_major avg `-0.3937` n `8`; equity avg `-1.3079` n `92`; fx avg `0.0528` n `6`; index avg `-0.2869` n `25`; metal avg `-0.1505` n `20`; unknown avg `0.045` n `765`
- 24h: commodity avg `0.1343` n `12`; crypto_alt avg `-0.7022` n `230`; crypto_major avg `-0.0506` n `8`; equity avg `-1.2809` n `92`; fx avg `0.006` n `6`; index avg `-0.2597` n `25`; metal avg `-0.2088` n `20`; unknown avg `0.29` n `741`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1911`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1875`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1392`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.13`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1146`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1127`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1063`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1019`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0936`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0881`, n `668`, weak_sample_signal
