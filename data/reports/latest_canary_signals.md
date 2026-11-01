# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-01T18:52:23.220782+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0313` n `13`; crypto_alt avg `-0.2653` n `238`; crypto_major avg `-0.1588` n `8`; equity avg `-0.0581` n `156`; fx avg `-0.0026` n `6`; index avg `-0.0026` n `27`; metal avg `-0.0107` n `20`; unknown avg `1.2351` n `1263`
- 1h: commodity avg `0.0044` n `13`; crypto_alt avg `-0.5142` n `238`; crypto_major avg `-0.2293` n `8`; equity avg `-0.1444` n `156`; fx avg `0.0073` n `6`; index avg `-0.0246` n `27`; metal avg `-0.002` n `20`; unknown avg `160.7305` n `1249`
- 4h: commodity avg `-0.0553` n `13`; crypto_alt avg `-1.1028` n `238`; crypto_major avg `-0.4702` n `8`; equity avg `-0.14` n `156`; fx avg `0.0115` n `6`; index avg `-0.0042` n `27`; metal avg `0.0062` n `20`; unknown avg `0.1842` n `1237`
- 24h: commodity avg `0.0219` n `13`; crypto_alt avg `-0.9464` n `238`; crypto_major avg `-0.3129` n `8`; equity avg `0.2283` n `156`; fx avg `0.0176` n `6`; index avg `0.0668` n `27`; metal avg `0.0554` n `20`; unknown avg `4.268` n `1004`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `0.1499`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1492`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1443`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1412`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.141`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1291`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1021`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0919`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0859`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0831`, n `668`, weak_sample_signal
