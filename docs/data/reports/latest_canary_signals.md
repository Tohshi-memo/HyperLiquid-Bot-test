# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-23T03:22:31.970865+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0149` n `13`; crypto_alt avg `-0.083` n `237`; crypto_major avg `-0.1451` n `8`; equity avg `0.0412` n `151`; fx avg `0.003` n `6`; index avg `0.0075` n `26`; metal avg `0.0029` n `20`; unknown avg `0.6387` n `1233`
- 1h: commodity avg `-0.0243` n `13`; crypto_alt avg `0.1938` n `237`; crypto_major avg `0.1176` n `8`; equity avg `0.2779` n `151`; fx avg `0.0178` n `6`; index avg `0.0555` n `26`; metal avg `0.0136` n `20`; unknown avg `2.8336` n `1229`
- 4h: commodity avg `0.1142` n `13`; crypto_alt avg `1.2755` n `237`; crypto_major avg `0.7632` n `8`; equity avg `0.8866` n `151`; fx avg `-0.002` n `6`; index avg `0.0269` n `26`; metal avg `-0.0603` n `20`; unknown avg `0.3939` n `1223`
- 24h: commodity avg `0.4635` n `13`; crypto_alt avg `-1.9324` n `237`; crypto_major avg `-1.0489` n `8`; equity avg `-3.281` n `151`; fx avg `-0.1321` n `6`; index avg `-0.4363` n `26`; metal avg `-0.637` n `20`; unknown avg `53.1916` n `903`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1743`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1709`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1637`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.153`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1493`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1451`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1359`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1169`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1166`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1065`, n `668`, weak_sample_signal
