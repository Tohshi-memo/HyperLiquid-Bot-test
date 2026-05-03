# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-03T21:00:29.179925+00:00`
- Correlation status: `ready`
- Asset price records: `203`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.2338` n `7`; crypto_alt avg `-0.1232` n `223`; crypto_major avg `-0.1681` n `7`; equity avg `-0.0014` n `42`; fx avg `-0.0048` n `4`; index avg `0.0001` n `9`; metal avg `0.0373` n `7`; unknown avg `-0.132` n `314`
- 1h: commodity avg `-0.5533` n `7`; crypto_alt avg `0.0769` n `223`; crypto_major avg `0.0` n `7`; equity avg `0.0271` n `42`; fx avg `-0.0045` n `4`; index avg `0.0426` n `9`; metal avg `-0.003` n `7`; unknown avg `-0.141` n `314`
- 4h: commodity avg `-0.2567` n `7`; crypto_alt avg `0.4958` n `223`; crypto_major avg `0.3034` n `7`; equity avg `0.179` n `42`; fx avg `-0.0259` n `4`; index avg `0.0635` n `9`; metal avg `0.1288` n `7`; unknown avg `-0.1151` n `313`
- 24h: commodity avg `-0.6442` n `7`; crypto_alt avg `-0.1169` n `223`; crypto_major avg `0.1295` n `7`; equity avg `0.1567` n `42`; fx avg `0.0385` n `4`; index avg `0.0918` n `9`; metal avg `0.501` n `7`; unknown avg `-0.1158` n `311`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.399`, n `199`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.3857`, n `195`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.3812`, n `199`, moderate_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.3788`, n `195`, moderate_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.3689`, n `199`, moderate_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.356`, n `199`, moderate_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.3363`, n `199`, moderate_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.3181`, n `199`, moderate_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.3064`, n `199`, moderate_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.2536`, n `195`, moderate_sample_signal
