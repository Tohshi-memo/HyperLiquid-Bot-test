# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-03T13:15:21.686514+00:00`
- Correlation status: `ready`
- Asset price records: `172`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0176` n `7`; crypto_alt avg `0.0611` n `223`; crypto_major avg `0.0763` n `7`; equity avg `-0.058` n `42`; fx avg `0.0` n `4`; index avg `0.0045` n `9`; metal avg `-0.0061` n `7`; unknown avg `0.1178` n `313`
- 1h: commodity avg `-0.0609` n `7`; crypto_alt avg `-0.0826` n `223`; crypto_major avg `-0.0485` n `7`; equity avg `0.0036` n `42`; fx avg `-0.0005` n `4`; index avg `0.0223` n `9`; metal avg `0.0261` n `7`; unknown avg `0.129` n `313`
- 4h: commodity avg `-0.1285` n `7`; crypto_alt avg `0.3279` n `223`; crypto_major avg `0.3732` n `7`; equity avg `0.2027` n `42`; fx avg `0.0128` n `4`; index avg `0.0724` n `9`; metal avg `0.0672` n `7`; unknown avg `-0.0608` n `313`
- 24h: commodity avg `-0.285` n `7`; crypto_alt avg `1.1834` n `223`; crypto_major avg `0.2952` n `7`; equity avg `0.3229` n `42`; fx avg `0.1508` n `4`; index avg `0.0546` n `9`; metal avg `0.1587` n `7`; unknown avg `0.3535` n `311`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.403`, n `168`, moderate_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.3857`, n `168`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.3852`, n `168`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.3769`, n `164`, moderate_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.3718`, n `168`, moderate_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.3707`, n `164`, moderate_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.3602`, n `164`, moderate_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.3516`, n `164`, moderate_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.326`, n `168`, moderate_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.3155`, n `168`, moderate_sample_signal
