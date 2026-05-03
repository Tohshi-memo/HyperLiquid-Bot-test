# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-03T21:30:27.882432+00:00`
- Correlation status: `ready`
- Asset price records: `205`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1592` n `7`; crypto_alt avg `-0.1269` n `223`; crypto_major avg `-0.0614` n `7`; equity avg `0.0189` n `42`; fx avg `0.0013` n `4`; index avg `-0.0018` n `9`; metal avg `0.0136` n `7`; unknown avg `-0.0437` n `314`
- 1h: commodity avg `-0.4213` n `7`; crypto_alt avg `-0.2932` n `223`; crypto_major avg `-0.1533` n `7`; equity avg `0.1618` n `42`; fx avg `-0.0451` n `4`; index avg `0.0412` n `9`; metal avg `0.1768` n `7`; unknown avg `-0.1466` n `314`
- 4h: commodity avg `0.0258` n `7`; crypto_alt avg `0.0738` n `223`; crypto_major avg `0.0396` n `7`; equity avg `0.2246` n `42`; fx avg `-0.0497` n `4`; index avg `0.03` n `9`; metal avg `0.1632` n `7`; unknown avg `-0.1538` n `314`
- 24h: commodity avg `-0.4769` n `7`; crypto_alt avg `-0.4836` n `223`; crypto_major avg `0.1136` n `7`; equity avg `0.2866` n `42`; fx avg `-0.0154` n `4`; index avg `0.1112` n `9`; metal avg `0.6205` n `7`; unknown avg `-0.1167` n `311`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.396`, n `201`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.3927`, n `197`, moderate_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.3858`, n `197`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.3782`, n `201`, moderate_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.3688`, n `201`, moderate_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.3559`, n `201`, moderate_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.3218`, n `201`, moderate_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.3025`, n `201`, moderate_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.3016`, n `201`, moderate_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.2428`, n `201`, weak_sample_signal
