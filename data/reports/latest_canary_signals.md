# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-31T20:07:20.452173+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.2523` n `12`; crypto_alt avg `0.3106` n `228`; crypto_major avg `0.2126` n `8`; equity avg `-0.0457` n `69`; fx avg `-0.0007` n `6`; index avg `-0.104` n `23`; metal avg `-0.0093` n `18`; unknown avg `0.1273` n `421`
- 1h: commodity avg `-0.2509` n `12`; crypto_alt avg `0.4424` n `228`; crypto_major avg `0.2115` n `8`; equity avg `0.0217` n `69`; fx avg `0.0014` n `6`; index avg `-0.0308` n `23`; metal avg `-0.0205` n `18`; unknown avg `0.1113` n `421`
- 4h: commodity avg `-0.1869` n `12`; crypto_alt avg `0.2924` n `228`; crypto_major avg `-0.2066` n `8`; equity avg `-0.0277` n `69`; fx avg `0.0012` n `6`; index avg `0.1579` n `23`; metal avg `-0.0092` n `18`; unknown avg `0.2043` n `421`
- 24h: commodity avg `0.5236` n `12`; crypto_alt avg `-1.066` n `228`; crypto_major avg `-0.741` n `8`; equity avg `0.8136` n `69`; fx avg `-0.0244` n `6`; index avg `0.3043` n `23`; metal avg `-0.1438` n `18`; unknown avg `0.445` n `401`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2579`, n `668`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1811`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1519`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.14`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1209`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1154`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1113`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0802`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0798`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0791`, n `668`, weak_sample_signal
