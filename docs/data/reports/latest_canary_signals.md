# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-03T19:00:27.379845+00:00`
- Correlation status: `ready`
- Asset price records: `195`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0919` n `7`; crypto_alt avg `0.0186` n `223`; crypto_major avg `0.0663` n `7`; equity avg `0.0241` n `42`; fx avg `0.0064` n `4`; index avg `0.0063` n `9`; metal avg `-0.0803` n `7`; unknown avg `0.0969` n `314`
- 1h: commodity avg `0.2071` n `7`; crypto_alt avg `0.0954` n `223`; crypto_major avg `0.0064` n `7`; equity avg `0.0418` n `42`; fx avg `-0.0336` n `4`; index avg `-0.0053` n `9`; metal avg `-0.0003` n `7`; unknown avg `0.1169` n `314`
- 4h: commodity avg `0.3945` n `7`; crypto_alt avg `0.1181` n `223`; crypto_major avg `-0.052` n `7`; equity avg `0.2726` n `42`; fx avg `-0.0312` n `4`; index avg `0.0771` n `9`; metal avg `0.1496` n `7`; unknown avg `0.3869` n `313`
- 24h: commodity avg `-0.0462` n `7`; crypto_alt avg `-0.0723` n `223`; crypto_major avg `0.0083` n `7`; equity avg `0.5004` n `42`; fx avg `0.0437` n `4`; index avg `0.0586` n `9`; metal avg `0.4071` n `7`; unknown avg `0.0728` n `311`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.3989`, n `191`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.381`, n `191`, moderate_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.3769`, n `191`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.3744`, n `187`, moderate_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.367`, n `187`, moderate_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.3634`, n `191`, moderate_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.3272`, n `191`, moderate_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.3081`, n `191`, moderate_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.3047`, n `191`, moderate_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.2641`, n `187`, moderate_sample_signal
