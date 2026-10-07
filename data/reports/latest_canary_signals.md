# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-07T13:07:33.985282+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0232` n `13`; crypto_alt avg `0.139` n `235`; crypto_major avg `0.0629` n `8`; equity avg `0.0203` n `150`; fx avg `0.0326` n `6`; index avg `0.001` n `26`; metal avg `0.0787` n `20`; unknown avg `150.1844` n `1074`
- 1h: commodity avg `-0.0076` n `13`; crypto_alt avg `-0.1425` n `235`; crypto_major avg `-0.1725` n `8`; equity avg `-0.1134` n `150`; fx avg `0.0061` n `6`; index avg `-0.0324` n `26`; metal avg `-0.2286` n `20`; unknown avg `92.9439` n `1074`
- 4h: commodity avg `0.1501` n `13`; crypto_alt avg `-1.2087` n `235`; crypto_major avg `-1.0494` n `8`; equity avg `-0.6134` n `150`; fx avg `-0.0529` n `6`; index avg `-0.1412` n `26`; metal avg `-0.2502` n `20`; unknown avg `1.4931` n `1068`
- 24h: commodity avg `1.2923` n `13`; crypto_alt avg `-5.4473` n `235`; crypto_major avg `-3.6688` n `8`; equity avg `-1.7868` n `150`; fx avg `-0.1855` n `6`; index avg `-0.4038` n `26`; metal avg `-0.6888` n `20`; unknown avg `814.5746` n `980`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1384`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1339`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.132`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1143`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0774`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.071`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0669`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0667`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0666`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0634`, n `668`, weak_sample_signal
