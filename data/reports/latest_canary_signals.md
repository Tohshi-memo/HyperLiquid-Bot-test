# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-03T05:00:47.099460+00:00`
- Correlation status: `ready`
- Asset price records: `139`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0014` n `7`; crypto_alt avg `-0.0723` n `223`; crypto_major avg `-0.023` n `7`; equity avg `-0.0951` n `42`; fx avg `0.0045` n `4`; index avg `-0.0288` n `9`; metal avg `0.0023` n `7`; unknown avg `0.0166` n `313`
- 1h: commodity avg `0.0106` n `7`; crypto_alt avg `0.1579` n `223`; crypto_major avg `0.0259` n `7`; equity avg `-0.1331` n `42`; fx avg `-0.0003` n `4`; index avg `-0.0086` n `9`; metal avg `-0.0014` n `7`; unknown avg `0.0203` n `313`
- 4h: commodity avg `0.0375` n `7`; crypto_alt avg `-0.7828` n `223`; crypto_major avg `-0.3809` n `7`; equity avg `-0.1762` n `42`; fx avg `0.0021` n `4`; index avg `-0.0632` n `9`; metal avg `0.0322` n `7`; unknown avg `0.2363` n `313`
- 24h: commodity avg `-0.1046` n `7`; crypto_alt avg `1.2061` n `223`; crypto_major avg `-0.1349` n `7`; equity avg `0.607` n `42`; fx avg `0.029` n `4`; index avg `0.0125` n `9`; metal avg `0.0785` n `7`; unknown avg `0.0869` n `311`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.4444`, n `135`, moderate_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.4293`, n `135`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.4087`, n `131`, moderate_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.4067`, n `131`, moderate_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.4042`, n `135`, moderate_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.3987`, n `131`, moderate_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.3936`, n `131`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.3864`, n `135`, moderate_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.3782`, n `131`, moderate_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.3627`, n `131`, moderate_sample_signal
