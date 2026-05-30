# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-30T06:07:23.047627+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.03` n `12`; crypto_alt avg `-0.1662` n `228`; crypto_major avg `-0.0796` n `8`; equity avg `-0.0303` n `69`; fx avg `-0.0022` n `6`; index avg `0.0263` n `23`; metal avg `0.0254` n `18`; unknown avg `0.7724` n `401`
- 1h: commodity avg `-0.0289` n `12`; crypto_alt avg `0.0605` n `228`; crypto_major avg `0.2307` n `8`; equity avg `0.0552` n `69`; fx avg `0.0058` n `6`; index avg `0.0669` n `23`; metal avg `0.0068` n `18`; unknown avg `0.031` n `401`
- 4h: commodity avg `-0.2682` n `12`; crypto_alt avg `-0.3231` n `228`; crypto_major avg `-0.0792` n `8`; equity avg `0.1463` n `69`; fx avg `0.005` n `6`; index avg `0.0823` n `23`; metal avg `-0.0053` n `18`; unknown avg `0.9344` n `401`
- 24h: commodity avg `-0.3248` n `12`; crypto_alt avg `1.5796` n `228`; crypto_major avg `1.9403` n `8`; equity avg `0.8817` n `69`; fx avg `0.0827` n `6`; index avg `0.0544` n `23`; metal avg `-0.09` n `18`; unknown avg `1.5736` n `399`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1913`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1651`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1642`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1512`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1325`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1229`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1166`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.116`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1126`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1113`, n `668`, weak_sample_signal
