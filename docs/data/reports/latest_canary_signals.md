# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-20T16:51:07.606237+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0258` n `12`; crypto_alt avg `0.0627` n `230`; crypto_major avg `-0.007` n `8`; equity avg `-0.1702` n `98`; fx avg `-0.0044` n `6`; index avg `-0.0274` n `25`; metal avg `-0.0335` n `20`; unknown avg `-0.115` n `770`
- 1h: commodity avg `0.0448` n `12`; crypto_alt avg `0.0983` n `230`; crypto_major avg `0.0285` n `8`; equity avg `0.1812` n `98`; fx avg `-0.0057` n `6`; index avg `-0.0011` n `25`; metal avg `-0.0438` n `20`; unknown avg `-0.1507` n `770`
- 4h: commodity avg `-0.1654` n `12`; crypto_alt avg `0.8595` n `230`; crypto_major avg `1.0159` n `8`; equity avg `-0.062` n `98`; fx avg `-0.0906` n `6`; index avg `-0.0017` n `25`; metal avg `0.0605` n `20`; unknown avg `-0.0893` n `770`
- 24h: commodity avg `-0.5672` n `12`; crypto_alt avg `1.6066` n `230`; crypto_major avg `1.4561` n `8`; equity avg `0.8085` n `97`; fx avg `-0.1479` n `6`; index avg `0.253` n `25`; metal avg `0.2246` n `20`; unknown avg `0.0608` n `745`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1511`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1271`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1266`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1042`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1003`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0971`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0962`, n `666`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0888`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0852`, n `666`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0805`, n `666`, weak_sample_signal
