# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-16T21:37:34.405060+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0749` n `13`; crypto_alt avg `0.2382` n `239`; crypto_major avg `0.2738` n `8`; equity avg `0.1292` n `162`; fx avg `0.0065` n `6`; index avg `0.0048` n `27`; metal avg `0.0401` n `20`; unknown avg `1.8524` n `1266`
- 1h: commodity avg `-0.118` n `13`; crypto_alt avg `0.2556` n `239`; crypto_major avg `0.5269` n `8`; equity avg `0.2645` n `162`; fx avg `-0.0119` n `6`; index avg `0.0246` n `27`; metal avg `0.0308` n `20`; unknown avg `1.2767` n `1230`
- 4h: commodity avg `-0.2913` n `13`; crypto_alt avg `0.2384` n `239`; crypto_major avg `0.5204` n `8`; equity avg `-0.5978` n `162`; fx avg `-0.0408` n `6`; index avg `-0.0929` n `27`; metal avg `-0.1307` n `20`; unknown avg `4.3028` n `1221`
- 24h: commodity avg `-1.2383` n `13`; crypto_alt avg `0.2499` n `239`; crypto_major avg `0.4864` n `8`; equity avg `-3.2908` n `162`; fx avg `-0.1444` n `6`; index avg `-0.3325` n `27`; metal avg `-0.3252` n `20`; unknown avg `479.1384` n `1027`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.145`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.12`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.1194`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1186`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1147`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0966`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0956`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0823`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0816`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0794`, n `668`, weak_sample_signal
