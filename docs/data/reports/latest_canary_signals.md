# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-20T10:07:31.920254+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0604` n `12`; crypto_alt avg `-0.071` n `230`; crypto_major avg `-0.1292` n `8`; equity avg `-0.1735` n `98`; fx avg `0.0012` n `6`; index avg `-0.0359` n `25`; metal avg `-0.0346` n `20`; unknown avg `-0.0446` n `770`
- 1h: commodity avg `-0.0269` n `12`; crypto_alt avg `0.3119` n `230`; crypto_major avg `0.2809` n `8`; equity avg `0.3151` n `98`; fx avg `-0.0013` n `6`; index avg `0.0598` n `25`; metal avg `0.065` n `20`; unknown avg `-0.018` n `770`
- 4h: commodity avg `-0.5519` n `12`; crypto_alt avg `0.9001` n `230`; crypto_major avg `0.2789` n `8`; equity avg `0.4896` n `98`; fx avg `0.0176` n `6`; index avg `0.1394` n `25`; metal avg `0.2075` n `20`; unknown avg `-0.0162` n `763`
- 24h: commodity avg `-0.5794` n `12`; crypto_alt avg `0.2331` n `230`; crypto_major avg `-0.2612` n `8`; equity avg `0.4278` n `97`; fx avg `-0.0263` n `6`; index avg `0.0997` n `25`; metal avg `0.2236` n `20`; unknown avg `-0.0475` n `745`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1499`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.125`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1035`, n `666`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0969`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0913`, n `666`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0856`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0834`, n `666`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0785`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0757`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0745`, n `666`, weak_sample_signal
