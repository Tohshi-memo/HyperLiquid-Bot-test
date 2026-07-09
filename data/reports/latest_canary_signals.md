# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-09T04:37:29.877802+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0257` n `12`; crypto_alt avg `0.2636` n `229`; crypto_major avg `0.3154` n `8`; equity avg `0.1589` n `91`; fx avg `0.0121` n `6`; index avg `0.0523` n `25`; metal avg `0.0571` n `20`; unknown avg `0.6985` n `764`
- 1h: commodity avg `0.0094` n `12`; crypto_alt avg `0.4451` n `229`; crypto_major avg `0.3533` n `8`; equity avg `0.1406` n `91`; fx avg `-0.0213` n `6`; index avg `0.006` n `25`; metal avg `0.0273` n `20`; unknown avg `0.1209` n `764`
- 4h: commodity avg `0.0082` n `12`; crypto_alt avg `0.3166` n `229`; crypto_major avg `0.0526` n `8`; equity avg `-0.2842` n `91`; fx avg `0.0357` n `6`; index avg `-0.122` n `25`; metal avg `-0.1346` n `20`; unknown avg `-0.525` n `764`
- 24h: commodity avg `0.3444` n `12`; crypto_alt avg `0.1794` n `229`; crypto_major avg `-0.3934` n `8`; equity avg `1.0124` n `91`; fx avg `0.017` n `6`; index avg `0.0284` n `25`; metal avg `-1.0371` n `20`; unknown avg `0.0841` n `739`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.0988`, n `669`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0901`, n `669`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0792`, n `669`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0755`, n `669`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0668`, n `669`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0628`, n `669`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0611`, n `669`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.061`, n `669`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0609`, n `669`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0571`, n `669`, weak_sample_signal
