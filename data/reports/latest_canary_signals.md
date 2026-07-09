# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-09T18:26:24.033990+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1492` n `12`; crypto_alt avg `-0.1352` n `229`; crypto_major avg `-0.218` n `8`; equity avg `-0.1315` n `91`; fx avg `-0.0164` n `6`; index avg `-0.0068` n `25`; metal avg `-0.067` n `20`; unknown avg `0.1794` n `765`
- 1h: commodity avg `0.0795` n `12`; crypto_alt avg `0.401` n `229`; crypto_major avg `0.3434` n `8`; equity avg `-0.0729` n `91`; fx avg `-0.0234` n `6`; index avg `0.0101` n `25`; metal avg `-0.0324` n `20`; unknown avg `0.1829` n `765`
- 4h: commodity avg `-0.3657` n `12`; crypto_alt avg `0.3415` n `229`; crypto_major avg `0.5136` n `8`; equity avg `0.9464` n `91`; fx avg `-0.0234` n `6`; index avg `0.2227` n `25`; metal avg `0.0854` n `20`; unknown avg `0.0529` n `765`
- 24h: commodity avg `-0.8504` n `12`; crypto_alt avg `1.3544` n `229`; crypto_major avg `0.7619` n `8`; equity avg `2.4619` n `91`; fx avg `0.0444` n `6`; index avg `0.3997` n `25`; metal avg `0.8414` n `20`; unknown avg `1.0274` n `748`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1024`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0918`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0798`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.074`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0695`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0648`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0628`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0627`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0607`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0605`, n `668`, weak_sample_signal
