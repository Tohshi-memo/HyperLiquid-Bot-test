# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-30T16:47:24.764544+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0215` n `12`; crypto_alt avg `-0.0809` n `228`; crypto_major avg `-0.1925` n `8`; equity avg `0.0135` n `69`; fx avg `0.0007` n `6`; index avg `-0.013` n `23`; metal avg `-0.005` n `18`; unknown avg `0.0035` n `421`
- 1h: commodity avg `-0.3477` n `12`; crypto_alt avg `0.1469` n `228`; crypto_major avg `0.1264` n `8`; equity avg `-0.14` n `69`; fx avg `-0.0115` n `6`; index avg `-0.0601` n `23`; metal avg `0.0062` n `18`; unknown avg `0.987` n `421`
- 4h: commodity avg `-0.2915` n `12`; crypto_alt avg `0.3218` n `228`; crypto_major avg `0.7052` n `8`; equity avg `-0.0025` n `69`; fx avg `-0.0027` n `6`; index avg `-0.02` n `23`; metal avg `0.0061` n `18`; unknown avg `1.1661` n `421`
- 24h: commodity avg `0.148` n `12`; crypto_alt avg `0.6404` n `228`; crypto_major avg `1.3486` n `8`; equity avg `0.8262` n `69`; fx avg `0.0075` n `6`; index avg `0.1469` n `23`; metal avg `-0.1677` n `18`; unknown avg `1.0831` n `401`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1917`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1628`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1566`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1484`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1343`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1256`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1223`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1195`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1114`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1107`, n `668`, weak_sample_signal
