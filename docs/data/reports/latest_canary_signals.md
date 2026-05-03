# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-03T22:00:33.773213+00:00`
- Correlation status: `ready`
- Asset price records: `207`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0039` n `7`; crypto_alt avg `0.3814` n `223`; crypto_major avg `0.3952` n `7`; equity avg `0.0637` n `42`; fx avg `-0.004` n `4`; index avg `0.19` n `9`; metal avg `-0.2195` n `7`; unknown avg `0.2441` n `314`
- 1h: commodity avg `0.0142` n `7`; crypto_alt avg `-0.1349` n `223`; crypto_major avg `-0.0451` n `7`; equity avg `0.1427` n `42`; fx avg `-0.0346` n `4`; index avg `0.2117` n `9`; metal avg `-0.126` n `7`; unknown avg `0.2947` n `314`
- 4h: commodity avg `-0.4137` n `7`; crypto_alt avg `0.1103` n `223`; crypto_major avg `0.0825` n `7`; equity avg `0.2149` n `42`; fx avg `-0.0548` n `4`; index avg `0.2623` n `9`; metal avg `-0.0459` n `7`; unknown avg `0.1405` n `314`
- 24h: commodity avg `-0.6072` n `7`; crypto_alt avg `-0.48` n `223`; crypto_major avg `-0.1186` n `7`; equity avg `0.2727` n `42`; fx avg `-0.0237` n `4`; index avg `0.3192` n `9`; metal avg `0.365` n `7`; unknown avg `0.096` n `311`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `-0.4019`, n `199`, moderate_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.3965`, n `199`, moderate_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.3948`, n `203`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.3771`, n `203`, moderate_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.3609`, n `203`, moderate_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.348`, n `203`, moderate_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.2979`, n `203`, moderate_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.2906`, n `203`, moderate_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.2781`, n `203`, moderate_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.2416`, n `199`, weak_sample_signal
