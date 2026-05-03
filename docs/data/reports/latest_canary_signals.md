# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-03T00:15:22.857117+00:00`
- Correlation status: `ready`
- Asset price records: `120`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.007` n `7`; crypto_alt avg `-0.3333` n `223`; crypto_major avg `-0.2575` n `7`; equity avg `-0.0077` n `42`; fx avg `-0.0064` n `4`; index avg `0.002` n `9`; metal avg `-0.0092` n `7`; unknown avg `-0.0268` n `313`
- 1h: commodity avg `0.0018` n `7`; crypto_alt avg `-0.3393` n `223`; crypto_major avg `-0.3099` n `7`; equity avg `-0.0131` n `42`; fx avg `-0.0005` n `4`; index avg `0.0101` n `9`; metal avg `0.0056` n `7`; unknown avg `0.0635` n `313`
- 4h: commodity avg `0.101` n `7`; crypto_alt avg `-0.3668` n `223`; crypto_major avg `-0.2287` n `7`; equity avg `0.1487` n `42`; fx avg `0.0298` n `4`; index avg `-0.0137` n `9`; metal avg `0.0262` n `7`; unknown avg `0.229` n `313`
- 24h: commodity avg `-0.2018` n `7`; crypto_alt avg `1.7` n `223`; crypto_major avg `0.2508` n `7`; equity avg `0.6754` n `42`; fx avg `-0.0063` n `4`; index avg `0.0308` n `9`; metal avg `0.0424` n `7`; unknown avg `0.5048` n `311`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.4801`, n `116`, moderate_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.4634`, n `116`, moderate_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.4229`, n `112`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.4173`, n `112`, moderate_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.4152`, n `112`, moderate_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.4067`, n `112`, moderate_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.4032`, n `116`, moderate_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.4015`, n `112`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.3853`, n `116`, moderate_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.3831`, n `112`, moderate_sample_signal
