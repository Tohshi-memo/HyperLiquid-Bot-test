# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-08T23:22:31.278495+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0249` n `12`; crypto_alt avg `-0.1466` n `229`; crypto_major avg `-0.1211` n `8`; equity avg `-0.1285` n `91`; fx avg `-0.0029` n `6`; index avg `-0.013` n `25`; metal avg `-0.0103` n `20`; unknown avg `0.0069` n `764`
- 1h: commodity avg `-0.0476` n `12`; crypto_alt avg `0.0585` n `229`; crypto_major avg `0.048` n `8`; equity avg `-0.1057` n `91`; fx avg `-0.0379` n `6`; index avg `-0.005` n `25`; metal avg `0.0085` n `20`; unknown avg `0.0518` n `764`
- 4h: commodity avg `0.1413` n `12`; crypto_alt avg `0.0826` n `229`; crypto_major avg `0.142` n `8`; equity avg `0.3317` n `91`; fx avg `-0.0005` n `6`; index avg `-0.001` n `25`; metal avg `-0.0999` n `20`; unknown avg `-0.2507` n `764`
- 24h: commodity avg `0.3281` n `12`; crypto_alt avg `-1.7295` n `229`; crypto_major avg `-2.5378` n `8`; equity avg `1.4489` n `91`; fx avg `-0.013` n `6`; index avg `-0.0045` n `25`; metal avg `-0.7255` n `20`; unknown avg `-0.1073` n `739`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1038`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0929`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0706`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0661`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0617`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0596`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0564`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0546`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0512`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0503`, n `668`, weak_sample_signal
