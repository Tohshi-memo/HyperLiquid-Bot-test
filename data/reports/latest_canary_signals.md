# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-13T01:52:31.011473+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0158` n `13`; crypto_alt avg `-0.1096` n `239`; crypto_major avg `-0.1961` n `8`; equity avg `-0.005` n `162`; fx avg `0.0116` n `6`; index avg `-0.0019` n `27`; metal avg `0.0295` n `20`; unknown avg `1.8226` n `1262`
- 1h: commodity avg `-0.085` n `13`; crypto_alt avg `-0.0207` n `239`; crypto_major avg `-0.2322` n `8`; equity avg `0.2248` n `162`; fx avg `-0.0438` n `6`; index avg `0.0394` n `27`; metal avg `0.2689` n `20`; unknown avg `12.9808` n `1260`
- 4h: commodity avg `-0.1613` n `13`; crypto_alt avg `-0.0432` n `239`; crypto_major avg `-0.2202` n `8`; equity avg `0.7754` n `162`; fx avg `-0.0236` n `6`; index avg `0.127` n `27`; metal avg `0.3455` n `20`; unknown avg `12.6779` n `1215`
- 24h: commodity avg `0.847` n `13`; crypto_alt avg `-0.4682` n `239`; crypto_major avg `-1.6617` n `8`; equity avg `-0.4262` n `162`; fx avg `-0.1245` n `6`; index avg `0.1124` n `27`; metal avg `-0.3593` n `20`; unknown avg `52.2202` n `1121`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1399`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1325`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1065`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0955`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0896`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0886`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0851`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0825`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0825`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0824`, n `668`, weak_sample_signal
