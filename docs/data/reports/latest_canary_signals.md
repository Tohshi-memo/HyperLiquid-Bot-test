# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-22T23:52:29.334472+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0267` n `13`; crypto_alt avg `0.1561` n `237`; crypto_major avg `0.1229` n `8`; equity avg `0.0491` n `151`; fx avg `0.0004` n `6`; index avg `0.0176` n `26`; metal avg `-0.0063` n `20`; unknown avg `0.0763` n `1233`
- 1h: commodity avg `0.0532` n `13`; crypto_alt avg `0.0611` n `237`; crypto_major avg `0.1015` n `8`; equity avg `-0.3218` n `151`; fx avg `-0.0008` n `6`; index avg `-0.0289` n `26`; metal avg `-0.0355` n `20`; unknown avg `0.1094` n `1231`
- 4h: commodity avg `0.0321` n `13`; crypto_alt avg `-0.1027` n `237`; crypto_major avg `-0.0482` n `8`; equity avg `-0.6384` n `151`; fx avg `-0.0216` n `6`; index avg `-0.0591` n `26`; metal avg `-0.0354` n `20`; unknown avg `-0.0007` n `1127`
- 24h: commodity avg `0.5179` n `13`; crypto_alt avg `-4.8524` n `237`; crypto_major avg `-3.4525` n `8`; equity avg `-5.2784` n `151`; fx avg `-0.1664` n `6`; index avg `-0.5806` n `26`; metal avg `-1.0033` n `20`; unknown avg `54.4112` n `905`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2027`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1806`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1636`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1606`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1553`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1515`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1433`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1276`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1108`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1103`, n `668`, weak_sample_signal
