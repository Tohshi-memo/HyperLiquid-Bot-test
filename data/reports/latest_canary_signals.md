# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-20T18:37:31.512102+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `1.6753` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0715` n `12`; crypto_alt avg `-0.0021` n `230`; crypto_major avg `-0.0623` n `8`; equity avg `-0.1603` n `98`; fx avg `-0.0047` n `6`; index avg `-0.0445` n `25`; metal avg `-0.0212` n `20`; unknown avg `0.1614` n `770`
- 1h: commodity avg `0.1318` n `12`; crypto_alt avg `0.3139` n `230`; crypto_major avg `0.2987` n `8`; equity avg `-0.0378` n `98`; fx avg `0.0152` n `6`; index avg `-0.0272` n `25`; metal avg `-0.0599` n `20`; unknown avg `0.0444` n `770`
- 4h: commodity avg `0.2974` n `12`; crypto_alt avg `1.2793` n `230`; crypto_major avg `1.632` n `8`; equity avg `0.3272` n `98`; fx avg `-0.0448` n `6`; index avg `-0.0633` n `25`; metal avg `-0.0433` n `20`; unknown avg `0.4355` n `770`
- 24h: commodity avg `-0.2708` n `12`; crypto_alt avg `2.1021` n `230`; crypto_major avg `1.7758` n `8`; equity avg `0.5406` n `98`; fx avg `-0.1367` n `6`; index avg `0.1578` n `25`; metal avg `0.1434` n `20`; unknown avg `0.5652` n `745`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1522`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1346`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.127`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1048`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1015`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0997`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0989`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0959`, n `666`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0844`, n `666`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0836`, n `666`, weak_sample_signal
