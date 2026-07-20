# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-20T23:07:26.570593+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0064` n `12`; crypto_alt avg `0.1977` n `230`; crypto_major avg `0.1579` n `8`; equity avg `0.0538` n `98`; fx avg `0.0026` n `6`; index avg `0.0331` n `25`; metal avg `0.0378` n `20`; unknown avg `0.0115` n `770`
- 1h: commodity avg `0.0042` n `12`; crypto_alt avg `0.0163` n `230`; crypto_major avg `-0.0666` n `8`; equity avg `0.0265` n `98`; fx avg `-0.0007` n `6`; index avg `0.0292` n `25`; metal avg `-0.0156` n `20`; unknown avg `-0.0655` n `770`
- 4h: commodity avg `-0.0816` n `12`; crypto_alt avg `-0.0327` n `230`; crypto_major avg `-0.0761` n `8`; equity avg `-0.1444` n `98`; fx avg `-0.0346` n `6`; index avg `-0.0391` n `25`; metal avg `-0.0285` n `20`; unknown avg `-0.3132` n `770`
- 24h: commodity avg `-0.3407` n `12`; crypto_alt avg `1.327` n `230`; crypto_major avg `0.9647` n `8`; equity avg `-0.3105` n `98`; fx avg `-0.1983` n `6`; index avg `-0.0336` n `25`; metal avg `0.1866` n `20`; unknown avg `0.2028` n `745`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1559`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1283`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1271`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1084`, n `666`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1065`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.105`, n `666`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1023`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0987`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0951`, n `666`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0863`, n `666`, weak_sample_signal
