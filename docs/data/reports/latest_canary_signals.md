# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-23T22:23:12.182965+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0054` n `12`; crypto_alt avg `-0.1914` n `234`; crypto_major avg `-0.2107` n `8`; equity avg `0.032` n `141`; fx avg `-0.0003` n `6`; index avg `-0.0052` n `26`; metal avg `-0.0116` n `20`; unknown avg `1.2733` n `945`
- 1h: commodity avg `-0.0296` n `12`; crypto_alt avg `0.6343` n `234`; crypto_major avg `0.616` n `8`; equity avg `0.1687` n `141`; fx avg `0.0005` n `6`; index avg `0.0368` n `26`; metal avg `0.0079` n `20`; unknown avg `1.4947` n `943`
- 4h: commodity avg `0.1613` n `12`; crypto_alt avg `0.1823` n `234`; crypto_major avg `0.8179` n `8`; equity avg `-0.1036` n `141`; fx avg `-0.0098` n `6`; index avg `0.0167` n `26`; metal avg `0.0352` n `20`; unknown avg `0.6098` n `845`
- 24h: commodity avg `0.6046` n `12`; crypto_alt avg `-3.5486` n `234`; crypto_major avg `-2.9542` n `8`; equity avg `-1.5378` n `140`; fx avg `-0.0038` n `6`; index avg `-0.3374` n `26`; metal avg `-0.8067` n `20`; unknown avg `584.5192` n `821`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1622`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1576`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1468`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1461`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1355`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1258`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1193`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1159`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.11`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0969`, n `668`, weak_sample_signal
