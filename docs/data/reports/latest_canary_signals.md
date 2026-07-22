# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-22T23:22:30.735801+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0119` n `12`; crypto_alt avg `-0.2887` n `230`; crypto_major avg `-0.2519` n `8`; equity avg `-0.0457` n `98`; fx avg `0.0084` n `6`; index avg `0.0015` n `25`; metal avg `0.0271` n `20`; unknown avg `0.1772` n `773`
- 1h: commodity avg `-0.0409` n `12`; crypto_alt avg `-0.409` n `230`; crypto_major avg `-0.1774` n `8`; equity avg `-0.2031` n `98`; fx avg `0.0133` n `6`; index avg `-0.0496` n `25`; metal avg `-0.0193` n `20`; unknown avg `0.1137` n `773`
- 4h: commodity avg `0.1488` n `12`; crypto_alt avg `-0.2683` n `230`; crypto_major avg `-0.14` n `8`; equity avg `-0.1916` n `98`; fx avg `-0.014` n `6`; index avg `-0.0781` n `25`; metal avg `-0.1142` n `20`; unknown avg `0.1869` n `773`
- 24h: commodity avg `0.6968` n `12`; crypto_alt avg `-0.5181` n `230`; crypto_major avg `-0.4887` n `8`; equity avg `-1.3836` n `98`; fx avg `-0.05` n `6`; index avg `-0.2139` n `25`; metal avg `0.139` n `20`; unknown avg `1.6954` n `739`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.162`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1256`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1218`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.102`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0962`, n `666`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0942`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0905`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0854`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0818`, n `666`, weak_sample_signal
