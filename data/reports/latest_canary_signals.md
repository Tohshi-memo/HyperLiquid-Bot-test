# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-23T16:52:35.980785+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.016` n `12`; crypto_alt avg `-0.1489` n `228`; crypto_major avg `-0.1243` n `8`; equity avg `-0.0787` n `86`; fx avg `0.0109` n `6`; index avg `-0.011` n `23`; metal avg `-0.033` n `20`; unknown avg `-0.1304` n `764`
- 1h: commodity avg `-0.1523` n `12`; crypto_alt avg `0.2471` n `228`; crypto_major avg `0.3624` n `8`; equity avg `0.2667` n `86`; fx avg `0.0147` n `6`; index avg `0.0491` n `23`; metal avg `-0.0115` n `20`; unknown avg `0.3921` n `764`
- 4h: commodity avg `-0.3048` n `12`; crypto_alt avg `0.1317` n `228`; crypto_major avg `-0.0281` n `8`; equity avg `0.9975` n `86`; fx avg `-0.0664` n `6`; index avg `0.0787` n `23`; metal avg `0.1149` n `20`; unknown avg `-0.1821` n `764`
- 24h: commodity avg `-0.5884` n `12`; crypto_alt avg `-3.7486` n `228`; crypto_major avg `-3.9815` n `8`; equity avg `-2.8425` n `86`; fx avg `-0.1775` n `6`; index avg `-0.888` n `23`; metal avg `-0.9614` n `20`; unknown avg `-0.0524` n `604`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1285`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1241`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1173`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1062`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0866`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.08`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0711`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0673`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.063`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0624`, n `668`, weak_sample_signal
