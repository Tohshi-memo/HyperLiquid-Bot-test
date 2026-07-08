# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-08T23:56:03.716418+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0057` n `12`; crypto_alt avg `0.1827` n `229`; crypto_major avg `0.2307` n `8`; equity avg `0.1866` n `91`; fx avg `-0.0207` n `6`; index avg `-0.0024` n `25`; metal avg `0.0365` n `20`; unknown avg `0.1509` n `764`
- 1h: commodity avg `-0.0373` n `12`; crypto_alt avg `0.1248` n `229`; crypto_major avg `0.2372` n `8`; equity avg `0.1994` n `91`; fx avg `-0.0201` n `6`; index avg `0.0078` n `25`; metal avg `0.0024` n `20`; unknown avg `0.144` n `764`
- 4h: commodity avg `0.0619` n `12`; crypto_alt avg `0.3499` n `229`; crypto_major avg `0.3698` n `8`; equity avg `0.4924` n `91`; fx avg `-0.0137` n `6`; index avg `0.0271` n `25`; metal avg `-0.0033` n `20`; unknown avg `-0.0729` n `764`
- 24h: commodity avg `0.3313` n `12`; crypto_alt avg `-1.2381` n `229`; crypto_major avg `-1.887` n `8`; equity avg `2.063` n `91`; fx avg `-0.0902` n `6`; index avg `0.0877` n `25`; metal avg `-0.6385` n `20`; unknown avg `-0.0619` n `739`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1028`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0918`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0702`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0652`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0605`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0599`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0557`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.055`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0518`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0504`, n `668`, weak_sample_signal
