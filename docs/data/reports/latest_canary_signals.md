# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-16T00:07:29.333374+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0222` n `13`; crypto_alt avg `0.0119` n `239`; crypto_major avg `-0.109` n `8`; equity avg `-0.1323` n `162`; fx avg `0.0117` n `6`; index avg `-0.0317` n `27`; metal avg `-0.0376` n `20`; unknown avg `0.5979` n `1253`
- 1h: commodity avg `0.0846` n `13`; crypto_alt avg `0.0861` n `239`; crypto_major avg `-0.0473` n `8`; equity avg `0.2848` n `162`; fx avg `0.0128` n `6`; index avg `0.0338` n `27`; metal avg `0.0522` n `20`; unknown avg `0.302` n `1255`
- 4h: commodity avg `-0.2897` n `13`; crypto_alt avg `0.8097` n `239`; crypto_major avg `0.9068` n `8`; equity avg `1.197` n `162`; fx avg `0.0064` n `6`; index avg `0.1976` n `27`; metal avg `0.3691` n `20`; unknown avg `1.031` n `1187`
- 24h: commodity avg `-0.2947` n `13`; crypto_alt avg `2.5366` n `239`; crypto_major avg `3.7209` n `8`; equity avg `2.0346` n `162`; fx avg `0.0292` n `6`; index avg `0.2636` n `27`; metal avg `0.5443` n `20`; unknown avg `3.1769` n `1138`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1352`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1339`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1262`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1023`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0955`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0914`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0854`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0726`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0668`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0663`, n `668`, weak_sample_signal
