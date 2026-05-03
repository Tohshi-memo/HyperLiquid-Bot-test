# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-03T07:45:31.145955+00:00`
- Correlation status: `ready`
- Asset price records: `150`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0072` n `7`; crypto_alt avg `0.0743` n `223`; crypto_major avg `0.0106` n `7`; equity avg `0.0225` n `42`; fx avg `0.0037` n `4`; index avg `-0.0182` n `9`; metal avg `0.0036` n `7`; unknown avg `0.0056` n `313`
- 1h: commodity avg `0.0127` n `7`; crypto_alt avg `0.4202` n `223`; crypto_major avg `0.3352` n `7`; equity avg `-0.003` n `42`; fx avg `0.013` n `4`; index avg `0.0589` n `9`; metal avg `0.039` n `7`; unknown avg `0.3004` n `313`
- 4h: commodity avg `-0.059` n `7`; crypto_alt avg `0.6685` n `223`; crypto_major avg `0.2862` n `7`; equity avg `-0.1731` n `42`; fx avg `0.0149` n `4`; index avg `0.0406` n `9`; metal avg `0.0581` n `7`; unknown avg `0.3284` n `311`
- 24h: commodity avg `-0.2022` n `7`; crypto_alt avg `1.4343` n `223`; crypto_major avg `0.0161` n `7`; equity avg `0.2306` n `42`; fx avg `0.152` n `4`; index avg `0.0688` n `9`; metal avg `0.0772` n `7`; unknown avg `0.399` n `311`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.4255`, n `146`, moderate_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.4107`, n `146`, moderate_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.4041`, n `146`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.3902`, n `142`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.3863`, n `146`, moderate_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.3853`, n `142`, moderate_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.3755`, n `142`, moderate_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.368`, n `142`, moderate_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.3623`, n `146`, moderate_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.3582`, n `146`, moderate_sample_signal
