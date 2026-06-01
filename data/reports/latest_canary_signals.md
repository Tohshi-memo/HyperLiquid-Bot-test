# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-01T03:52:21.139764+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1321` n `12`; crypto_alt avg `-0.1322` n `228`; crypto_major avg `-0.0687` n `8`; equity avg `-0.1394` n `69`; fx avg `-0.0103` n `6`; index avg `-0.0128` n `23`; metal avg `-0.2545` n `18`; unknown avg `0.6205` n `422`
- 1h: commodity avg `0.0904` n `12`; crypto_alt avg `0.1977` n `228`; crypto_major avg `0.1498` n `8`; equity avg `0.1067` n `69`; fx avg `-0.0176` n `6`; index avg `0.0588` n `23`; metal avg `-0.2307` n `18`; unknown avg `0.5809` n `422`
- 4h: commodity avg `0.2431` n `12`; crypto_alt avg `1.014` n `228`; crypto_major avg `0.3236` n `8`; equity avg `0.0498` n `69`; fx avg `0.0921` n `6`; index avg `0.5513` n `23`; metal avg `-0.2949` n `18`; unknown avg `0.4939` n `421`
- 24h: commodity avg `1.0993` n `12`; crypto_alt avg `1.1751` n `228`; crypto_major avg `-0.1524` n `8`; equity avg `0.5205` n `69`; fx avg `0.0378` n `6`; index avg `0.704` n `23`; metal avg `0.0214` n `18`; unknown avg `1.8805` n `401`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2878`, n `668`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.2245`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.2031`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1375`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.136`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1232`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1073`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0977`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0937`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0902`, n `668`, weak_sample_signal
