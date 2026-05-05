# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-05T15:45:37.838859+00:00`
- Correlation status: `ready`
- Asset price records: `371`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0177` n `7`; crypto_alt avg `-0.0063` n `223`; crypto_major avg `-0.0229` n `7`; equity avg `0.0721` n `47`; fx avg `0.0141` n `4`; index avg `-0.0147` n `6`; metal avg `-0.0952` n `7`; unknown avg `0.069` n `313`
- 1h: commodity avg `-0.3414` n `7`; crypto_alt avg `-0.2272` n `223`; crypto_major avg `0.2182` n `7`; equity avg `0.2212` n `47`; fx avg `-0.1429` n `4`; index avg `0.2208` n `6`; metal avg `-0.152` n `7`; unknown avg `-0.0173` n `313`
- 4h: commodity avg `-0.8838` n `7`; crypto_alt avg `-0.0838` n `223`; crypto_major avg `0.5776` n `7`; equity avg `0.8248` n `47`; fx avg `-0.1045` n `4`; index avg `0.9054` n `6`; metal avg `0.0254` n `7`; unknown avg `0.2062` n `312`
- 24h: commodity avg `-1.3207` n `7`; crypto_alt avg `1.8116` n `223`; crypto_major avg `2.4152` n `7`; equity avg `1.4071` n `47`; fx avg `-0.0552` n `4`; index avg `1.0447` n `6`; metal avg `1.1277` n `7`; unknown avg `0.9767` n `310`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.208`, n `368`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2009`, n `368`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1333`, n `368`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1293`, n `368`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1058`, n `368`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1058`, n `364`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1051`, n `368`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1044`, n `368`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.103`, n `368`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0976`, n `364`, weak_sample_signal
