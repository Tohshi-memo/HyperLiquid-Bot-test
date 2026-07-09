# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-09T00:37:26.256500+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0109` n `12`; crypto_alt avg `0.0046` n `229`; crypto_major avg `0.1701` n `8`; equity avg `-0.062` n `91`; fx avg `-0.0019` n `6`; index avg `-0.0172` n `25`; metal avg `0.0145` n `20`; unknown avg `0.0645` n `764`
- 1h: commodity avg `-0.0282` n `12`; crypto_alt avg `0.1571` n `229`; crypto_major avg `0.1589` n `8`; equity avg `0.3221` n `91`; fx avg `-0.0438` n `6`; index avg `0.0224` n `25`; metal avg `0.0464` n `20`; unknown avg `0.0214` n `764`
- 4h: commodity avg `-0.1689` n `12`; crypto_alt avg `0.3796` n `229`; crypto_major avg `0.3321` n `8`; equity avg `0.7265` n `91`; fx avg `-0.0255` n `6`; index avg `0.0946` n `25`; metal avg `0.1477` n `20`; unknown avg `-0.12` n `764`
- 24h: commodity avg `0.3333` n `12`; crypto_alt avg `-1.6382` n `229`; crypto_major avg `-2.1092` n `8`; equity avg `1.39` n `91`; fx avg `-0.0943` n `6`; index avg `-0.0301` n `25`; metal avg `-0.717` n `20`; unknown avg `-0.1109` n `739`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1028`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0909`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0728`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0671`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0595`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0589`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0587`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0548`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0547`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0516`, n `668`, weak_sample_signal
