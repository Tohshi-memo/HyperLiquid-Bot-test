# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-23T07:52:26.996273+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0102` n `12`; crypto_alt avg `0.0182` n `230`; crypto_major avg `0.0335` n `8`; equity avg `-0.0016` n `98`; fx avg `-0.0159` n `6`; index avg `-0.0015` n `25`; metal avg `0.0235` n `20`; unknown avg `0.0178` n `773`
- 1h: commodity avg `0.1215` n `12`; crypto_alt avg `-0.2329` n `230`; crypto_major avg `-0.4369` n `8`; equity avg `-0.4138` n `98`; fx avg `0.0202` n `6`; index avg `-0.0941` n `25`; metal avg `-0.3081` n `20`; unknown avg `0.1024` n `773`
- 4h: commodity avg `0.2265` n `12`; crypto_alt avg `0.0636` n `230`; crypto_major avg `-0.3616` n `8`; equity avg `-0.4218` n `98`; fx avg `0.0402` n `6`; index avg `-0.0952` n `25`; metal avg `-0.3986` n `20`; unknown avg `-0.2596` n `741`
- 24h: commodity avg `0.5845` n `12`; crypto_alt avg `0.0835` n `230`; crypto_major avg `0.019` n `8`; equity avg `0.3122` n `98`; fx avg `-0.0535` n `6`; index avg `0.1247` n `25`; metal avg `-0.2574` n `20`; unknown avg `11.4043` n `741`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1524`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1319`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1293`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1195`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1078`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1042`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0938`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0909`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0892`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0854`, n `666`, weak_sample_signal
