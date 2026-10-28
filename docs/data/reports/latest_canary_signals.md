# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-28T03:07:28.743131+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.59` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0111` n `13`; crypto_alt avg `-0.079` n `238`; crypto_major avg `-0.0401` n `8`; equity avg `-0.0352` n `154`; fx avg `0.0006` n `6`; index avg `-0.0073` n `27`; metal avg `-0.0177` n `20`; unknown avg `0.947` n `1230`
- 1h: commodity avg `-0.0743` n `13`; crypto_alt avg `-0.0295` n `238`; crypto_major avg `0.072` n `8`; equity avg `0.1692` n `154`; fx avg `0.0321` n `6`; index avg `0.0155` n `27`; metal avg `-0.0054` n `20`; unknown avg `0.755` n `1226`
- 4h: commodity avg `0.1828` n `13`; crypto_alt avg `0.3402` n `238`; crypto_major avg `0.1538` n `8`; equity avg `0.9201` n `154`; fx avg `0.1311` n `6`; index avg `0.1461` n `27`; metal avg `-0.148` n `20`; unknown avg `1.6471` n `1220`
- 24h: commodity avg `0.0316` n `13`; crypto_alt avg `2.4791` n `237`; crypto_major avg `2.0869` n `8`; equity avg `2.4602` n `154`; fx avg `0.0664` n `6`; index avg `0.4931` n `27`; metal avg `0.2319` n `20`; unknown avg `174.7205` n `1020`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2136`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1845`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1795`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1462`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1159`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.086`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0807`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0802`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0684`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0682`, n `668`, weak_sample_signal
