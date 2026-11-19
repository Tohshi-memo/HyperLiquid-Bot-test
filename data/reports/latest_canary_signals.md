# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-19T21:07:27.903680+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0124` n `13`; crypto_alt avg `-0.2076` n `239`; crypto_major avg `-0.3764` n `8`; equity avg `-0.8564` n `165`; fx avg `-0.002` n `6`; index avg `-0.077` n `27`; metal avg `-0.0728` n `20`; unknown avg `11.8086` n `1236`
- 1h: commodity avg `0.042` n `13`; crypto_alt avg `-0.283` n `239`; crypto_major avg `-0.294` n `8`; equity avg `-0.8246` n `165`; fx avg `0.0041` n `6`; index avg `-0.0538` n `27`; metal avg `-0.1059` n `20`; unknown avg `11.7743` n `1242`
- 4h: commodity avg `0.0275` n `13`; crypto_alt avg `0.1563` n `239`; crypto_major avg `-0.0928` n `8`; equity avg `-1.4316` n `165`; fx avg `0.0015` n `6`; index avg `-0.0923` n `27`; metal avg `-0.0342` n `20`; unknown avg `1.7545` n `1232`
- 24h: commodity avg `0.018` n `13`; crypto_alt avg `-0.7116` n `239`; crypto_major avg `-0.213` n `8`; equity avg `-2.3958` n `165`; fx avg `-0.007` n `6`; index avg `-0.1703` n `27`; metal avg `-0.5869` n `20`; unknown avg `7.4752` n `1164`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1617`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.159`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1321`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1271`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0868`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0859`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0745`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0624`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0621`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.058`, n `668`, weak_sample_signal
