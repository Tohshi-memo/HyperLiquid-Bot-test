# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-23T07:37:26.661710+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0309` n `13`; crypto_alt avg `0.1076` n `237`; crypto_major avg `0.1556` n `8`; equity avg `-0.0311` n `152`; fx avg `0.0005` n `6`; index avg `-0.0062` n `26`; metal avg `0.0575` n `20`; unknown avg `0.9071` n `1233`
- 1h: commodity avg `-0.0712` n `13`; crypto_alt avg `0.135` n `237`; crypto_major avg `0.1263` n `8`; equity avg `0.001` n `152`; fx avg `-0.0287` n `6`; index avg `-0.0319` n `26`; metal avg `-0.0368` n `20`; unknown avg `0.5841` n `1231`
- 4h: commodity avg `0.0018` n `13`; crypto_alt avg `0.4291` n `237`; crypto_major avg `0.4204` n `8`; equity avg `1.2606` n `152`; fx avg `-0.0171` n `6`; index avg `0.0789` n `26`; metal avg `-0.02` n `20`; unknown avg `-0.1976` n `1204`
- 24h: commodity avg `0.1625` n `13`; crypto_alt avg `-0.1788` n `237`; crypto_major avg `-0.0479` n `8`; equity avg `-1.0226` n `152`; fx avg `-0.0631` n `6`; index avg `-0.0957` n `26`; metal avg `-0.4348` n `20`; unknown avg `52.0863` n `898`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1804`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1754`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1595`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1529`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1442`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1415`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1356`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1191`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1178`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1116`, n `668`, weak_sample_signal
