# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-22T22:37:24.539469+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0248` n `13`; crypto_alt avg `0.0159` n `237`; crypto_major avg `0.0873` n `8`; equity avg `-0.0278` n `151`; fx avg `-0.002` n `6`; index avg `-0.0128` n `26`; metal avg `-0.0128` n `20`; unknown avg `0.2054` n `1193`
- 1h: commodity avg `0.0111` n `13`; crypto_alt avg `-0.0683` n `237`; crypto_major avg `-0.0168` n `8`; equity avg `0.0084` n `151`; fx avg `-0.0217` n `6`; index avg `0.0448` n `26`; metal avg `-0.0131` n `20`; unknown avg `0.0429` n `1191`
- 4h: commodity avg `0.0024` n `13`; crypto_alt avg `-0.0306` n `237`; crypto_major avg `0.1857` n `8`; equity avg `-0.0499` n `151`; fx avg `-0.0575` n `6`; index avg `-0.0022` n `26`; metal avg `-0.064` n `20`; unknown avg `0.1713` n `1127`
- 24h: commodity avg `0.4484` n `13`; crypto_alt avg `-4.7798` n `237`; crypto_major avg `-3.401` n `8`; equity avg `-4.9301` n `151`; fx avg `-0.181` n `6`; index avg `-0.5354` n `26`; metal avg `-0.9685` n `20`; unknown avg `54.2629` n `905`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.192`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1729`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1543`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1533`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1494`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1463`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1359`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1223`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1108`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1049`, n `668`, weak_sample_signal
