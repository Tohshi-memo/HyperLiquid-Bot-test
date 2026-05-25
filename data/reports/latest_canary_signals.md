# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-25T04:22:19.845376+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0652` n `12`; crypto_alt avg `0.0453` n `228`; crypto_major avg `-0.0035` n `8`; equity avg `0.0124` n `67`; fx avg `0.0018` n `6`; index avg `0.0212` n `23`; metal avg `0.1098` n `18`; unknown avg `-0.179` n `397`
- 1h: commodity avg `-0.1222` n `12`; crypto_alt avg `0.0835` n `228`; crypto_major avg `0.0494` n `8`; equity avg `0.1068` n `67`; fx avg `0.0085` n `6`; index avg `0.1214` n `23`; metal avg `0.0684` n `18`; unknown avg `-0.2119` n `397`
- 4h: commodity avg `-0.453` n `12`; crypto_alt avg `-0.0401` n `228`; crypto_major avg `-0.5018` n `8`; equity avg `0.3676` n `67`; fx avg `-0.0671` n `6`; index avg `0.3029` n `23`; metal avg `-0.162` n `18`; unknown avg `-0.2763` n `396`
- 24h: commodity avg `0.0879` n `12`; crypto_alt avg `-1.0465` n `228`; crypto_major avg `-0.2246` n `8`; equity avg `0.477` n `67`; fx avg `-0.0499` n `6`; index avg `-0.0717` n `23`; metal avg `0.578` n `18`; unknown avg `-0.3623` n `386`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1495`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1321`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1266`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1231`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1221`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1178`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1151`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1128`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1113`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1104`, n `668`, weak_sample_signal
