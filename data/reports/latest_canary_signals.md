# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-09T00:22:31.217433+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0191` n `12`; crypto_alt avg `-0.1212` n `229`; crypto_major avg `-0.1063` n `8`; equity avg `0.1101` n `91`; fx avg `-0.0297` n `6`; index avg `0.0319` n `25`; metal avg `-0.0222` n `20`; unknown avg `0.0139` n `764`
- 1h: commodity avg `-0.0436` n `12`; crypto_alt avg `0.1404` n `229`; crypto_major avg `0.0114` n `8`; equity avg `0.553` n `91`; fx avg `-0.034` n `6`; index avg `0.0848` n `25`; metal avg `0.0393` n `20`; unknown avg `-0.0594` n `764`
- 4h: commodity avg `-0.1152` n `12`; crypto_alt avg `0.2334` n `229`; crypto_major avg `-0.0087` n `8`; equity avg `0.6713` n `91`; fx avg `-0.0482` n `6`; index avg `0.1057` n `25`; metal avg `0.0557` n `20`; unknown avg `-0.2502` n `764`
- 24h: commodity avg `0.2119` n `12`; crypto_alt avg `-1.4041` n `229`; crypto_major avg `-2.2065` n `8`; equity avg `1.5033` n `91`; fx avg `-0.0921` n `6`; index avg `0.0302` n `25`; metal avg `-0.6253` n `20`; unknown avg `-0.0684` n `739`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1022`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0909`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0707`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0651`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0599`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0594`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0574`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0551`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0535`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0511`, n `668`, weak_sample_signal
