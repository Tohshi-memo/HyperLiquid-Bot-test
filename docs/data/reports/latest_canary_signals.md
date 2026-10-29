# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-29T06:07:28.306389+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0137` n `13`; crypto_alt avg `-0.1769` n `238`; crypto_major avg `-0.0884` n `8`; equity avg `-0.016` n `155`; fx avg `-0.0037` n `6`; index avg `0.0045` n `27`; metal avg `-0.055` n `20`; unknown avg `1.0599` n `1212`
- 1h: commodity avg `-0.0366` n `13`; crypto_alt avg `-0.2126` n `238`; crypto_major avg `-0.1785` n `8`; equity avg `-0.122` n `155`; fx avg `-0.0084` n `6`; index avg `0.0245` n `27`; metal avg `-0.1765` n `20`; unknown avg `1.3182` n `1210`
- 4h: commodity avg `-0.0676` n `13`; crypto_alt avg `0.273` n `238`; crypto_major avg `0.5666` n `8`; equity avg `0.5137` n `155`; fx avg `-0.0137` n `6`; index avg `0.183` n `27`; metal avg `-0.314` n `20`; unknown avg `2.7013` n `1174`
- 24h: commodity avg `-0.166` n `13`; crypto_alt avg `-1.8146` n `238`; crypto_major avg `-1.0525` n `8`; equity avg `-0.8952` n `154`; fx avg `0.0456` n `6`; index avg `0.0177` n `27`; metal avg `-0.3043` n `20`; unknown avg `31.1406` n `970`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1215`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.114`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0903`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0881`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0859`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0776`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0737`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0718`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0702`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0637`, n `668`, weak_sample_signal
