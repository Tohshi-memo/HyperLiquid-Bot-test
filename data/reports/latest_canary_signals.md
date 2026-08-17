# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-17T01:51:51.728341+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.004` n `12`; crypto_alt avg `-0.0849` n `230`; crypto_major avg `-0.0525` n `8`; equity avg `-0.0173` n `114`; fx avg `0.0041` n `6`; index avg `0.0035` n `25`; metal avg `-0.0052` n `20`; unknown avg `-0.0231` n `792`
- 1h: commodity avg `0.0675` n `12`; crypto_alt avg `0.4853` n `230`; crypto_major avg `0.7297` n `8`; equity avg `0.0581` n `114`; fx avg `-0.011` n `6`; index avg `0.0114` n `25`; metal avg `0.0579` n `20`; unknown avg `0.4175` n `792`
- 4h: commodity avg `-0.1372` n `12`; crypto_alt avg `0.4767` n `230`; crypto_major avg `0.6075` n `8`; equity avg `0.1021` n `114`; fx avg `-0.0573` n `6`; index avg `0.0035` n `25`; metal avg `0.2191` n `20`; unknown avg `0.0803` n `791`
- 24h: commodity avg `-0.1378` n `12`; crypto_alt avg `0.0052` n `230`; crypto_major avg `0.334` n `8`; equity avg `0.3823` n `114`; fx avg `-0.0645` n `6`; index avg `0.0393` n `25`; metal avg `0.2249` n `20`; unknown avg `-0.0188` n `759`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2016`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1681`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1536`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1429`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1413`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1371`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1351`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1246`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1153`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0895`, n `668`, weak_sample_signal
