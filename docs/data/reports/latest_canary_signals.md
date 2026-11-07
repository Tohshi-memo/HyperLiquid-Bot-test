# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-07T19:37:31.048636+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0653` n `13`; crypto_alt avg `-0.0917` n `239`; crypto_major avg `-0.0355` n `8`; equity avg `0.0363` n `158`; fx avg `0.0029` n `6`; index avg `0.0016` n `27`; metal avg `0.0048` n `20`; unknown avg `0.0565` n `1262`
- 1h: commodity avg `0.0785` n `13`; crypto_alt avg `-0.2926` n `239`; crypto_major avg `-0.0892` n `8`; equity avg `-0.0485` n `158`; fx avg `0.0021` n `6`; index avg `-0.0101` n `27`; metal avg `-0.0072` n `20`; unknown avg `0.0936` n `1256`
- 4h: commodity avg `0.0999` n `13`; crypto_alt avg `0.0126` n `239`; crypto_major avg `0.0923` n `8`; equity avg `0.1808` n `158`; fx avg `-0.005` n `6`; index avg `0.0092` n `27`; metal avg `-0.0146` n `20`; unknown avg `0.8186` n `1217`
- 24h: commodity avg `0.0414` n `13`; crypto_alt avg `-1.3915` n `239`; crypto_major avg `-0.5142` n `8`; equity avg `0.4236` n `158`; fx avg `-0.0121` n `6`; index avg `0.0412` n `27`; metal avg `0.0313` n `20`; unknown avg `0.2766` n `1077`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2131`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1644`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1622`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1287`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.124`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1089`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1065`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1057`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1056`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1033`, n `668`, weak_sample_signal
