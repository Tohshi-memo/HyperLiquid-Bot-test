# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-20T21:52:28.385029+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0085` n `12`; crypto_alt avg `-0.2348` n `230`; crypto_major avg `-0.1758` n `8`; equity avg `0.0341` n `98`; fx avg `-0.0024` n `6`; index avg `0.0147` n `25`; metal avg `0.0017` n `20`; unknown avg `0.0311` n `770`
- 1h: commodity avg `0.005` n `12`; crypto_alt avg `-0.0246` n `230`; crypto_major avg `0.0064` n `8`; equity avg `0.1912` n `98`; fx avg `-0.0009` n `6`; index avg `0.0174` n `25`; metal avg `0.0215` n `20`; unknown avg `0.6254` n `770`
- 4h: commodity avg `0.0454` n `12`; crypto_alt avg `-0.001` n `230`; crypto_major avg `-0.1759` n `8`; equity avg `-0.7605` n `98`; fx avg `-0.0184` n `6`; index avg `-0.1299` n `25`; metal avg `-0.0269` n `20`; unknown avg `0.1353` n `770`
- 24h: commodity avg `-0.3785` n `12`; crypto_alt avg `1.8985` n `230`; crypto_major avg `1.4604` n `8`; equity avg `-0.1688` n `98`; fx avg `-0.2465` n `6`; index avg `0.0386` n `25`; metal avg `0.1365` n `20`; unknown avg `0.3282` n `745`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1548`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1316`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1273`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1078`, n `666`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1063`, n `666`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1052`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.105`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1005`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0942`, n `666`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0867`, n `666`, weak_sample_signal
