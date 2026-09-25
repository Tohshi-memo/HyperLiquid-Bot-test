# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-25T05:37:26.489399+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0723` n `12`; crypto_alt avg `0.1304` n `234`; crypto_major avg `0.1009` n `8`; equity avg `0.1164` n `141`; fx avg `-0.0126` n `6`; index avg `0.035` n `26`; metal avg `0.0873` n `20`; unknown avg `1.0804` n `946`
- 1h: commodity avg `-0.0492` n `12`; crypto_alt avg `-0.241` n `234`; crypto_major avg `-0.1404` n `8`; equity avg `0.1603` n `141`; fx avg `-0.0304` n `6`; index avg `0.0499` n `26`; metal avg `0.0251` n `20`; unknown avg `52.94` n `942`
- 4h: commodity avg `-0.0062` n `12`; crypto_alt avg `-0.3366` n `234`; crypto_major avg `-0.2586` n `8`; equity avg `0.2431` n `141`; fx avg `-0.0821` n `6`; index avg `0.0648` n `26`; metal avg `-0.1347` n `20`; unknown avg `5.9253` n `936`
- 24h: commodity avg `0.3674` n `12`; crypto_alt avg `1.4679` n `234`; crypto_major avg `0.295` n `8`; equity avg `0.5412` n `141`; fx avg `-0.1513` n `6`; index avg `0.0832` n `26`; metal avg `-0.1737` n `20`; unknown avg `17.5239` n `813`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1651`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1518`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1496`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1422`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1348`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1301`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1231`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1071`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1026`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0932`, n `668`, weak_sample_signal
