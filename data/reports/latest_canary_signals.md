# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-01T05:52:20.688875+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.027` n `12`; crypto_alt avg `0.3786` n `228`; crypto_major avg `0.2197` n `8`; equity avg `0.1589` n `69`; fx avg `-0.0955` n `6`; index avg `0.095` n `23`; metal avg `0.1614` n `18`; unknown avg `0.2364` n `422`
- 1h: commodity avg `0.1447` n `12`; crypto_alt avg `0.0126` n `228`; crypto_major avg `-0.0096` n `8`; equity avg `0.0389` n `69`; fx avg `-0.0974` n `6`; index avg `-0.3174` n `23`; metal avg `0.2806` n `18`; unknown avg `-0.1736` n `422`
- 4h: commodity avg `0.0552` n `12`; crypto_alt avg `0.1557` n `228`; crypto_major avg `0.165` n `8`; equity avg `0.1942` n `69`; fx avg `-0.0915` n `6`; index avg `0.0734` n `23`; metal avg `0.1246` n `18`; unknown avg `-0.4409` n `421`
- 24h: commodity avg `1.0249` n `12`; crypto_alt avg `0.3821` n `228`; crypto_major avg `-0.7855` n `8`; equity avg `0.5165` n `69`; fx avg `-0.0614` n `6`; index avg `0.4354` n `23`; metal avg `0.397` n `18`; unknown avg `1.7266` n `401`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2864`, n `668`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.2249`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.204`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1511`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1497`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1235`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1124`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1073`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1065`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0992`, n `668`, weak_sample_signal
