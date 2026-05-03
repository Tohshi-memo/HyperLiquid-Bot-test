# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-03T01:15:34.552750+00:00`
- Correlation status: `ready`
- Asset price records: `124`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0098` n `7`; crypto_alt avg `-0.2284` n `223`; crypto_major avg `-0.1498` n `7`; equity avg `-0.0269` n `42`; fx avg `0.0` n `4`; index avg `-0.0` n `9`; metal avg `0.0101` n `7`; unknown avg `0.114` n `313`
- 1h: commodity avg `0.0205` n `7`; crypto_alt avg `-0.1461` n `223`; crypto_major avg `-0.1306` n `7`; equity avg `-0.0172` n `42`; fx avg `0.0021` n `4`; index avg `0.0231` n `9`; metal avg `-0.0122` n `7`; unknown avg `-0.1461` n `313`
- 4h: commodity avg `0.0683` n `7`; crypto_alt avg `-0.5787` n `223`; crypto_major avg `-0.3748` n `7`; equity avg `-0.029` n `42`; fx avg `0.0189` n `4`; index avg `-0.0063` n `9`; metal avg `0.0077` n `7`; unknown avg `-0.1861` n `313`
- 24h: commodity avg `-0.1644` n `7`; crypto_alt avg `1.2617` n `223`; crypto_major avg `-0.0639` n `7`; equity avg `0.7458` n `42`; fx avg `-0.0137` n `4`; index avg `0.0384` n `9`; metal avg `0.0376` n `7`; unknown avg `0.1413` n `311`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.4738`, n `120`, moderate_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.4574`, n `120`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.4203`, n `116`, moderate_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.4183`, n `116`, moderate_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.4048`, n `116`, moderate_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.4037`, n `120`, moderate_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.3998`, n `116`, moderate_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.3862`, n `116`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.3859`, n `120`, moderate_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.3722`, n `116`, moderate_sample_signal
