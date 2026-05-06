# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-06T05:45:18.630800+00:00`
- Correlation status: `ready`
- Asset price records: `427`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0202` n `7`; crypto_alt avg `-0.1269` n `223`; crypto_major avg `-0.1332` n `7`; equity avg `-0.0198` n `47`; fx avg `0.0063` n `4`; index avg `0.0585` n `6`; metal avg `0.0142` n `7`; unknown avg `0.0579` n `313`
- 1h: commodity avg `0.1667` n `7`; crypto_alt avg `-0.0542` n `223`; crypto_major avg `-0.0812` n `7`; equity avg `0.0462` n `47`; fx avg `0.1214` n `4`; index avg `0.0212` n `6`; metal avg `0.0241` n `7`; unknown avg `0.3238` n `313`
- 4h: commodity avg `0.2219` n `7`; crypto_alt avg `0.1722` n `223`; crypto_major avg `0.1113` n `7`; equity avg `0.7056` n `47`; fx avg `-0.1638` n `4`; index avg `0.2722` n `6`; metal avg `0.6087` n `7`; unknown avg `0.2678` n `313`
- 24h: commodity avg `-1.3434` n `7`; crypto_alt avg `2.3463` n `223`; crypto_major avg `1.4722` n `7`; equity avg `2.7391` n `47`; fx avg `-0.3679` n `4`; index avg `2.298` n `6`; metal avg `2.0049` n `7`; unknown avg `1.1587` n `310`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1809`, n `423`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1746`, n `423`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1273`, n `423`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1267`, n `423`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1228`, n `423`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1102`, n `423`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1016`, n `419`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0964`, n `419`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0959`, n `423`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0951`, n `423`, weak_sample_signal
