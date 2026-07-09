# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-09T07:24:40.263664+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0003` n `12`; crypto_alt avg `-0.2357` n `229`; crypto_major avg `-0.1764` n `8`; equity avg `0.0729` n `91`; fx avg `-0.006` n `6`; index avg `0.0235` n `25`; metal avg `0.0729` n `20`; unknown avg `-0.0477` n `764`
- 1h: commodity avg `0.0839` n `12`; crypto_alt avg `-0.0006` n `229`; crypto_major avg `-0.0451` n `8`; equity avg `0.2548` n `91`; fx avg `0.0414` n `6`; index avg `0.0503` n `25`; metal avg `0.1479` n `20`; unknown avg `0.0364` n `764`
- 4h: commodity avg `-0.1805` n `12`; crypto_alt avg `1.0912` n `229`; crypto_major avg `1.0454` n `8`; equity avg `0.9601` n `91`; fx avg `0.0666` n `6`; index avg `0.2138` n `25`; metal avg `0.6645` n `20`; unknown avg `0.088` n `748`
- 24h: commodity avg `0.1046` n `12`; crypto_alt avg `0.6545` n `229`; crypto_major avg `0.3697` n `8`; equity avg `1.892` n `91`; fx avg `0.168` n `6`; index avg `0.2286` n `25`; metal avg `-0.3469` n `20`; unknown avg `0.3779` n `741`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.102`, n `669`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.101`, n `669`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0732`, n `669`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0667`, n `669`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0653`, n `669`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.065`, n `669`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0634`, n `669`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.059`, n `669`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0587`, n `669`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0556`, n `669`, weak_sample_signal
