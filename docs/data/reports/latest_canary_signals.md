# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-20T12:37:25.171683+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.021` n `12`; crypto_alt avg `0.0082` n `230`; crypto_major avg `0.0206` n `8`; equity avg `0.1415` n `98`; fx avg `0.014` n `6`; index avg `0.031` n `25`; metal avg `0.0217` n `20`; unknown avg `0.0514` n `770`
- 1h: commodity avg `0.4707` n `12`; crypto_alt avg `-0.0179` n `230`; crypto_major avg `-0.2505` n `8`; equity avg `-0.1969` n `98`; fx avg `0.0049` n `6`; index avg `-0.0524` n `25`; metal avg `-0.1974` n `20`; unknown avg `0.0624` n `770`
- 4h: commodity avg `0.1672` n `12`; crypto_alt avg `1.1587` n `230`; crypto_major avg `1.0661` n `8`; equity avg `0.8469` n `98`; fx avg `-0.0289` n `6`; index avg `0.1855` n `25`; metal avg `-0.1113` n `20`; unknown avg `0.1957` n `770`
- 24h: commodity avg `-0.4543` n `12`; crypto_alt avg `0.9336` n `230`; crypto_major avg `0.3935` n `8`; equity avg `0.9389` n `97`; fx avg `-0.0465` n `6`; index avg `0.2102` n `25`; metal avg `0.1682` n `20`; unknown avg `0.0488` n `745`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.15`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1246`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1081`, n `666`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1051`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1047`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1015`, n `666`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0895`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0797`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0783`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0774`, n `666`, weak_sample_signal
