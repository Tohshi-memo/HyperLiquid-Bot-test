# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-09T21:37:29.286736+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0125` n `12`; crypto_alt avg `-0.097` n `229`; crypto_major avg `-0.0964` n `8`; equity avg `-0.0137` n `91`; fx avg `-0.0005` n `6`; index avg `-0.004` n `25`; metal avg `0.0085` n `20`; unknown avg `-0.2431` n `765`
- 1h: commodity avg `0.0469` n `12`; crypto_alt avg `-0.1211` n `229`; crypto_major avg `-0.0945` n `8`; equity avg `0.0102` n `91`; fx avg `0.0212` n `6`; index avg `-0.0063` n `25`; metal avg `0.0101` n `20`; unknown avg `-0.3317` n `765`
- 4h: commodity avg `0.1241` n `12`; crypto_alt avg `0.1904` n `229`; crypto_major avg `0.2685` n `8`; equity avg `-0.3508` n `91`; fx avg `-0.016` n `6`; index avg `-0.0198` n `25`; metal avg `-0.2609` n `20`; unknown avg `-0.1446` n `765`
- 24h: commodity avg `-1.2244` n `12`; crypto_alt avg `1.4071` n `229`; crypto_major avg `0.9207` n `8`; equity avg `1.6532` n `91`; fx avg `0.0389` n `6`; index avg `0.3696` n `25`; metal avg `0.7058` n `20`; unknown avg `-0.1591` n `748`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1053`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0933`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0812`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0727`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.072`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0709`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0662`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0644`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0636`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0625`, n `668`, weak_sample_signal
