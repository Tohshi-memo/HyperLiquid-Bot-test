# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-13T16:37:31.197292+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.027` n `12`; crypto_alt avg `-0.2536` n `230`; crypto_major avg `-0.2768` n `8`; equity avg `-0.4661` n `92`; fx avg `-0.0087` n `6`; index avg `-0.0693` n `25`; metal avg `-0.1737` n `20`; unknown avg `-0.0079` n `766`
- 1h: commodity avg `0.1666` n `12`; crypto_alt avg `-0.6932` n `230`; crypto_major avg `-0.7445` n `8`; equity avg `-1.1017` n `92`; fx avg `-0.0018` n `6`; index avg `-0.1987` n `25`; metal avg `-0.2437` n `20`; unknown avg `0.1056` n `766`
- 4h: commodity avg `0.1778` n `12`; crypto_alt avg `-0.3948` n `230`; crypto_major avg `-0.5999` n `8`; equity avg `-0.8577` n `92`; fx avg `-0.0548` n `6`; index avg `-0.0996` n `25`; metal avg `-0.3204` n `20`; unknown avg `-0.0929` n `766`
- 24h: commodity avg `0.1715` n `12`; crypto_alt avg `-1.9718` n `230`; crypto_major avg `-3.0044` n `8`; equity avg `-3.1439` n `92`; fx avg `-0.0984` n `6`; index avg `-0.6361` n `25`; metal avg `-0.5751` n `20`; unknown avg `-0.2115` n `749`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.2029`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1875`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1386`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1277`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1245`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1095`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1072`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0988`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0875`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0848`, n `668`, weak_sample_signal
