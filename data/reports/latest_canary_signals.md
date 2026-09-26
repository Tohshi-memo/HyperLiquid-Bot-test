# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-26T01:37:26.621275+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.033` n `12`; crypto_alt avg `0.0264` n `234`; crypto_major avg `0.0603` n `8`; equity avg `0.0009` n `141`; fx avg `0.0057` n `6`; index avg `0.0058` n `26`; metal avg `-0.0036` n `20`; unknown avg `-0.206` n `960`
- 1h: commodity avg `-0.1951` n `12`; crypto_alt avg `0.3427` n `234`; crypto_major avg `0.5468` n `8`; equity avg `0.0392` n `141`; fx avg `0.0068` n `6`; index avg `0.0327` n `26`; metal avg `0.0131` n `20`; unknown avg `0.6389` n `958`
- 4h: commodity avg `0.4269` n `12`; crypto_alt avg `1.1663` n `234`; crypto_major avg `0.7463` n `8`; equity avg `-0.1851` n `141`; fx avg `0.0141` n `6`; index avg `-0.0588` n `26`; metal avg `-0.0394` n `20`; unknown avg `0.4784` n `926`
- 24h: commodity avg `0.1566` n `12`; crypto_alt avg `3.106` n `234`; crypto_major avg `1.3211` n `8`; equity avg `-0.334` n `141`; fx avg `-0.1665` n `6`; index avg `0.1314` n `26`; metal avg `0.0666` n `20`; unknown avg `1125.8698` n `810`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1666`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1525`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1488`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1455`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.139`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1294`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1219`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0998`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0908`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0867`, n `668`, weak_sample_signal
