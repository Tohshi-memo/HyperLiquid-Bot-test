# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-03T01:30:23.881187+00:00`
- Correlation status: `ready`
- Asset price records: `125`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0057` n `7`; crypto_alt avg `-0.1879` n `223`; crypto_major avg `-0.0908` n `7`; equity avg `0.0082` n `42`; fx avg `0.0` n `4`; index avg `-0.0005` n `9`; metal avg `-0.0096` n `7`; unknown avg `0.0489` n `313`
- 1h: commodity avg `0.0017` n `7`; crypto_alt avg `-0.6457` n `223`; crypto_major avg `-0.4489` n `7`; equity avg `-0.0271` n `42`; fx avg `0.0` n `4`; index avg `0.0088` n `9`; metal avg `-0.0024` n `7`; unknown avg `-0.0366` n `313`
- 4h: commodity avg `0.0518` n `7`; crypto_alt avg `-0.8873` n `223`; crypto_major avg `-0.4954` n `7`; equity avg `-0.0354` n `42`; fx avg `-0.0037` n `4`; index avg `0.0149` n `9`; metal avg `0.0041` n `7`; unknown avg `-0.1496` n `313`
- 24h: commodity avg `-0.1332` n `7`; crypto_alt avg `1.0291` n `223`; crypto_major avg `-0.1246` n `7`; equity avg `0.6279` n `42`; fx avg `-0.0137` n `4`; index avg `0.0364` n `9`; metal avg `0.0259` n `7`; unknown avg `0.1682` n `311`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.465`, n `121`, moderate_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.449`, n `121`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.4206`, n `117`, moderate_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.4186`, n `117`, moderate_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.4047`, n `117`, moderate_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.4038`, n `121`, moderate_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.3996`, n `117`, moderate_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.387`, n `117`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.386`, n `121`, moderate_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.3727`, n `117`, moderate_sample_signal
