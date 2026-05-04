# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-04T00:30:30.056760+00:00`
- Correlation status: `ready`
- Asset price records: `217`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0183` n `7`; crypto_alt avg `-0.1727` n `223`; crypto_major avg `-0.2565` n `7`; equity avg `-0.0112` n `42`; fx avg `0.0058` n `4`; index avg `0.037` n `9`; metal avg `-0.2511` n `7`; unknown avg `-0.0299` n `314`
- 1h: commodity avg `0.157` n `7`; crypto_alt avg `-0.4792` n `223`; crypto_major avg `-0.4584` n `7`; equity avg `0.0867` n `42`; fx avg `0.0013` n `4`; index avg `0.0577` n `9`; metal avg `-0.3227` n `7`; unknown avg `-0.0239` n `314`
- 4h: commodity avg `0.2539` n `7`; crypto_alt avg `-0.9989` n `223`; crypto_major avg `-0.7239` n `7`; equity avg `-0.0996` n `42`; fx avg `-0.0529` n `4`; index avg `0.0988` n `9`; metal avg `-0.3189` n `7`; unknown avg `0.0384` n `314`
- 24h: commodity avg `0.1468` n `7`; crypto_alt avg `-0.9448` n `223`; crypto_major avg `-0.4133` n `7`; equity avg `0.0408` n `42`; fx avg `-0.0196` n `4`; index avg `0.1623` n `9`; metal avg `0.1151` n `7`; unknown avg `0.0146` n `311`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.3871`, n `213`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.3705`, n `213`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.3019`, n `209`, moderate_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.3011`, n `209`, moderate_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.2902`, n `213`, moderate_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.2796`, n `213`, moderate_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.2739`, n `209`, moderate_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.2687`, n `209`, moderate_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.2304`, n `213`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.2175`, n `213`, weak_sample_signal
