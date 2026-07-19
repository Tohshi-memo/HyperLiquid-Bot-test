# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-19T10:07:28.198182+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0071` n `12`; crypto_alt avg `0.0373` n `230`; crypto_major avg `-0.0417` n `8`; equity avg `-0.0702` n `96`; fx avg `-0.0006` n `6`; index avg `-0.0014` n `25`; metal avg `-0.0037` n `20`; unknown avg `-0.0049` n `770`
- 1h: commodity avg `-0.0106` n `12`; crypto_alt avg `-0.1914` n `230`; crypto_major avg `-0.2906` n `8`; equity avg `-0.1643` n `96`; fx avg `-0.0033` n `6`; index avg `-0.0111` n `25`; metal avg `-0.0019` n `20`; unknown avg `-0.0474` n `770`
- 4h: commodity avg `0.0564` n `12`; crypto_alt avg `0.0015` n `230`; crypto_major avg `-0.004` n `8`; equity avg `0.0473` n `96`; fx avg `-0.0081` n `6`; index avg `0.0331` n `25`; metal avg `-0.0495` n `20`; unknown avg `-0.1014` n `770`
- 24h: commodity avg `0.2801` n `12`; crypto_alt avg `0.3606` n `230`; crypto_major avg `1.011` n `8`; equity avg `0.1639` n `96`; fx avg `-0.0231` n `6`; index avg `-0.0371` n `25`; metal avg `-0.0849` n `20`; unknown avg `0.0292` n `751`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1428`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1318`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1165`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1103`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1098`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0973`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0928`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0886`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.088`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.085`, n `668`, weak_sample_signal
