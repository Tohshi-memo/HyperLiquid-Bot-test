# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-31T23:52:36.356965+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0085` n `12`; crypto_alt avg `-0.0231` n `230`; crypto_major avg `-0.0358` n `8`; equity avg `-0.0143` n `102`; fx avg `-0.0239` n `6`; index avg `-0.0159` n `25`; metal avg `-0.0018` n `20`; unknown avg `5.5411` n `781`
- 1h: commodity avg `0.0473` n `12`; crypto_alt avg `0.1508` n `230`; crypto_major avg `-0.0045` n `8`; equity avg `-0.0176` n `102`; fx avg `-0.0419` n `6`; index avg `-0.0378` n `25`; metal avg `-0.0082` n `20`; unknown avg `5.0274` n `781`
- 4h: commodity avg `0.5921` n `12`; crypto_alt avg `0.0216` n `230`; crypto_major avg `-0.1112` n `8`; equity avg `-0.7002` n `102`; fx avg `-0.142` n `6`; index avg `-0.1599` n `25`; metal avg `-0.0811` n `20`; unknown avg `5.9765` n `780`
- 24h: commodity avg `0.8122` n `12`; crypto_alt avg `-0.4763` n `230`; crypto_major avg `-2.2857` n `8`; equity avg `-1.9727` n `102`; fx avg `0.0423` n `6`; index avg `-0.0554` n `25`; metal avg `-0.4329` n `20`; unknown avg `2.6536` n `747`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1031`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0997`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.092`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0835`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0746`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0713`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0708`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0663`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0654`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0653`, n `668`, weak_sample_signal
