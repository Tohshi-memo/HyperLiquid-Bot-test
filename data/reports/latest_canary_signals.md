# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-03T17:45:36.089269+00:00`
- Correlation status: `ready`
- Asset price records: `190`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1383` n `7`; crypto_alt avg `-0.0262` n `223`; crypto_major avg `0.0449` n `7`; equity avg `0.0396` n `42`; fx avg `0.0003` n `4`; index avg `-0.0082` n `9`; metal avg `0.0125` n `7`; unknown avg `0.0279` n `314`
- 1h: commodity avg `0.1519` n `7`; crypto_alt avg `0.1438` n `223`; crypto_major avg `0.1106` n `7`; equity avg `0.0976` n `42`; fx avg `-0.0104` n `4`; index avg `0.0131` n `9`; metal avg `0.0919` n `7`; unknown avg `0.1037` n `313`
- 4h: commodity avg `-0.2865` n `7`; crypto_alt avg `0.1431` n `223`; crypto_major avg `0.2426` n `7`; equity avg `0.2672` n `42`; fx avg `-0.0079` n `4`; index avg `0.0934` n `9`; metal avg `0.2485` n `7`; unknown avg `0.3195` n `313`
- 24h: commodity avg `-0.4029` n `7`; crypto_alt avg `-0.0101` n `223`; crypto_major avg `0.1885` n `7`; equity avg `0.5562` n `42`; fx avg `0.0766` n `4`; index avg `0.107` n `9`; metal avg `0.4373` n `7`; unknown avg `0.1666` n `311`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.3998`, n `186`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.3883`, n `182`, moderate_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.3821`, n `182`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.3819`, n `186`, moderate_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.3782`, n `186`, moderate_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.3647`, n `186`, moderate_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.3265`, n `186`, moderate_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.3069`, n `186`, moderate_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.3058`, n `186`, moderate_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.2921`, n `182`, moderate_sample_signal
