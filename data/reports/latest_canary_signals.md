# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-13T09:22:28.052212+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0052` n `13`; crypto_alt avg `-0.136` n `239`; crypto_major avg `0.0561` n `8`; equity avg `0.1115` n `162`; fx avg `0.0033` n `6`; index avg `0.0089` n `27`; metal avg `-0.0448` n `20`; unknown avg `0.1544` n `1260`
- 1h: commodity avg `0.0817` n `13`; crypto_alt avg `0.1774` n `239`; crypto_major avg `0.4835` n `8`; equity avg `0.1922` n `162`; fx avg `0.001` n `6`; index avg `0.0142` n `27`; metal avg `0.0571` n `20`; unknown avg `0.2853` n `1258`
- 4h: commodity avg `0.0799` n `13`; crypto_alt avg `1.3072` n `239`; crypto_major avg `0.5851` n `8`; equity avg `0.0928` n `162`; fx avg `0.0457` n `6`; index avg `0.0147` n `27`; metal avg `-0.2182` n `20`; unknown avg `171.7441` n `1168`
- 24h: commodity avg `0.6194` n `13`; crypto_alt avg `-0.9574` n `239`; crypto_major avg `-3.0317` n `8`; equity avg `-1.2278` n `162`; fx avg `-0.0192` n `6`; index avg `0.0124` n `27`; metal avg `-0.3998` n `20`; unknown avg `103.1267` n `1093`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1252`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.107`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0982`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0957`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0915`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0815`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0756`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0743`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0739`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0739`, n `668`, weak_sample_signal
