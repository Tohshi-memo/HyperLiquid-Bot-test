# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-18T23:33:25.978135+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0541` n `12`; crypto_alt avg `0.0126` n `230`; crypto_major avg `-0.0263` n `8`; equity avg `-0.0149` n `96`; fx avg `-0.0035` n `6`; index avg `-0.0035` n `25`; metal avg `-0.0021` n `20`; unknown avg `-0.0901` n `770`
- 1h: commodity avg `-0.0144` n `12`; crypto_alt avg `0.1598` n `230`; crypto_major avg `0.0965` n `8`; equity avg `0.037` n `96`; fx avg `-0.004` n `6`; index avg `0.0029` n `25`; metal avg `0.0033` n `20`; unknown avg `-0.1879` n `770`
- 4h: commodity avg `-0.0379` n `12`; crypto_alt avg `0.3195` n `230`; crypto_major avg `0.222` n `8`; equity avg `0.0141` n `96`; fx avg `0.0058` n `6`; index avg `-0.0031` n `25`; metal avg `-0.0169` n `20`; unknown avg `0.3126` n `770`
- 24h: commodity avg `0.2781` n `12`; crypto_alt avg `-0.2681` n `230`; crypto_major avg `0.4909` n `8`; equity avg `-0.1922` n `96`; fx avg `-0.0813` n `6`; index avg `0.0617` n `25`; metal avg `-0.0343` n `20`; unknown avg `0.0725` n `737`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `0.1126`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1049`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0966`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0936`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0869`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0806`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0776`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0764`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0747`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0725`, n `668`, weak_sample_signal
