# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-09T04:07:31.808516+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0174` n `12`; crypto_alt avg `0.0775` n `229`; crypto_major avg `0.0126` n `8`; equity avg `0.0321` n `91`; fx avg `-0.0019` n `6`; index avg `-0.0017` n `25`; metal avg `-0.0025` n `20`; unknown avg `-0.0342` n `764`
- 1h: commodity avg `-0.0196` n `12`; crypto_alt avg `0.2948` n `229`; crypto_major avg `0.3231` n `8`; equity avg `0.2446` n `91`; fx avg `-0.0098` n `6`; index avg `0.1034` n `25`; metal avg `0.0347` n `20`; unknown avg `-0.0111` n `764`
- 4h: commodity avg `0.0078` n `12`; crypto_alt avg `-0.1687` n `229`; crypto_major avg `-0.2238` n `8`; equity avg `-0.3474` n `91`; fx avg `0.0233` n `6`; index avg `-0.1149` n `25`; metal avg `-0.172` n `20`; unknown avg `-0.4315` n `764`
- 24h: commodity avg `0.3256` n `12`; crypto_alt avg `-0.2619` n `229`; crypto_major avg `-0.8225` n `8`; equity avg `0.4612` n `91`; fx avg `0.0223` n `6`; index avg `-0.1082` n `25`; metal avg `-1.0479` n `20`; unknown avg `0.0683` n `739`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1012`, n `669`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0934`, n `669`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0829`, n `669`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0778`, n `669`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0668`, n `669`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0643`, n `669`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0639`, n `669`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0605`, n `669`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.06`, n `669`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0575`, n `669`, weak_sample_signal
