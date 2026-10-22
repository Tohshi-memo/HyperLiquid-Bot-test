# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-22T22:52:26.767726+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0151` n `13`; crypto_alt avg `-0.137` n `237`; crypto_major avg `-0.1549` n `8`; equity avg `-0.054` n `151`; fx avg `0.0153` n `6`; index avg `-0.0172` n `26`; metal avg `-0.0004` n `20`; unknown avg `0.0953` n `1233`
- 1h: commodity avg `0.0319` n `13`; crypto_alt avg `-0.1973` n `237`; crypto_major avg `-0.1677` n `8`; equity avg `0.062` n `151`; fx avg `-0.0057` n `6`; index avg `0.0334` n `26`; metal avg `-0.0125` n `20`; unknown avg `0.0194` n `1191`
- 4h: commodity avg `-0.0285` n `13`; crypto_alt avg `-0.3178` n `237`; crypto_major avg `-0.1793` n `8`; equity avg `-0.1024` n `151`; fx avg `-0.0285` n `6`; index avg `-0.0082` n `26`; metal avg `-0.0329` n `20`; unknown avg `-0.1066` n `1127`
- 24h: commodity avg `0.4639` n `13`; crypto_alt avg `-4.9077` n `237`; crypto_major avg `-3.5498` n `8`; equity avg `-4.9811` n `151`; fx avg `-0.1657` n `6`; index avg `-0.5521` n `26`; metal avg `-0.969` n `20`; unknown avg `54.1638` n `905`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1903`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1713`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1534`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1529`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1526`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1515`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1341`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1203`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1104`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1065`, n `668`, weak_sample_signal
