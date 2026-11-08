# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-08T12:52:25.880654+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0005` n `13`; crypto_alt avg `-0.0019` n `239`; crypto_major avg `0.0577` n `8`; equity avg `-0.0156` n `158`; fx avg `-0.0053` n `6`; index avg `-0.0011` n `27`; metal avg `-0.0042` n `20`; unknown avg `0.0813` n `1262`
- 1h: commodity avg `0.0188` n `13`; crypto_alt avg `-0.3311` n `239`; crypto_major avg `-0.0201` n `8`; equity avg `-0.0436` n `158`; fx avg `-0.0028` n `6`; index avg `-0.0083` n `27`; metal avg `-0.0022` n `20`; unknown avg `0.0174` n `1250`
- 4h: commodity avg `0.0334` n `13`; crypto_alt avg `-0.3311` n `239`; crypto_major avg `0.1377` n `8`; equity avg `0.1239` n `158`; fx avg `0.0085` n `6`; index avg `-0.0127` n `27`; metal avg `0.001` n `20`; unknown avg `218.8716` n `1170`
- 24h: commodity avg `0.1057` n `13`; crypto_alt avg `-1.2909` n `239`; crypto_major avg `-0.0448` n `8`; equity avg `0.1344` n `158`; fx avg `0.0044` n `6`; index avg `0.0224` n `27`; metal avg `-0.0291` n `20`; unknown avg `5.539` n `1097`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2079`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1604`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1511`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1209`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1143`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1129`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1093`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1055`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1046`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1019`, n `668`, weak_sample_signal
