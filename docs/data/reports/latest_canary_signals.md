# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-01T08:52:26.083634+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0031` n `13`; crypto_alt avg `0.0776` n `238`; crypto_major avg `0.2303` n `8`; equity avg `0.0116` n `156`; fx avg `0.003` n `6`; index avg `-0.0023` n `27`; metal avg `-0.002` n `20`; unknown avg `0.0151` n `1263`
- 1h: commodity avg `0.0055` n `13`; crypto_alt avg `0.0817` n `238`; crypto_major avg `0.3697` n `8`; equity avg `0.1181` n `156`; fx avg `-0.0002` n `6`; index avg `0.0029` n `27`; metal avg `-0.002` n `20`; unknown avg `-0.095` n `1241`
- 4h: commodity avg `0.0146` n `13`; crypto_alt avg `0.237` n `238`; crypto_major avg `0.3402` n `8`; equity avg `0.1476` n `156`; fx avg `0.0041` n `6`; index avg `0.0185` n `27`; metal avg `0.0156` n `20`; unknown avg `81.1371` n `1222`
- 24h: commodity avg `-0.035` n `13`; crypto_alt avg `0.9701` n `238`; crypto_major avg `1.0315` n `8`; equity avg `0.4872` n `156`; fx avg `-0.0123` n `6`; index avg `0.0149` n `27`; metal avg `0.0788` n `20`; unknown avg `2.6023` n `996`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1454`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1447`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1433`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1419`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1342`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1139`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1116`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0999`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.083`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0824`, n `668`, weak_sample_signal
