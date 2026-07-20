# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-20T10:42:22.917188+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0528` n `12`; crypto_alt avg `0.0526` n `230`; crypto_major avg `0.0073` n `8`; equity avg `0.069` n `98`; fx avg `0.0083` n `6`; index avg `-0.0005` n `25`; metal avg `-0.0275` n `20`; unknown avg `0.0429` n `770`
- 1h: commodity avg `0.1369` n `12`; crypto_alt avg `0.1874` n `230`; crypto_major avg `0.1087` n `8`; equity avg `0.2378` n `98`; fx avg `0.0239` n `6`; index avg `0.023` n `25`; metal avg `0.0102` n `20`; unknown avg `0.0191` n `770`
- 4h: commodity avg `-0.5207` n `12`; crypto_alt avg `1.2359` n `230`; crypto_major avg `0.892` n `8`; equity avg `0.8559` n `98`; fx avg `0.0443` n `6`; index avg `0.1645` n `25`; metal avg `0.2119` n `20`; unknown avg `0.1629` n `763`
- 24h: crypto_alt avg `0.4068` n `225`; crypto_major avg `-0.2133` n `7`; metal avg `0.2946` n `1`; unknown avg `-0.0372` n `679`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1503`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1254`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.105`, n `666`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0986`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0941`, n `666`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.088`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0855`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.079`, n `666`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0789`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0789`, n `668`, weak_sample_signal
