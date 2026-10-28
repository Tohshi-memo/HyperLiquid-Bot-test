# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-28T17:52:34.360259+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.59` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0362` n `13`; crypto_alt avg `0.277` n `238`; crypto_major avg `0.3217` n `8`; equity avg `0.1619` n `155`; fx avg `-0.0046` n `6`; index avg `0.01` n `27`; metal avg `-0.0025` n `20`; unknown avg `1.033` n `1238`
- 1h: commodity avg `-0.0503` n `13`; crypto_alt avg `-0.0806` n `238`; crypto_major avg `0.1772` n `8`; equity avg `-0.0822` n `155`; fx avg `-0.0181` n `6`; index avg `-0.0418` n `27`; metal avg `-0.0768` n `20`; unknown avg `3.028` n `1232`
- 4h: commodity avg `-0.0406` n `13`; crypto_alt avg `0.2755` n `238`; crypto_major avg `0.5418` n `8`; equity avg `0.5704` n `155`; fx avg `0.0605` n `6`; index avg `0.0824` n `27`; metal avg `-0.0949` n `20`; unknown avg `3.9827` n `1164`
- 24h: commodity avg `0.5347` n `13`; crypto_alt avg `-0.0253` n `238`; crypto_major avg `0.2628` n `8`; equity avg `1.1986` n `154`; fx avg `0.2414` n `6`; index avg `0.2611` n `27`; metal avg `-0.1624` n `20`; unknown avg `4.1936` n `1100`

## Correlations

- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1634`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1597`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1459`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1458`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1041`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0923`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0812`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0756`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0735`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0703`, n `668`, weak_sample_signal
