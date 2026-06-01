# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-01T01:37:21.328615+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0337` n `12`; crypto_alt avg `-0.1434` n `228`; crypto_major avg `-0.1988` n `8`; equity avg `0.0034` n `69`; fx avg `0.0115` n `6`; index avg `0.0055` n `23`; metal avg `-0.0474` n `18`; unknown avg `-0.0657` n `421`
- 1h: commodity avg `0.143` n `12`; crypto_alt avg `-0.5552` n `228`; crypto_major avg `-0.5167` n `8`; equity avg `-0.114` n `69`; fx avg `0.0372` n `6`; index avg `-0.0806` n `23`; metal avg `-0.0408` n `18`; unknown avg `-0.3671` n `421`
- 4h: commodity avg `0.7374` n `12`; crypto_alt avg `0.8589` n `228`; crypto_major avg `0.1557` n `8`; equity avg `-0.1751` n `69`; fx avg `0.0732` n `6`; index avg `0.1247` n `23`; metal avg `0.2689` n `18`; unknown avg `0.3664` n `421`
- 24h: commodity avg `1.0258` n `12`; crypto_alt avg `0.4535` n `228`; crypto_major avg `-0.4499` n `8`; equity avg `0.4195` n `69`; fx avg `0.0621` n `6`; index avg `0.333` n `23`; metal avg `0.1498` n `18`; unknown avg `1.5235` n `401`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2816`, n `668`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.2562`, n `668`, moderate_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.2056`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1529`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1486`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1226`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.118`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1064`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.102`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0978`, n `668`, weak_sample_signal
