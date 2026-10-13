# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-13T19:07:25.807368+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0108` n `13`; crypto_alt avg `0.2415` n `235`; crypto_major avg `0.0793` n `8`; equity avg `0.0096` n `151`; fx avg `-0.0005` n `6`; index avg `0.0056` n `26`; metal avg `-0.0098` n `20`; unknown avg `0.2124` n `1133`
- 1h: commodity avg `0.0194` n `13`; crypto_alt avg `0.2287` n `235`; crypto_major avg `0.1401` n `8`; equity avg `-0.0688` n `151`; fx avg `0.0215` n `6`; index avg `-0.003` n `26`; metal avg `0.0153` n `20`; unknown avg `-0.3223` n `1133`
- 4h: commodity avg `0.2751` n `13`; crypto_alt avg `0.2803` n `235`; crypto_major avg `-0.0464` n `8`; equity avg `0.3526` n `151`; fx avg `0.0142` n `6`; index avg `0.0661` n `26`; metal avg `-0.055` n `20`; unknown avg `0.484` n `1123`
- 24h: commodity avg `0.6079` n `13`; crypto_alt avg `-1.134` n `235`; crypto_major avg `-0.0577` n `8`; equity avg `-0.8443` n `151`; fx avg `0.1788` n `6`; index avg `-0.1578` n `26`; metal avg `-0.1965` n `20`; unknown avg `0.2379` n `1006`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1618`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1453`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1245`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1202`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1073`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.092`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.09`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.086`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0854`, n `666`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0823`, n `668`, weak_sample_signal
