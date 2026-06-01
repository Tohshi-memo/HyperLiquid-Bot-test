# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-01T00:37:22.049380+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0495` n `12`; crypto_alt avg `0.2488` n `228`; crypto_major avg `0.3092` n `8`; equity avg `0.0594` n `69`; fx avg `0.0194` n `6`; index avg `0.2842` n `23`; metal avg `-0.0543` n `18`; unknown avg `0.0212` n `421`
- 1h: commodity avg `0.1311` n `12`; crypto_alt avg `1.1171` n `228`; crypto_major avg `0.7642` n `8`; equity avg `0.0564` n `69`; fx avg `0.0354` n `6`; index avg `0.3452` n `23`; metal avg `-0.0103` n `18`; unknown avg `0.1577` n `421`
- 4h: commodity avg `0.5264` n `12`; crypto_alt avg `1.8029` n `228`; crypto_major avg `1.1082` n `8`; equity avg `0.0524` n `69`; fx avg `0.0325` n `6`; index avg `0.3103` n `23`; metal avg `0.338` n `18`; unknown avg `1.1888` n `421`
- 24h: commodity avg `1.0315` n `12`; crypto_alt avg `1.4725` n `228`; crypto_major avg `0.5362` n `8`; equity avg `0.646` n `69`; fx avg `0.0098` n `6`; index avg `0.4509` n `23`; metal avg `0.1958` n `18`; unknown avg `2.1265` n `401`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2933`, n `668`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.2535`, n `668`, moderate_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.2098`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1515`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1469`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.126`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1251`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.105`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1021`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0991`, n `668`, weak_sample_signal
