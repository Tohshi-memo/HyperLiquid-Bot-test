# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-30T22:52:22.108585+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0216` n `12`; crypto_alt avg `-0.0327` n `228`; crypto_major avg `0.1363` n `8`; equity avg `0.0733` n `69`; fx avg `0.0` n `6`; index avg `0.0797` n `23`; metal avg `0.001` n `18`; unknown avg `-0.0171` n `421`
- 1h: commodity avg `-0.0094` n `12`; crypto_alt avg `-0.9271` n `228`; crypto_major avg `-0.3424` n `8`; equity avg `-0.0304` n `69`; fx avg `0.0025` n `6`; index avg `0.0729` n `23`; metal avg `-0.0286` n `18`; unknown avg `0.6153` n `421`
- 4h: commodity avg `0.1161` n `12`; crypto_alt avg `-0.8693` n `228`; crypto_major avg `-0.3391` n `8`; equity avg `0.206` n `69`; fx avg `0.0096` n `6`; index avg `0.0633` n `23`; metal avg `-0.0172` n `18`; unknown avg `0.7646` n `421`
- 24h: commodity avg `-0.0628` n `12`; crypto_alt avg `1.0615` n `228`; crypto_major avg `2.6387` n `8`; equity avg `1.0052` n `69`; fx avg `0.0267` n `6`; index avg `0.1286` n `23`; metal avg `0.0309` n `18`; unknown avg `1.1075` n `401`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1727`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1343`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1312`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1297`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1089`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1022`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0989`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0983`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0958`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0861`, n `668`, weak_sample_signal
