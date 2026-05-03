# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-03T04:30:23.082456+00:00`
- Correlation status: `ready`
- Asset price records: `137`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0144` n `7`; crypto_alt avg `0.1616` n `223`; crypto_major avg `0.0856` n `7`; equity avg `-0.0187` n `42`; fx avg `0.0` n `4`; index avg `-0.0528` n `9`; metal avg `0.0036` n `7`; unknown avg `0.0052` n `313`
- 1h: commodity avg `0.0176` n `7`; crypto_alt avg `0.2637` n `223`; crypto_major avg `0.1281` n `7`; equity avg `0.0213` n `42`; fx avg `0.0021` n `4`; index avg `-0.0342` n `9`; metal avg `0.0033` n `7`; unknown avg `-0.001` n `313`
- 4h: commodity avg `0.0237` n `7`; crypto_alt avg `-1.0325` n `223`; crypto_major avg `-0.5331` n `7`; equity avg `-0.0848` n `42`; fx avg `0.0016` n `4`; index avg `-0.0795` n `9`; metal avg `0.0337` n `7`; unknown avg `-0.132` n `313`
- 24h: commodity avg `-0.1179` n `7`; crypto_alt avg `1.0288` n `223`; crypto_major avg `-0.1406` n `7`; equity avg `0.6557` n `42`; fx avg `0.0354` n `4`; index avg `-0.0141` n `9`; metal avg `0.0803` n `7`; unknown avg `0.1334` n `311`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.445`, n `133`, moderate_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.4299`, n `133`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.4121`, n `129`, moderate_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.4096`, n `129`, moderate_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.4041`, n `133`, moderate_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.3981`, n `129`, moderate_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.393`, n `129`, moderate_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.3907`, n `129`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.3862`, n `133`, moderate_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.3831`, n `133`, moderate_sample_signal
