# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-31T20:37:22.089945+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0026` n `12`; crypto_alt avg `0.0018` n `228`; crypto_major avg `0.0258` n `8`; equity avg `0.0187` n `69`; fx avg `0.0` n `6`; index avg `0.0385` n `23`; metal avg `0.0088` n `18`; unknown avg `0.0013` n `421`
- 1h: commodity avg `-0.0981` n `12`; crypto_alt avg `0.7074` n `228`; crypto_major avg `0.4199` n `8`; equity avg `-0.0051` n `69`; fx avg `-0.0085` n `6`; index avg `-0.1892` n `23`; metal avg `-0.019` n `18`; unknown avg `0.4801` n `421`
- 4h: commodity avg `0.0125` n `12`; crypto_alt avg `1.0574` n `228`; crypto_major avg `0.553` n `8`; equity avg `0.1147` n `69`; fx avg `-0.0103` n `6`; index avg `0.1672` n `23`; metal avg `-0.0176` n `18`; unknown avg `0.2203` n `421`
- 24h: commodity avg `0.5432` n `12`; crypto_alt avg `-0.907` n `228`; crypto_major avg `-0.4629` n `8`; equity avg `0.7605` n `69`; fx avg `-0.0343` n `6`; index avg `0.1756` n `23`; metal avg `-0.1626` n `18`; unknown avg `0.6134` n `401`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2693`, n `668`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1928`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1533`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1506`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1195`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1182`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1165`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0838`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0809`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.079`, n `668`, weak_sample_signal
