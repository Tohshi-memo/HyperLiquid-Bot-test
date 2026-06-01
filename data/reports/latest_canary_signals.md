# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-01T00:22:15.553993+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1455` n `12`; crypto_alt avg `0.2344` n `228`; crypto_major avg `0.0426` n `8`; equity avg `0.1157` n `69`; fx avg `0.0159` n `6`; index avg `-0.0941` n `23`; metal avg `-0.0178` n `18`; unknown avg `0.0081` n `421`
- 1h: commodity avg `0.0628` n `12`; crypto_alt avg `0.4872` n `228`; crypto_major avg `0.0623` n `8`; equity avg `-0.0291` n `69`; fx avg `0.0176` n `6`; index avg `0.082` n `23`; metal avg `0.1744` n `18`; unknown avg `-0.0615` n `421`
- 4h: commodity avg `0.4746` n `12`; crypto_alt avg `1.5501` n `228`; crypto_major avg `0.8227` n `8`; equity avg `0.003` n `69`; fx avg `0.0131` n `6`; index avg `0.0598` n `23`; metal avg `0.4014` n `18`; unknown avg `1.1431` n `421`
- 24h: commodity avg `0.9368` n `12`; crypto_alt avg `1.1234` n `228`; crypto_major avg `0.1801` n `8`; equity avg `0.6005` n `69`; fx avg `-0.0112` n `6`; index avg `0.1629` n `23`; metal avg `0.2552` n `18`; unknown avg `1.9141` n `401`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.299`, n `668`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.2552`, n `668`, moderate_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.2081`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1481`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1424`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1298`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1293`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1007`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0983`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0963`, n `668`, weak_sample_signal
