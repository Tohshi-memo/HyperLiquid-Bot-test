# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-31T23:41:51.892001+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0184` n `12`; crypto_alt avg `-0.3746` n `228`; crypto_major avg `-0.3888` n `8`; equity avg `-0.0174` n `69`; fx avg `0.0016` n `6`; index avg `0.0203` n `23`; metal avg `0.1303` n `18`; unknown avg `-0.1604` n `421`
- 1h: commodity avg `-0.0257` n `12`; crypto_alt avg `-0.4558` n `228`; crypto_major avg `-0.5907` n `8`; equity avg `-0.0478` n `69`; fx avg `0.0007` n `6`; index avg `-0.2716` n `23`; metal avg `0.342` n `18`; unknown avg `0.021` n `421`
- 4h: commodity avg `0.292` n `12`; crypto_alt avg `1.3904` n `228`; crypto_major avg `0.7625` n `8`; equity avg `-0.008` n `69`; fx avg `-0.0114` n `6`; index avg `-0.233` n `23`; metal avg `0.3293` n `18`; unknown avg `1.4548` n `421`
- 24h: commodity avg `0.8783` n `12`; crypto_alt avg `0.7964` n `228`; crypto_major avg `0.1842` n `8`; equity avg `0.6486` n `69`; fx avg `-0.019` n `6`; index avg `0.0662` n `23`; metal avg `0.2119` n `18`; unknown avg `1.8008` n `401`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.3387`, n `668`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.2544`, n `668`, moderate_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1996`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1579`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1517`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1447`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1281`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1047`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1025`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1002`, n `668`, weak_sample_signal
