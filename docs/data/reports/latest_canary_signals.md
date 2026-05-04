# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-04T09:45:22.573085+00:00`
- Correlation status: `ready`
- Asset price records: `254`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.072` n `7`; crypto_alt avg `0.3736` n `223`; crypto_major avg `0.3172` n `7`; equity avg `0.0168` n `42`; fx avg `-0.0042` n `4`; index avg `0.032` n `9`; metal avg `0.0162` n `7`; unknown avg `0.2165` n `314`
- 1h: commodity avg `-0.0938` n `7`; crypto_alt avg `0.5448` n `223`; crypto_major avg `0.308` n `7`; equity avg `0.1149` n `42`; fx avg `0.0064` n `4`; index avg `-0.1083` n `9`; metal avg `0.0515` n `7`; unknown avg `0.2037` n `314`
- 4h: commodity avg `0.5536` n `7`; crypto_alt avg `0.0872` n `223`; crypto_major avg `-0.4053` n `7`; equity avg `-0.1102` n `42`; fx avg `0.0143` n `4`; index avg `-0.2596` n `9`; metal avg `-0.8692` n `7`; unknown avg `0.0428` n `312`
- 24h: commodity avg `0.493` n `7`; crypto_alt avg `2.3106` n `223`; crypto_major avg `2.0359` n `7`; equity avg `1.0728` n `42`; fx avg `-0.0425` n `4`; index avg `0.6399` n `9`; metal avg `-0.9214` n `7`; unknown avg `0.3308` n `311`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.3348`, n `250`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.324`, n `250`, moderate_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.2514`, n `246`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.2486`, n `246`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.2152`, n `246`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.203`, n `246`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1911`, n `250`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1779`, n `246`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1776`, n `250`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1716`, n `250`, weak_sample_signal
