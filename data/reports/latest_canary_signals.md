# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-04T15:00:38.860439+00:00`
- Correlation status: `ready`
- Asset price records: `275`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.2816` n `7`; crypto_alt avg `0.4403` n `223`; crypto_major avg `0.4745` n `7`; equity avg `-0.2017` n `42`; fx avg `0.0002` n `4`; index avg `0.0232` n `9`; metal avg `-0.3949` n `7`; unknown avg `0.1022` n `314`
- 1h: commodity avg `0.4792` n `7`; crypto_alt avg `0.8534` n `223`; crypto_major avg `1.2509` n `7`; equity avg `0.1885` n `42`; fx avg `-0.0043` n `4`; index avg `0.3057` n `9`; metal avg `-0.2333` n `7`; unknown avg `-0.0147` n `314`
- 4h: commodity avg `0.1237` n `7`; crypto_alt avg `1.1204` n `223`; crypto_major avg `1.1357` n `7`; equity avg `0.9527` n `42`; fx avg `0.0032` n `4`; index avg `0.759` n `9`; metal avg `0.1124` n `7`; unknown avg `-0.4403` n `314`
- 24h: commodity avg `1.5242` n `7`; crypto_alt avg `1.9298` n `223`; crypto_major avg `1.5525` n `7`; equity avg `1.0822` n `42`; fx avg `-0.0694` n `4`; index avg `1.1389` n `9`; metal avg `-1.4591` n `7`; unknown avg `-0.191` n `311`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2589`, n `271`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.2566`, n `267`, moderate_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.253`, n `267`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2504`, n `271`, moderate_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1526`, n `271`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1512`, n `271`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1506`, n `271`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1474`, n `267`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1473`, n `271`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1367`, n `267`, weak_sample_signal
