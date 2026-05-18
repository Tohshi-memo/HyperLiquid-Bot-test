# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-18T06:07:13.692019+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1556` n `12`; crypto_alt avg `-0.1785` n `228`; crypto_major avg `-0.167` n `8`; equity avg `-0.1064` n `66`; fx avg `-0.0079` n `5`; index avg `-0.1001` n `23`; metal avg `-0.0894` n `18`; unknown avg `0.1141` n `363`
- 1h: commodity avg `0.0217` n `12`; crypto_alt avg `-0.6256` n `228`; crypto_major avg `-0.4896` n `8`; equity avg `-0.1007` n `66`; fx avg `-0.0302` n `5`; index avg `-0.0551` n `23`; metal avg `-0.1116` n `18`; unknown avg `-0.0635` n `363`
- 4h: commodity avg `-0.0817` n `12`; crypto_alt avg `-0.4876` n `228`; crypto_major avg `-0.6464` n `8`; equity avg `0.1646` n `66`; fx avg `-0.0235` n `5`; index avg `0.1279` n `23`; metal avg `0.2368` n `18`; unknown avg `-0.2019` n `363`
- 24h: commodity avg `2.7078` n `12`; crypto_alt avg `-11.1995` n `228`; crypto_major avg `-3.655` n `8`; equity avg `-3.1242` n `65`; fx avg `-0.0932` n `5`; index avg `-1.768` n `23`; metal avg `-6.2926` n `18`; unknown avg `-1.1259` n `357`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1447`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1221`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1058`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.105`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1033`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.097`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0947`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0933`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0915`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0883`, n `668`, weak_sample_signal
