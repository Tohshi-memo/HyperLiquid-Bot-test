# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-22T09:37:26.302942+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.76` - Polymarket crypto volume is unusually high.
- 4h_index_leads_crypto: score `1.0053` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0761` n `13`; crypto_alt avg `-0.1975` n `237`; crypto_major avg `-0.1202` n `8`; equity avg `-0.0035` n `151`; fx avg `-0.0096` n `6`; index avg `-0.004` n `26`; metal avg `-0.0169` n `20`; unknown avg `-0.1983` n `1169`
- 1h: commodity avg `-0.0812` n `13`; crypto_alt avg `0.1187` n `237`; crypto_major avg `-0.0137` n `8`; equity avg `-0.0147` n `151`; fx avg `-0.0266` n `6`; index avg `-0.0075` n `26`; metal avg `-0.0197` n `20`; unknown avg `15.2916` n `1105`
- 4h: commodity avg `0.1028` n `13`; crypto_alt avg `-1.3111` n `237`; crypto_major avg `-1.0758` n `8`; equity avg `-0.5475` n `151`; fx avg `-0.0982` n `6`; index avg `-0.0705` n `26`; metal avg `-0.1205` n `20`; unknown avg `8.9861` n `1073`
- 24h: commodity avg `-0.2033` n `13`; crypto_alt avg `-2.7365` n `237`; crypto_major avg `-2.1409` n `8`; equity avg `-2.4688` n `151`; fx avg `-0.1349` n `6`; index avg `-0.3955` n `26`; metal avg `-0.6165` n `20`; unknown avg `15.7909` n `898`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1563`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.152`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1393`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1366`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1269`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1247`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1207`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1199`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1125`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1056`, n `668`, weak_sample_signal
