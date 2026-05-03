# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-03T23:15:27.040864+00:00`
- Correlation status: `ready`
- Asset price records: `212`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0665` n `7`; crypto_alt avg `-0.1113` n `223`; crypto_major avg `-0.0893` n `7`; equity avg `-0.0655` n `42`; fx avg `-0.0011` n `4`; index avg `-0.0139` n `9`; metal avg `-0.0141` n `7`; unknown avg `0.0063` n `314`
- 1h: commodity avg `0.1075` n `7`; crypto_alt avg `-0.2519` n `223`; crypto_major avg `-0.0468` n `7`; equity avg `-0.2018` n `42`; fx avg `-0.0021` n `4`; index avg `-0.0351` n `9`; metal avg `0.0335` n `7`; unknown avg `-0.1747` n `314`
- 4h: commodity avg `-0.0299` n `7`; crypto_alt avg `0.1316` n `223`; crypto_major avg `0.5059` n `7`; equity avg `-0.0457` n `42`; fx avg `-0.0319` n `4`; index avg `-0.0301` n `9`; metal avg `-0.0476` n `7`; unknown avg `-0.0166` n `314`
- 24h: commodity avg `-0.1232` n `7`; crypto_alt avg `-0.1062` n `223`; crypto_major avg `0.5122` n `7`; equity avg `0.0836` n `42`; fx avg `-0.0228` n `4`; index avg `0.0422` n `9`; metal avg `0.3939` n `7`; unknown avg `0.0609` n `311`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.3917`, n `208`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.3744`, n `208`, moderate_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.3177`, n `208`, moderate_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.3072`, n `208`, moderate_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.3046`, n `208`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.2908`, n `204`, moderate_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.2903`, n `204`, moderate_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.2901`, n `208`, moderate_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.2859`, n `208`, moderate_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.2369`, n `204`, weak_sample_signal
