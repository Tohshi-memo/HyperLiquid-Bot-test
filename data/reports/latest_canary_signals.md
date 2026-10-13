# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-13T18:07:36.122265+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0169` n `13`; crypto_alt avg `0.5105` n `235`; crypto_major avg `0.4076` n `8`; equity avg `0.3188` n `151`; fx avg `-0.0056` n `6`; index avg `0.061` n `26`; metal avg `0.1156` n `20`; unknown avg `33.5143` n `1133`
- 1h: commodity avg `0.0534` n `13`; crypto_alt avg `0.2307` n `235`; crypto_major avg `0.1229` n `8`; equity avg `0.1502` n `151`; fx avg `0.0164` n `6`; index avg `0.0167` n `26`; metal avg `0.0327` n `20`; unknown avg `3.8426` n `1133`
- 4h: commodity avg `0.1904` n `13`; crypto_alt avg `-0.0081` n `235`; crypto_major avg `-0.1536` n `8`; equity avg `0.1963` n `151`; fx avg `-0.0072` n `6`; index avg `0.0198` n `26`; metal avg `-0.1315` n `20`; unknown avg `1.213` n `1099`
- 24h: commodity avg `0.5343` n `13`; crypto_alt avg `-1.3645` n `235`; crypto_major avg `-0.2656` n `8`; equity avg `-0.8537` n `151`; fx avg `0.1578` n `6`; index avg `-0.1677` n `26`; metal avg `-0.2482` n `20`; unknown avg `1.5116` n `1006`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1639`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.148`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1252`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1221`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.108`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0944`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0916`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0902`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0856`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0838`, n `668`, weak_sample_signal
