# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-26T05:07:29.666834+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0075` n `13`; crypto_alt avg `0.1985` n `237`; crypto_major avg `0.0999` n `8`; equity avg `0.1883` n `152`; fx avg `-0.005` n `6`; index avg `0.019` n `26`; metal avg `0.0237` n `20`; unknown avg `-0.0691` n `1238`
- 1h: commodity avg `0.0314` n `13`; crypto_alt avg `0.906` n `237`; crypto_major avg `0.6551` n `8`; equity avg `0.4142` n `152`; fx avg `0.0033` n `6`; index avg `0.0501` n `26`; metal avg `0.0666` n `20`; unknown avg `1.3383` n `1236`
- 4h: commodity avg `-0.114` n `13`; crypto_alt avg `0.0417` n `237`; crypto_major avg `0.0477` n `8`; equity avg `0.2593` n `152`; fx avg `-0.0115` n `6`; index avg `0.101` n `26`; metal avg `0.197` n `20`; unknown avg `0.3468` n `1222`
- 24h: commodity avg `-0.6019` n `13`; crypto_alt avg `-0.9498` n `237`; crypto_major avg `-1.0` n `8`; equity avg `-0.3559` n `152`; fx avg `0.0445` n `6`; index avg `0.0506` n `26`; metal avg `0.204` n `20`; unknown avg `-0.3479` n `983`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2532`, n `668`, moderate_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.2014`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1942`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1917`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.153`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1435`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1338`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1289`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0931`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0918`, n `668`, weak_sample_signal
