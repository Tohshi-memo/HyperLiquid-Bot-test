# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-18T23:37:30.671949+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.19` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0076` n `13`; crypto_alt avg `0.2033` n `239`; crypto_major avg `0.1386` n `8`; equity avg `0.2303` n `164`; fx avg `-0.0026` n `6`; index avg `0.0295` n `27`; metal avg `0.0385` n `20`; unknown avg `1.4044` n `1265`
- 1h: commodity avg `0.0239` n `13`; crypto_alt avg `0.6641` n `239`; crypto_major avg `0.505` n `8`; equity avg `1.1435` n `164`; fx avg `0.0012` n `6`; index avg `0.1377` n `27`; metal avg `0.1783` n `20`; unknown avg `6.8562` n `1263`
- 4h: commodity avg `-0.1239` n `13`; crypto_alt avg `0.2082` n `239`; crypto_major avg `0.1621` n `8`; equity avg `1.0773` n `164`; fx avg `0.0099` n `6`; index avg `0.1445` n `27`; metal avg `0.2332` n `20`; unknown avg `5.0703` n `1219`
- 24h: commodity avg `-0.2483` n `13`; crypto_alt avg `-1.4744` n `239`; crypto_major avg `-2.3615` n `8`; equity avg `-1.9641` n `164`; fx avg `-0.1558` n `6`; index avg `-0.1394` n `27`; metal avg `-1.0453` n `20`; unknown avg `47.7195` n `1126`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.1103`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0779`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0749`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0731`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0703`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0681`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.064`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0602`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0576`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0565`, n `668`, weak_sample_signal
