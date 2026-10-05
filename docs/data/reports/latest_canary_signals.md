# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-05T11:07:34.964471+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0612` n `13`; crypto_alt avg `-0.1812` n `235`; crypto_major avg `-0.1076` n `8`; equity avg `-0.0737` n `144`; fx avg `-0.0201` n `6`; index avg `0.0081` n `26`; metal avg `0.0392` n `20`; unknown avg `0.2534` n `1077`
- 1h: commodity avg `-0.0147` n `13`; crypto_alt avg `-0.1642` n `235`; crypto_major avg `-0.0897` n `8`; equity avg `-0.1169` n `144`; fx avg `-0.0246` n `6`; index avg `0.0114` n `26`; metal avg `0.02` n `20`; unknown avg `0.1352` n `1077`
- 4h: commodity avg `0.124` n `13`; crypto_alt avg `-0.3779` n `235`; crypto_major avg `-0.2362` n `8`; equity avg `-0.2911` n `144`; fx avg `0.0205` n `6`; index avg `-0.0503` n `26`; metal avg `0.0507` n `20`; unknown avg `24.3629` n `997`
- 24h: commodity avg `-0.1448` n `13`; crypto_alt avg `0.8581` n `235`; crypto_major avg `0.9272` n `8`; equity avg `0.0052` n `144`; fx avg `-0.0822` n `6`; index avg `-0.0776` n `26`; metal avg `0.2703` n `20`; unknown avg `0.5533` n `878`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.2099`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1914`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1819`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1493`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1416`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1009`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0967`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0917`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0907`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0902`, n `668`, weak_sample_signal
