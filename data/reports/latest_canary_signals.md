# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-20T09:22:29.388464+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0702` n `12`; crypto_alt avg `0.1944` n `230`; crypto_major avg `0.2388` n `8`; equity avg `0.1683` n `98`; fx avg `-0.0062` n `6`; index avg `0.0234` n `25`; metal avg `0.0394` n `20`; unknown avg `0.0137` n `770`
- 1h: commodity avg `-0.0363` n `12`; crypto_alt avg `0.0423` n `230`; crypto_major avg `0.0167` n `8`; equity avg `-0.0165` n `98`; fx avg `-0.0273` n `6`; index avg `0.0261` n `25`; metal avg `-0.0665` n `20`; unknown avg `-0.0127` n `769`
- 4h: commodity avg `-0.5023` n `12`; crypto_alt avg `0.7748` n `230`; crypto_major avg `0.1765` n `8`; equity avg `0.2313` n `98`; fx avg `-0.0097` n `6`; index avg `0.088` n `25`; metal avg `0.1367` n `20`; unknown avg `-0.0102` n `747`
- 24h: commodity avg `-0.6231` n `12`; crypto_alt avg `0.1813` n `230`; crypto_major avg `-0.3261` n `8`; equity avg `0.2011` n `97`; fx avg `-0.0351` n `6`; index avg `0.0501` n `25`; metal avg `0.1958` n `20`; unknown avg `-0.0159` n `745`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.15`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1242`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1022`, n `666`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0963`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0892`, n `666`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0859`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0801`, n `666`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0776`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0771`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0759`, n `668`, weak_sample_signal
