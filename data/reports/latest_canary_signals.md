# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-04T02:07:26.372696+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0344` n `12`; crypto_alt avg `-0.0723` n `232`; crypto_major avg `-0.0719` n `8`; equity avg `0.134` n `133`; fx avg `-0.0138` n `6`; index avg `0.0085` n `26`; metal avg `0.0687` n `20`; unknown avg `0.1461` n `791`
- 1h: commodity avg `0.0395` n `12`; crypto_alt avg `-0.1303` n `232`; crypto_major avg `-0.1169` n `8`; equity avg `0.0033` n `133`; fx avg `0.0025` n `6`; index avg `-0.0073` n `26`; metal avg `0.0669` n `20`; unknown avg `-0.0627` n `791`
- 4h: commodity avg `0.0334` n `12`; crypto_alt avg `-0.6347` n `232`; crypto_major avg `-0.4625` n `8`; equity avg `0.3414` n `133`; fx avg `0.0359` n `6`; index avg `0.0123` n `26`; metal avg `-0.0269` n `20`; unknown avg `2.2273` n `784`
- 24h: commodity avg `-0.2047` n `12`; crypto_alt avg `3.1196` n `232`; crypto_major avg `4.538` n `8`; equity avg `1.6049` n `133`; fx avg `-0.1424` n `6`; index avg `0.2094` n `26`; metal avg `0.6484` n `20`; unknown avg `1.2639` n `736`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1167`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1128`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0986`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0886`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0843`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0802`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0733`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0708`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0694`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0659`, n `668`, weak_sample_signal
