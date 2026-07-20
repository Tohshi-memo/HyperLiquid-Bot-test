# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-20T15:22:28.000357+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0254` n `12`; crypto_alt avg `0.2804` n `230`; crypto_major avg `0.2814` n `8`; equity avg `0.2762` n `98`; fx avg `-0.0166` n `6`; index avg `0.0442` n `25`; metal avg `0.0414` n `20`; unknown avg `-0.0034` n `770`
- 1h: commodity avg `-0.0586` n `12`; crypto_alt avg `0.8641` n `230`; crypto_major avg `1.1189` n `8`; equity avg `0.5142` n `98`; fx avg `-0.068` n `6`; index avg `0.0203` n `25`; metal avg `0.1429` n `20`; unknown avg `0.5164` n `770`
- 4h: commodity avg `-0.0007` n `12`; crypto_alt avg `0.5316` n `230`; crypto_major avg `0.6878` n `8`; equity avg `-0.3522` n `98`; fx avg `-0.1075` n `6`; index avg `-0.0559` n `25`; metal avg `-0.0217` n `20`; unknown avg `0.318` n `770`
- 24h: commodity avg `-0.5711` n `12`; crypto_alt avg `0.8482` n `230`; crypto_major avg `0.492` n `8`; equity avg `0.46` n `97`; fx avg `-0.1437` n `6`; index avg `0.1286` n `25`; metal avg `0.2029` n `20`; unknown avg `-0.0274` n `745`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1501`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1257`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1063`, n `666`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1016`, n `666`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1001`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0952`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0943`, n `666`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0862`, n `666`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0822`, n `666`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0783`, n `668`, weak_sample_signal
