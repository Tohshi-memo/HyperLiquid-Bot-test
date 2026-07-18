# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-18T23:37:29.737466+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0805` n `12`; crypto_alt avg `0.0147` n `230`; crypto_major avg `-0.0148` n `8`; equity avg `-0.0159` n `96`; fx avg `-0.0035` n `6`; index avg `-0.0016` n `25`; metal avg `-0.0011` n `20`; unknown avg `0.2262` n `770`
- 1h: commodity avg `-0.0408` n `12`; crypto_alt avg `0.1619` n `230`; crypto_major avg `0.1081` n `8`; equity avg `0.036` n `96`; fx avg `-0.004` n `6`; index avg `0.0047` n `25`; metal avg `0.0043` n `20`; unknown avg `-0.1744` n `770`
- 4h: commodity avg `-0.0643` n `12`; crypto_alt avg `0.3216` n `230`; crypto_major avg `0.2336` n `8`; equity avg `0.013` n `96`; fx avg `0.0058` n `6`; index avg `-0.0013` n `25`; metal avg `-0.0159` n `20`; unknown avg `0.4216` n `770`
- 24h: commodity avg `0.2511` n `12`; crypto_alt avg `-0.2659` n `230`; crypto_major avg `0.5025` n `8`; equity avg `-0.1934` n `96`; fx avg `-0.0813` n `6`; index avg `0.0635` n `25`; metal avg `-0.0333` n `20`; unknown avg `0.0703` n `737`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `0.1126`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1036`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0967`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0936`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0869`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0806`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0776`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0769`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0747`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0726`, n `668`, weak_sample_signal
