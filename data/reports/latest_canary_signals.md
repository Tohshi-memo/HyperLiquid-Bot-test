# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-03T15:34:46.827130+00:00`
- Correlation status: `ready`
- Asset price records: `181`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0383` n `7`; crypto_alt avg `-0.0203` n `223`; crypto_major avg `-0.022` n `7`; equity avg `-0.0265` n `42`; fx avg `-0.0026` n `4`; index avg `0.0341` n `9`; metal avg `0.0017` n `7`; unknown avg `0.1454` n `313`
- 1h: commodity avg `-0.1762` n `7`; crypto_alt avg `0.1394` n `223`; crypto_major avg `-0.0169` n `7`; equity avg `-0.0221` n `42`; fx avg `-0.0018` n `4`; index avg `0.0322` n `9`; metal avg `0.0216` n `7`; unknown avg `0.2097` n `313`
- 4h: commodity avg `-0.2224` n `7`; crypto_alt avg `0.2832` n `223`; crypto_major avg `0.3742` n `7`; equity avg `0.0453` n `42`; fx avg `0.007` n `4`; index avg `-0.0199` n `9`; metal avg `0.0809` n `7`; unknown avg `0.153` n `313`
- 24h: commodity avg `-0.4633` n `7`; crypto_alt avg `0.288` n `223`; crypto_major avg `0.0971` n `7`; equity avg `0.3858` n `42`; fx avg `0.1262` n `4`; index avg `0.0602` n `9`; metal avg `0.2332` n `7`; unknown avg `0.1122` n `311`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.4027`, n `177`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.3849`, n `177`, moderate_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.3815`, n `177`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.3789`, n `173`, moderate_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.3745`, n `173`, moderate_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.3678`, n `177`, moderate_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.3282`, n `173`, moderate_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.3219`, n `177`, moderate_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.3184`, n `173`, moderate_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.3053`, n `177`, moderate_sample_signal
