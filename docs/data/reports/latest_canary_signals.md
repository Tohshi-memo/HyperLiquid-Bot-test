# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-29T00:22:35.636116+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.071` n `13`; crypto_alt avg `-0.0931` n `238`; crypto_major avg `-0.1804` n `8`; equity avg `0.0897` n `155`; fx avg `-0.033` n `6`; index avg `0.0246` n `27`; metal avg `-0.0634` n `20`; unknown avg `0.3577` n `1238`
- 1h: commodity avg `0.0632` n `13`; crypto_alt avg `0.0103` n `238`; crypto_major avg `-0.1588` n `8`; equity avg `0.1423` n `155`; fx avg `-0.0615` n `6`; index avg `0.0403` n `27`; metal avg `-0.0981` n `20`; unknown avg `0.3277` n `1212`
- 4h: commodity avg `0.1084` n `13`; crypto_alt avg `-0.1865` n `238`; crypto_major avg `-0.1746` n `8`; equity avg `-0.2289` n `155`; fx avg `-0.0686` n `6`; index avg `-0.0491` n `27`; metal avg `-0.1592` n `20`; unknown avg `1.8722` n `1076`
- 24h: commodity avg `0.1297` n `13`; crypto_alt avg `0.5238` n `238`; crypto_major avg `0.4279` n `8`; equity avg `0.7431` n `154`; fx avg `0.1518` n `6`; index avg `0.16` n `27`; metal avg `-0.236` n `20`; unknown avg `24.7509` n `996`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1575`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1346`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1287`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1042`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0966`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0939`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0906`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0855`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0761`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0757`, n `668`, weak_sample_signal
