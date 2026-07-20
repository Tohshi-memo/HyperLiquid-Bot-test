# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-20T16:37:30.589467+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0765` n `12`; crypto_alt avg `0.0165` n `230`; crypto_major avg `-0.0091` n `8`; equity avg `-0.0154` n `98`; fx avg `-0.0048` n `6`; index avg `-0.0452` n `25`; metal avg `-0.0349` n `20`; unknown avg `0.0393` n `770`
- 1h: commodity avg `0.0397` n `12`; crypto_alt avg `0.558` n `230`; crypto_major avg `0.7807` n `8`; equity avg `0.4616` n `98`; fx avg `-0.0004` n `6`; index avg `0.0293` n `25`; metal avg `0.0154` n `20`; unknown avg `0.0709` n `770`
- 4h: commodity avg `-0.111` n `12`; crypto_alt avg `0.6473` n `230`; crypto_major avg `0.9463` n `8`; equity avg `0.0141` n `98`; fx avg `-0.0911` n `6`; index avg `-0.0146` n `25`; metal avg `0.089` n `20`; unknown avg `0.0072` n `770`
- 24h: commodity avg `-0.5509` n `12`; crypto_alt avg `1.5477` n `230`; crypto_major avg `1.4294` n `8`; equity avg `1.0095` n `97`; fx avg `-0.1429` n `6`; index avg `0.2888` n `25`; metal avg `0.2542` n `20`; unknown avg `0.1843` n `745`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1513`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1269`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1254`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1027`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1013`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.099`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0966`, n `666`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0875`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0847`, n `666`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0815`, n `666`, weak_sample_signal
