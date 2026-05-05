# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-05T16:15:21.301216+00:00`
- Correlation status: `ready`
- Asset price records: `373`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0033` n `7`; crypto_alt avg `-0.0198` n `223`; crypto_major avg `-0.061` n `7`; equity avg `-0.0495` n `47`; fx avg `-0.0044` n `4`; index avg `-0.0003` n `6`; metal avg `-0.0133` n `7`; unknown avg `-0.0002` n `313`
- 1h: commodity avg `0.0386` n `7`; crypto_alt avg `-0.0459` n `223`; crypto_major avg `-0.1013` n `7`; equity avg `-0.024` n `47`; fx avg `-0.0045` n `4`; index avg `0.1236` n `6`; metal avg `-0.2497` n `7`; unknown avg `1.2224` n `313`
- 4h: commodity avg `-0.5784` n `7`; crypto_alt avg `-0.0963` n `223`; crypto_major avg `0.2595` n `7`; equity avg `0.3515` n `47`; fx avg `-0.1186` n `4`; index avg `0.7649` n `6`; metal avg `-0.4788` n `7`; unknown avg `1.4184` n `312`
- 24h: commodity avg `-1.2261` n `7`; crypto_alt avg `1.4951` n `223`; crypto_major avg `1.8228` n `7`; equity avg `1.3905` n `47`; fx avg `-0.0476` n `4`; index avg `1.1315` n `6`; metal avg `1.0235` n `7`; unknown avg `1.8698` n `310`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2079`, n `369`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2009`, n `369`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1334`, n `369`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1293`, n `369`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1075`, n `365`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.107`, n `369`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1052`, n `369`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1045`, n `369`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1037`, n `369`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0992`, n `365`, weak_sample_signal
