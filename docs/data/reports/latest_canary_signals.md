# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-29T12:52:21.007434+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1065` n `12`; crypto_alt avg `0.0809` n `228`; crypto_major avg `0.1373` n `8`; equity avg `0.098` n `69`; fx avg `-0.0052` n `6`; index avg `0.0638` n `23`; metal avg `0.1738` n `18`; unknown avg `0.1032` n `417`
- 1h: commodity avg `0.032` n `12`; crypto_alt avg `-0.3566` n `228`; crypto_major avg `-0.1658` n `8`; equity avg `-0.039` n `69`; fx avg `0.0103` n `6`; index avg `-0.0079` n `23`; metal avg `-0.1592` n `18`; unknown avg `-0.1245` n `417`
- 4h: commodity avg `-0.4277` n `12`; crypto_alt avg `-0.8596` n `228`; crypto_major avg `-0.5949` n `8`; equity avg `-0.1069` n `69`; fx avg `0.0103` n `6`; index avg `0.2196` n `23`; metal avg `0.4027` n `18`; unknown avg `-0.2419` n `417`
- 24h: commodity avg `0.4115` n `12`; crypto_alt avg `0.7319` n `228`; crypto_major avg `1.438` n `8`; equity avg `2.8627` n `69`; fx avg `0.0825` n `6`; index avg `1.2349` n `23`; metal avg `1.6132` n `18`; unknown avg `0.9046` n `407`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1689`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1514`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1452`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.141`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1353`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.132`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1305`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1291`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.129`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1266`, n `668`, weak_sample_signal
