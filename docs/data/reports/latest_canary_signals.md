# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-28T23:37:29.217440+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.19` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.006` n `12`; crypto_alt avg `0.052` n `231`; crypto_major avg `0.0542` n `8`; equity avg `0.0073` n `127`; fx avg `0.0055` n `6`; index avg `-0.0015` n `26`; metal avg `0.0286` n `20`; unknown avg `-0.0049` n `793`
- 1h: commodity avg `-0.0385` n `12`; crypto_alt avg `0.3896` n `231`; crypto_major avg `0.1525` n `8`; equity avg `0.0102` n `127`; fx avg `-0.0051` n `6`; index avg `-0.0037` n `26`; metal avg `0.0177` n `20`; unknown avg `0.2151` n `793`
- 4h: commodity avg `-0.0193` n `12`; crypto_alt avg `0.5105` n `231`; crypto_major avg `0.2834` n `8`; equity avg `0.0128` n `127`; fx avg `-0.0185` n `6`; index avg `-0.0188` n `26`; metal avg `0.008` n `20`; unknown avg `0.1335` n `793`
- 24h: commodity avg `-0.1187` n `12`; crypto_alt avg `-2.9922` n `231`; crypto_major avg `-3.5693` n `8`; equity avg `-1.9683` n `127`; fx avg `-0.1375` n `6`; index avg `-0.1742` n `26`; metal avg `-0.3227` n `20`; unknown avg `-0.6098` n `760`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1279`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1119`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1096`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1056`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1026`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0934`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0877`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0781`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0778`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0711`, n `668`, weak_sample_signal
