# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-29T03:22:13.907119+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.49` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0095` n `12`; crypto_alt avg `0.114` n `231`; crypto_major avg `0.1351` n `8`; equity avg `0.0081` n `127`; fx avg `-0.0012` n `6`; index avg `0.0002` n `26`; metal avg `-0.0012` n `20`; unknown avg `0.0558` n `793`
- 1h: commodity avg `0.0041` n `12`; crypto_alt avg `0.3303` n `231`; crypto_major avg `0.2632` n `8`; equity avg `0.0489` n `127`; fx avg `0.0006` n `6`; index avg `0.0235` n `26`; metal avg `-0.0134` n `20`; unknown avg `0.0524` n `793`
- 4h: commodity avg `-0.0057` n `12`; crypto_alt avg `0.1208` n `231`; crypto_major avg `0.1258` n `8`; equity avg `0.1283` n `127`; fx avg `0.0` n `6`; index avg `0.0385` n `26`; metal avg `0.0189` n `20`; unknown avg `-0.2961` n `793`
- 24h: commodity avg `-0.1186` n `12`; crypto_alt avg `-1.7278` n `231`; crypto_major avg `-2.546` n `8`; equity avg `-2.0463` n `127`; fx avg `-0.0923` n `6`; index avg `-0.2104` n `26`; metal avg `-0.2673` n `20`; unknown avg `-0.3656` n `760`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1356`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1005`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0943`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0906`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0873`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0827`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0816`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0809`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0755`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0743`, n `668`, weak_sample_signal
