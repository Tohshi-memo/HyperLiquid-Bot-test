# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-03T05:15:38.294071+00:00`
- Correlation status: `ready`
- Asset price records: `140`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0014` n `7`; crypto_alt avg `0.1317` n `223`; crypto_major avg `0.0783` n `7`; equity avg `-0.0216` n `42`; fx avg `-0.0032` n `4`; index avg `-0.0253` n `9`; metal avg `0.004` n `7`; unknown avg `0.2849` n `313`
- 1h: commodity avg `-0.0044` n `7`; crypto_alt avg `0.3141` n `223`; crypto_major avg `0.1077` n `7`; equity avg `-0.1388` n `42`; fx avg `-0.0027` n `4`; index avg `-0.0525` n `9`; metal avg `0.0031` n `7`; unknown avg `0.2935` n `313`
- 4h: commodity avg `0.0264` n `7`; crypto_alt avg `-0.4247` n `223`; crypto_major avg `-0.1534` n `7`; equity avg `-0.1711` n `42`; fx avg `-0.0011` n `4`; index avg `-0.0885` n `9`; metal avg `0.0261` n `7`; unknown avg `0.2752` n `313`
- 24h: commodity avg `-0.0938` n `7`; crypto_alt avg `1.4712` n `223`; crypto_major avg `0.1026` n `7`; equity avg `0.54` n `42`; fx avg `0.0519` n `4`; index avg `-0.0068` n `9`; metal avg `0.0901` n `7`; unknown avg `0.3872` n `311`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.4433`, n `136`, moderate_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.4281`, n `136`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.4107`, n `132`, moderate_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.4084`, n `132`, moderate_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.4042`, n `136`, moderate_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.3978`, n `132`, moderate_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.3928`, n `132`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.3864`, n `136`, moderate_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.3678`, n `132`, moderate_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.3547`, n `136`, moderate_sample_signal
