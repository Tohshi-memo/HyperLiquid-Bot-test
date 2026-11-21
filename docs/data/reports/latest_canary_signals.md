# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-21T14:22:24.283598+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `3.5384` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `3.3656` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `2.5715` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0128` n `13`; crypto_alt avg `-0.0575` n `239`; crypto_major avg `-0.0395` n `8`; equity avg `-0.1164` n `166`; fx avg `-0.0003` n `6`; index avg `-0.0092` n `27`; metal avg `-0.0116` n `20`; unknown avg `0.1252` n `1260`
- 1h: commodity avg `0.0262` n `13`; crypto_alt avg `1.1964` n `239`; crypto_major avg `1.5116` n `8`; equity avg `0.5222` n `166`; fx avg `0.0021` n `6`; index avg `0.0635` n `27`; metal avg `0.0637` n `20`; unknown avg `0.6444` n `1260`
- 4h: commodity avg `-0.043` n `13`; crypto_alt avg `2.4978` n `239`; crypto_major avg `3.4954` n `8`; equity avg `0.9239` n `166`; fx avg `-0.021` n `6`; index avg `0.1298` n `27`; metal avg `0.1298` n `20`; unknown avg `163.7616` n `1226`
- 24h: commodity avg `0.5305` n `13`; crypto_alt avg `-2.2072` n `239`; crypto_major avg `-2.3251` n `8`; equity avg `-3.71` n `166`; fx avg `-0.1029` n `6`; index avg `-0.394` n `27`; metal avg `-0.2744` n `20`; unknown avg `0.5094` n `1145`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1515`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1492`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1385`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1215`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1103`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1064`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1043`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0941`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0932`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0865`, n `668`, weak_sample_signal
