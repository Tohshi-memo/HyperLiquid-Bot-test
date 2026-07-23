# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-23T09:07:32.018569+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0288` n `12`; crypto_alt avg `0.0623` n `230`; crypto_major avg `0.1519` n `8`; equity avg `0.2215` n `98`; fx avg `-0.0141` n `6`; index avg `0.063` n `25`; metal avg `0.0981` n `20`; unknown avg `-0.0166` n `773`
- 1h: commodity avg `0.0366` n `12`; crypto_alt avg `0.2606` n `230`; crypto_major avg `0.3294` n `8`; equity avg `0.484` n `98`; fx avg `-0.0073` n `6`; index avg `0.0685` n `25`; metal avg `0.0129` n `20`; unknown avg `0.0056` n `773`
- 4h: commodity avg `0.2119` n `12`; crypto_alt avg `0.2177` n `230`; crypto_major avg `0.0935` n `8`; equity avg `0.4207` n `98`; fx avg `0.0069` n `6`; index avg `0.0116` n `25`; metal avg `-0.2986` n `20`; unknown avg `-0.0444` n `741`
- 24h: commodity avg `0.6607` n `12`; crypto_alt avg `0.0106` n `230`; crypto_major avg `0.0526` n `8`; equity avg `0.7957` n `98`; fx avg `-0.0661` n `6`; index avg `0.1712` n `25`; metal avg `-0.2994` n `20`; unknown avg `11.4995` n `741`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1511`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1404`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1387`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1116`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1073`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.101`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0893`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0821`, n `666`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0804`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0787`, n `668`, weak_sample_signal
