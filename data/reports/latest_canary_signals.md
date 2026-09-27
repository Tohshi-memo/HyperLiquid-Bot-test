# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-27T15:07:31.439144+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1322` n `12`; crypto_alt avg `-0.3232` n `234`; crypto_major avg `-0.1424` n `8`; equity avg `-0.0177` n `141`; fx avg `0.0047` n `6`; index avg `0.0074` n `26`; metal avg `-0.0006` n `20`; unknown avg `0.3879` n `960`
- 1h: commodity avg `-0.1328` n `12`; crypto_alt avg `-0.8358` n `234`; crypto_major avg `-0.8461` n `8`; equity avg `-0.1079` n `141`; fx avg `0.0049` n `6`; index avg `0.0021` n `26`; metal avg `-0.0074` n `20`; unknown avg `3.3684` n `960`
- 4h: commodity avg `-0.148` n `12`; crypto_alt avg `-1.2406` n `234`; crypto_major avg `-0.9983` n `8`; equity avg `-0.1004` n `141`; fx avg `0.0018` n `6`; index avg `-0.0221` n `26`; metal avg `-0.0168` n `20`; unknown avg `7.7987` n `954`
- 24h: commodity avg `-0.1413` n `12`; crypto_alt avg `-1.2024` n `234`; crypto_major avg `-0.3923` n `8`; equity avg `0.1666` n `141`; fx avg `-0.0225` n `6`; index avg `-0.0003` n `26`; metal avg `-0.0226` n `20`; unknown avg `229.5304` n `889`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1738`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1572`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1545`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1521`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1458`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1193`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1149`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0984`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.097`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0906`, n `668`, weak_sample_signal
