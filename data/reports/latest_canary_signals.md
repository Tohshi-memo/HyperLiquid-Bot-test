# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-20T04:22:30.515566+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0063` n `13`; crypto_alt avg `0.1317` n `237`; crypto_major avg `0.1304` n `8`; equity avg `0.006` n `151`; fx avg `-0.0079` n `6`; index avg `0.0299` n `26`; metal avg `0.015` n `20`; unknown avg `0.0606` n `1198`
- 1h: commodity avg `-0.0765` n `13`; crypto_alt avg `0.5322` n `237`; crypto_major avg `0.3639` n `8`; equity avg `-0.2897` n `151`; fx avg `-0.0012` n `6`; index avg `-0.0483` n `26`; metal avg `0.0252` n `20`; unknown avg `0.252` n `1190`
- 4h: commodity avg `0.0618` n `13`; crypto_alt avg `1.0524` n `237`; crypto_major avg `0.7663` n `8`; equity avg `0.154` n `151`; fx avg `0.0228` n `6`; index avg `-0.0052` n `26`; metal avg `0.1961` n `20`; unknown avg `10.0227` n `1190`
- 24h: commodity avg `0.2402` n `13`; crypto_alt avg `0.9718` n `237`; crypto_major avg `0.0106` n `8`; equity avg `-1.0374` n `151`; fx avg `-0.0216` n `6`; index avg `-0.1824` n `26`; metal avg `-0.1807` n `20`; unknown avg `5.0775` n `1012`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1935`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.139`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1237`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1041`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1011`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0888`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0876`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0789`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0744`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0731`, n `668`, weak_sample_signal
