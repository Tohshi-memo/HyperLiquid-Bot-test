# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-03T16:15:20.346791+00:00`
- Correlation status: `ready`
- Asset price records: `184`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.2082` n `7`; crypto_alt avg `-0.1004` n `223`; crypto_major avg `-0.1006` n `7`; equity avg `0.0839` n `42`; fx avg `0.0035` n `4`; index avg `0.0278` n `9`; metal avg `0.0092` n `7`; unknown avg `-0.0078` n `313`
- 1h: commodity avg `-0.36` n `7`; crypto_alt avg `-0.2546` n `223`; crypto_major avg `-0.219` n `7`; equity avg `0.0895` n `42`; fx avg `0.0014` n `4`; index avg `0.0687` n `9`; metal avg `0.0672` n `7`; unknown avg `-0.0212` n `313`
- 4h: commodity avg `-0.5719` n `7`; crypto_alt avg `-0.3322` n `223`; crypto_major avg `-0.3112` n `7`; equity avg `0.1423` n `42`; fx avg `0.0149` n `4`; index avg `0.0426` n `9`; metal avg `0.1469` n `7`; unknown avg `-0.0687` n `313`
- 24h: commodity avg `-0.7717` n `7`; crypto_alt avg `-0.2202` n `223`; crypto_major avg `-0.1968` n `7`; equity avg `0.4448` n `42`; fx avg `0.1195` n `4`; index avg `0.0812` n `9`; metal avg `0.3016` n `7`; unknown avg `-0.0666` n `311`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.4021`, n `180`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.3843`, n `180`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.3808`, n `176`, moderate_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.3803`, n `180`, moderate_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.3755`, n `176`, moderate_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.3666`, n `180`, moderate_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.3242`, n `180`, moderate_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.3123`, n `176`, moderate_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.306`, n `180`, moderate_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.3052`, n `180`, moderate_sample_signal
