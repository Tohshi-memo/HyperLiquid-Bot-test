# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-27T08:22:27.085748+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0221` n `12`; crypto_alt avg `-0.0553` n `234`; crypto_major avg `-0.0659` n `8`; equity avg `0.0097` n `141`; fx avg `-0.0084` n `6`; index avg `0.0105` n `26`; metal avg `-0.0049` n `20`; unknown avg `0.0211` n `961`
- 1h: commodity avg `-0.0078` n `12`; crypto_alt avg `0.5239` n `234`; crypto_major avg `0.7016` n `8`; equity avg `0.0827` n `141`; fx avg `-0.013` n `6`; index avg `0.0207` n `26`; metal avg `-0.0004` n `20`; unknown avg `1.7366` n `943`
- 4h: commodity avg `-0.0141` n `12`; crypto_alt avg `1.4647` n `234`; crypto_major avg `0.9699` n `8`; equity avg `0.1462` n `141`; fx avg `-0.0038` n `6`; index avg `0.0272` n `26`; metal avg `0.0045` n `20`; unknown avg `4.6117` n `923`
- 24h: commodity avg `0.0466` n `12`; crypto_alt avg `1.6045` n `234`; crypto_major avg `0.943` n `8`; equity avg `0.3785` n `141`; fx avg `-0.0112` n `6`; index avg `0.0337` n `26`; metal avg `0.0052` n `20`; unknown avg `4.9047` n `887`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1627`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1513`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1501`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1425`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1293`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1212`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.115`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0969`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0881`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0877`, n `668`, weak_sample_signal
