# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-05T07:15:30.904993+00:00`
- Correlation status: `ready`
- Asset price records: `339`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0759` n `7`; crypto_alt avg `0.0123` n `223`; crypto_major avg `-0.0406` n `7`; equity avg `0.134` n `47`; fx avg `0.0059` n `4`; index avg `0.0545` n `6`; metal avg `0.1315` n `7`; unknown avg `0.0737` n `312`
- 1h: commodity avg `-0.1308` n `7`; crypto_alt avg `0.0023` n `223`; crypto_major avg `0.2327` n `7`; equity avg `0.35` n `47`; fx avg `-0.0062` n `4`; index avg `0.1929` n `6`; metal avg `0.3457` n `7`; unknown avg `0.0476` n `312`
- 4h: commodity avg `0.0467` n `7`; crypto_alt avg `0.2359` n `223`; crypto_major avg `0.5837` n `7`; equity avg `0.7944` n `47`; fx avg `-0.0004` n `4`; index avg `0.415` n `6`; metal avg `0.3435` n `7`; unknown avg `1.5132` n `310`
- 24h: commodity avg `0.7076` n `7`; crypto_alt avg `0.8612` n `223`; crypto_major avg `0.5427` n `7`; equity avg `0.0004` n `47`; fx avg `-0.0313` n `4`; index avg `-0.0886` n `6`; metal avg `-0.6593` n `7`; unknown avg `1.198` n `310`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2209`, n `335`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2141`, n `335`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1392`, n `335`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1348`, n `335`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1266`, n `335`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1103`, n `335`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1081`, n `335`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1073`, n `335`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1044`, n `331`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0957`, n `331`, weak_sample_signal
