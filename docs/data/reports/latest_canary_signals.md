# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-03T14:39:16.587492+00:00`
- Correlation status: `ready`
- Asset price records: `177`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0094` n `7`; crypto_alt avg `-0.0903` n `223`; crypto_major avg `-0.0093` n `7`; equity avg `0.0843` n `42`; fx avg `0.0032` n `4`; index avg `-0.0041` n `9`; metal avg `0.014` n `7`; unknown avg `0.0011` n `313`
- 1h: commodity avg `-0.0354` n `7`; crypto_alt avg `0.0116` n `223`; crypto_major avg `0.0872` n `7`; equity avg `0.0326` n `42`; fx avg `0.0021` n `4`; index avg `-0.0142` n `9`; metal avg `0.0299` n `7`; unknown avg `-0.0474` n `313`
- 4h: commodity avg `-0.0834` n `7`; crypto_alt avg `0.0003` n `223`; crypto_major avg `0.3604` n `7`; equity avg `0.1764` n `42`; fx avg `0.0199` n `4`; index avg `-0.027` n `9`; metal avg `0.0826` n `7`; unknown avg `-0.1992` n `313`
- 24h: commodity avg `-0.3035` n `7`; crypto_alt avg `0.4845` n `223`; crypto_major avg `0.1958` n `7`; equity avg `0.4291` n `42`; fx avg `0.1639` n `4`; index avg `0.0209` n `9`; metal avg `0.2188` n `7`; unknown avg `-0.1298` n `311`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.403`, n `173`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.3853`, n `173`, moderate_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.3841`, n `173`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.3792`, n `169`, moderate_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.3744`, n `169`, moderate_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.3704`, n `173`, moderate_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.3556`, n `169`, moderate_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.3463`, n `169`, moderate_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.3223`, n `173`, moderate_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.3056`, n `173`, moderate_sample_signal
