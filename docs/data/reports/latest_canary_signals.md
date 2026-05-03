# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-03T08:28:13.929489+00:00`
- Correlation status: `ready`
- Asset price records: `152`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0058` n `7`; crypto_alt avg `0.217` n `223`; crypto_major avg `0.0018` n `7`; equity avg `-0.0211` n `42`; fx avg `0.0074` n `4`; index avg `0.0411` n `9`; metal avg `0.0359` n `7`; unknown avg `-0.1256` n `313`
- 1h: commodity avg `0.0091` n `7`; crypto_alt avg `0.1657` n `223`; crypto_major avg `0.0038` n `7`; equity avg `0.0339` n `42`; fx avg `0.0151` n `4`; index avg `0.027` n `9`; metal avg `0.0643` n `7`; unknown avg `-0.0713` n `313`
- 4h: commodity avg `-0.0788` n `7`; crypto_alt avg `0.722` n `223`; crypto_major avg `0.2033` n `7`; equity avg `-0.1923` n `42`; fx avg `0.0218` n `4`; index avg `0.0213` n `9`; metal avg `0.0953` n `7`; unknown avg `0.2522` n `311`
- 24h: commodity avg `-0.2121` n `7`; crypto_alt avg `1.5156` n `223`; crypto_major avg `-0.1507` n `7`; equity avg `0.1739` n `42`; fx avg `0.1265` n `4`; index avg `0.0757` n `9`; metal avg `0.1114` n `7`; unknown avg `0.2146` n `311`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.4249`, n `148`, moderate_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.4101`, n `148`, moderate_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.4037`, n `148`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.3882`, n `144`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.3859`, n `148`, moderate_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.3828`, n `144`, moderate_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.3759`, n `144`, moderate_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.3685`, n `144`, moderate_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.3605`, n `148`, moderate_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.3569`, n `148`, moderate_sample_signal
