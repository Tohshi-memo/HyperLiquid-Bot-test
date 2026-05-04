# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-04T01:45:20.840356+00:00`
- Correlation status: `ready`
- Asset price records: `222`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0025` n `7`; crypto_alt avg `0.2278` n `223`; crypto_major avg `0.1889` n `7`; equity avg `0.1774` n `42`; fx avg `0.0106` n `4`; index avg `0.0738` n `9`; metal avg `0.1046` n `7`; unknown avg `0.0735` n `314`
- 1h: commodity avg `0.0445` n `7`; crypto_alt avg `0.7462` n `223`; crypto_major avg `0.8331` n `7`; equity avg `0.4399` n `42`; fx avg `0.0165` n `4`; index avg `0.2654` n `9`; metal avg `-0.1523` n `7`; unknown avg `0.19` n `314`
- 4h: commodity avg `0.7612` n `7`; crypto_alt avg `0.5087` n `223`; crypto_major avg `0.6858` n `7`; equity avg `0.2574` n `42`; fx avg `0.0077` n `4`; index avg `0.2508` n `9`; metal avg `-0.5898` n `7`; unknown avg `0.3255` n `314`
- 24h: commodity avg `0.0543` n `7`; crypto_alt avg `0.8615` n `223`; crypto_major avg `1.0397` n `7`; equity avg `0.5407` n `42`; fx avg `-0.0021` n `4`; index avg `0.3824` n `9`; metal avg `-0.0059` n `7`; unknown avg `0.5251` n `311`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.3808`, n `218`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.3653`, n `218`, moderate_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.3399`, n `214`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.3395`, n `214`, moderate_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.2707`, n `218`, moderate_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.2611`, n `218`, moderate_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.2252`, n `218`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.2004`, n `218`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1763`, n `218`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1741`, n `218`, weak_sample_signal
