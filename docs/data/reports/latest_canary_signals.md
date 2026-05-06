# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-06T00:15:38.536050+00:00`
- Correlation status: `ready`
- Asset price records: `405`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1583` n `7`; crypto_alt avg `0.152` n `223`; crypto_major avg `0.1367` n `7`; equity avg `0.1206` n `47`; fx avg `0.0181` n `4`; index avg `-0.0111` n `6`; metal avg `-0.1616` n `7`; unknown avg `0.0116` n `313`
- 1h: commodity avg `0.3111` n `7`; crypto_alt avg `0.0399` n `223`; crypto_major avg `-0.2271` n `7`; equity avg `0.0468` n `47`; fx avg `-0.2186` n `4`; index avg `-0.021` n `6`; metal avg `-0.1668` n `7`; unknown avg `-0.184` n `313`
- 4h: commodity avg `-0.3785` n `7`; crypto_alt avg `0.2494` n `223`; crypto_major avg `-0.1726` n `7`; equity avg `1.0724` n `47`; fx avg `-0.1005` n `4`; index avg `0.3213` n `6`; metal avg `0.6116` n `7`; unknown avg `0.2027` n `313`
- 24h: commodity avg `-1.5115` n `7`; crypto_alt avg `2.3326` n `223`; crypto_major avg `2.3804` n `7`; equity avg `3.0197` n `47`; fx avg `-0.1333` n `4`; index avg `1.8622` n `6`; metal avg `1.2246` n `7`; unknown avg `1.489` n `310`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1926`, n `401`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1863`, n `401`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1299`, n `401`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1259`, n `401`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1095`, n `401`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1074`, n `397`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.102`, n `401`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1012`, n `401`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1003`, n `401`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0998`, n `397`, weak_sample_signal
