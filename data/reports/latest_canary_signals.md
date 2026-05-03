# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-03T08:15:21.401810+00:00`
- Correlation status: `ready`
- Asset price records: `152`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0163` n `7`; crypto_alt avg `0.2073` n `223`; crypto_major avg `0.1026` n `7`; equity avg `-0.0388` n `42`; fx avg `0.0037` n `4`; index avg `-0.0096` n `9`; metal avg `0.0265` n `7`; unknown avg `-0.0864` n `313`
- 1h: commodity avg `0.0196` n `7`; crypto_alt avg `0.1557` n `223`; crypto_major avg `0.1046` n `7`; equity avg `0.0162` n `42`; fx avg `0.0114` n `4`; index avg `-0.0235` n `9`; metal avg `0.0549` n `7`; unknown avg `-0.0341` n `313`
- 4h: commodity avg `-0.0683` n `7`; crypto_alt avg `0.7079` n `223`; crypto_major avg `0.3042` n `7`; equity avg `-0.2106` n `42`; fx avg `0.018` n `4`; index avg `-0.0291` n `9`; metal avg `0.0859` n `7`; unknown avg `0.2898` n `311`
- 24h: commodity avg `-0.2017` n `7`; crypto_alt avg `1.501` n `223`; crypto_major avg `-0.0506` n `7`; equity avg `0.1558` n `42`; fx avg `0.1228` n `4`; index avg `0.0254` n `9`; metal avg `0.102` n `7`; unknown avg `0.1891` n `311`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.424`, n `148`, moderate_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.4092`, n `148`, moderate_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.4038`, n `148`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.3907`, n `144`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.386`, n `148`, moderate_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.3858`, n `144`, moderate_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.3762`, n `144`, moderate_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.3688`, n `144`, moderate_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.36`, n `148`, moderate_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.3565`, n `148`, moderate_sample_signal
