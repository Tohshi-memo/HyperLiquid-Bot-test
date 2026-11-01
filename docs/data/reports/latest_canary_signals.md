# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-01T23:37:25.682489+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0248` n `13`; crypto_alt avg `0.1048` n `238`; crypto_major avg `0.1526` n `8`; equity avg `0.0402` n `156`; fx avg `0.0011` n `6`; index avg `-0.0031` n `27`; metal avg `0.0184` n `20`; unknown avg `-0.1007` n `1263`
- 1h: commodity avg `-0.0546` n `13`; crypto_alt avg `0.6015` n `238`; crypto_major avg `0.5717` n `8`; equity avg `0.1415` n `156`; fx avg `0.0239` n `6`; index avg `-0.0049` n `27`; metal avg `0.1179` n `20`; unknown avg `160.8681` n `1243`
- 4h: commodity avg `-0.041` n `13`; crypto_alt avg `0.5239` n `238`; crypto_major avg `0.4523` n `8`; equity avg `0.1591` n `156`; fx avg `0.0` n `6`; index avg `0.0063` n `27`; metal avg `0.1053` n `20`; unknown avg `334.949` n `1205`
- 24h: commodity avg `-0.0346` n `13`; crypto_alt avg `-0.2908` n `238`; crypto_major avg `0.18` n `8`; equity avg `0.3997` n `156`; fx avg `0.0127` n `6`; index avg `0.0492` n `27`; metal avg `0.1304` n `20`; unknown avg `3.365` n `1084`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `0.1515`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.151`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1467`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1436`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1371`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.128`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1079`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0873`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0857`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0826`, n `668`, weak_sample_signal
