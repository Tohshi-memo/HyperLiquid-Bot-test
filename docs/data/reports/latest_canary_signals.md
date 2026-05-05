# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-05T21:30:28.938117+00:00`
- Correlation status: `ready`
- Asset price records: `394`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0132` n `7`; crypto_alt avg `-0.1926` n `223`; crypto_major avg `-0.2396` n `7`; equity avg `-0.0012` n `47`; fx avg `0.0593` n `4`; index avg `0.0147` n `6`; metal avg `-0.0133` n `7`; unknown avg `0.1269` n `313`
- 1h: commodity avg `0.1006` n `7`; crypto_alt avg `0.3375` n `223`; crypto_major avg `-0.0794` n `7`; equity avg `-0.0587` n `47`; fx avg `0.0301` n `4`; index avg `0.0801` n `6`; metal avg `-0.0129` n `7`; unknown avg `0.2015` n `313`
- 4h: commodity avg `0.1314` n `7`; crypto_alt avg `1.1993` n `223`; crypto_major avg `0.3973` n `7`; equity avg `0.3363` n `47`; fx avg `0.0638` n `4`; index avg `0.1221` n `6`; metal avg `-0.17` n `7`; unknown avg `0.2553` n `313`
- 24h: commodity avg `-1.1259` n `7`; crypto_alt avg `2.2963` n `223`; crypto_major avg `2.2662` n `7`; equity avg `2.2162` n `47`; fx avg `0.019` n `4`; index avg `1.5502` n `6`; metal avg `0.678` n `7`; unknown avg `1.4853` n `310`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2067`, n `390`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1999`, n `390`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1307`, n `390`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1265`, n `390`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1111`, n `386`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.111`, n `390`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.107`, n `390`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.103`, n `386`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.101`, n `390`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1`, n `390`, weak_sample_signal
