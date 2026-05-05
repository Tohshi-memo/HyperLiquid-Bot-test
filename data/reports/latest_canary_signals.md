# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-05T21:45:36.939073+00:00`
- Correlation status: `ready`
- Asset price records: `395`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0316` n `7`; crypto_alt avg `-0.1911` n `223`; crypto_major avg `-0.0518` n `7`; equity avg `0.0985` n `47`; fx avg `0.0233` n `4`; index avg `-0.0187` n `6`; metal avg `0.0394` n `7`; unknown avg `1.0079` n `313`
- 1h: commodity avg `-0.0314` n `7`; crypto_alt avg `-0.1108` n `223`; crypto_major avg `-0.199` n `7`; equity avg `0.2381` n `47`; fx avg `0.0883` n `4`; index avg `0.045` n `6`; metal avg `0.0994` n `7`; unknown avg `1.1124` n `313`
- 4h: commodity avg `0.0215` n `7`; crypto_alt avg `1.0365` n `223`; crypto_major avg `0.352` n `7`; equity avg `0.4086` n `47`; fx avg `0.0913` n `4`; index avg `0.1483` n `6`; metal avg `-0.1067` n `7`; unknown avg `1.3718` n `313`
- 24h: commodity avg `-1.1203` n `7`; crypto_alt avg `2.0642` n `223`; crypto_major avg `2.1449` n `7`; equity avg `2.3178` n `47`; fx avg `0.046` n `4`; index avg `1.6568` n `6`; metal avg `0.7031` n `7`; unknown avg `3.2023` n `310`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2066`, n `391`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1998`, n `391`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1307`, n `391`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1266`, n `391`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1109`, n `387`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1106`, n `391`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1069`, n `391`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1028`, n `387`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.101`, n `391`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1001`, n `391`, weak_sample_signal
