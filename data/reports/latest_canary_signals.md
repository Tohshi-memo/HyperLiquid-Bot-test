# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-01T00:07:21.938154+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0398` n `12`; crypto_alt avg `0.2661` n `228`; crypto_major avg `0.1022` n `8`; equity avg `-0.1828` n `69`; fx avg `0.0086` n `6`; index avg `0.1008` n `23`; metal avg `-0.0015` n `18`; unknown avg `-0.012` n `421`
- 1h: commodity avg `-0.058` n `12`; crypto_alt avg `-0.1302` n `228`; crypto_major avg `-0.3135` n `8`; equity avg `-0.1818` n `69`; fx avg `-0.0001` n `6`; index avg `-0.1805` n `23`; metal avg `0.2676` n `18`; unknown avg `-0.0511` n `421`
- 4h: commodity avg `0.4077` n `12`; crypto_alt avg `1.4615` n `228`; crypto_major avg `0.8273` n `8`; equity avg `-0.1256` n `69`; fx avg `-0.0115` n `6`; index avg `0.1275` n `23`; metal avg `0.3989` n `18`; unknown avg `1.3222` n `421`
- 24h: commodity avg `0.8218` n `12`; crypto_alt avg `1.1804` n `228`; crypto_major avg `0.3625` n `8`; equity avg `0.4541` n `69`; fx avg `-0.0258` n `6`; index avg `0.2389` n `23`; metal avg `0.2692` n `18`; unknown avg `1.9254` n `401`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.3111`, n `668`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.2554`, n `668`, moderate_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.208`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1496`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1422`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1388`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1305`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0996`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0985`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0985`, n `668`, weak_sample_signal
