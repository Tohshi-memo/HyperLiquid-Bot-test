# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-09T10:22:28.212960+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0462` n `12`; crypto_alt avg `-0.0876` n `229`; crypto_major avg `-0.1559` n `8`; equity avg `0.0216` n `91`; fx avg `-0.0058` n `6`; index avg `0.0082` n `25`; metal avg `-0.043` n `20`; unknown avg `-0.0414` n `764`
- 1h: commodity avg `0.1168` n `12`; crypto_alt avg `0.0679` n `229`; crypto_major avg `0.0378` n `8`; equity avg `0.0341` n `91`; fx avg `-0.0125` n `6`; index avg `0.0055` n `25`; metal avg `-0.0789` n `20`; unknown avg `0.0188` n `764`
- 4h: commodity avg `0.0729` n `12`; crypto_alt avg `0.0322` n `229`; crypto_major avg `-0.16` n `8`; equity avg `0.3899` n `91`; fx avg `0.0482` n `6`; index avg `0.0343` n `25`; metal avg `0.1434` n `20`; unknown avg `-0.076` n `764`
- 24h: commodity avg `-0.3949` n `12`; crypto_alt avg `1.9362` n `229`; crypto_major avg `0.9568` n `8`; equity avg `3.6942` n `91`; fx avg `0.1499` n `6`; index avg `0.5587` n `25`; metal avg `0.5559` n `20`; unknown avg `0.826` n `741`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.0997`, n `670`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0977`, n `670`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0698`, n `670`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0669`, n `670`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0647`, n `670`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0624`, n `670`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0624`, n `670`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0579`, n `670`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0575`, n `670`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0549`, n `670`, weak_sample_signal
