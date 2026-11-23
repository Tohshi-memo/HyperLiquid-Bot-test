# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-23T01:22:27.493127+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.01` n `13`; crypto_alt avg `0.0504` n `239`; crypto_major avg `0.0327` n `8`; equity avg `-0.0062` n `166`; fx avg `0.0074` n `6`; index avg `-0.012` n `27`; metal avg `0.0712` n `20`; unknown avg `0.018` n `1263`
- 1h: commodity avg `0.0605` n `13`; crypto_alt avg `-0.2336` n `239`; crypto_major avg `-0.3198` n `8`; equity avg `-0.2109` n `166`; fx avg `0.0819` n `6`; index avg `-0.0411` n `27`; metal avg `0.0443` n `20`; unknown avg `-0.0378` n `1257`
- 4h: commodity avg `-0.3148` n `13`; crypto_alt avg `-0.3727` n `239`; crypto_major avg `-0.2696` n `8`; equity avg `0.2751` n `166`; fx avg `0.1571` n `6`; index avg `0.0757` n `27`; metal avg `0.3397` n `20`; unknown avg `164.5574` n `1216`
- 24h: commodity avg `-0.4582` n `13`; crypto_alt avg `0.4387` n `239`; crypto_major avg `0.5802` n `8`; equity avg `0.9665` n `166`; fx avg `0.1458` n `6`; index avg `0.1161` n `27`; metal avg `0.3126` n `20`; unknown avg `241.6544` n `1033`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `-0.1676`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1656`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1558`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1482`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1448`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1415`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1227`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1218`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1185`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1179`, n `668`, weak_sample_signal
