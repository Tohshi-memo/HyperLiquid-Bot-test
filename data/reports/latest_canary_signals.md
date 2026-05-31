# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-31T18:50:02.649745+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0259` n `12`; crypto_alt avg `-0.038` n `228`; crypto_major avg `-0.1289` n `8`; equity avg `0.0601` n `69`; fx avg `-0.0037` n `6`; index avg `-0.0209` n `23`; metal avg `-0.0014` n `18`; unknown avg `0.7598` n `421`
- 1h: commodity avg `0.0231` n `12`; crypto_alt avg `-0.1058` n `228`; crypto_major avg `-0.3046` n `8`; equity avg `0.038` n `69`; fx avg `-0.0016` n `6`; index avg `-0.0764` n `23`; metal avg `0.0098` n `18`; unknown avg `0.619` n `421`
- 4h: commodity avg `0.1629` n `12`; crypto_alt avg `0.0378` n `228`; crypto_major avg `-0.3353` n `8`; equity avg `0.1405` n `69`; fx avg `-0.0081` n `6`; index avg `0.2433` n `23`; metal avg `-0.0522` n `18`; unknown avg `0.6381` n `421`
- 24h: commodity avg `0.7006` n `12`; crypto_alt avg `-1.3986` n `228`; crypto_major avg `-0.8114` n `8`; equity avg `0.9354` n `69`; fx avg `-0.0116` n `6`; index avg `0.1171` n `23`; metal avg `-0.1359` n `18`; unknown avg `1.1391` n `401`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2321`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1791`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1487`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1303`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1219`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1197`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1128`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0823`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0788`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0783`, n `668`, weak_sample_signal
