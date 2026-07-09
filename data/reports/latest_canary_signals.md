# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-09T15:37:27.081808+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.003` n `12`; crypto_alt avg `-0.3149` n `229`; crypto_major avg `-0.3922` n `8`; equity avg `-0.0298` n `91`; fx avg `0.0183` n `6`; index avg `0.004` n `25`; metal avg `0.0046` n `20`; unknown avg `-0.0238` n `765`
- 1h: commodity avg `-0.1991` n `12`; crypto_alt avg `-0.0799` n `229`; crypto_major avg `0.0675` n `8`; equity avg `0.4971` n `91`; fx avg `-0.0079` n `6`; index avg `0.0729` n `25`; metal avg `0.0912` n `20`; unknown avg `0.0573` n `765`
- 4h: commodity avg `-0.7906` n `12`; crypto_alt avg `0.049` n `229`; crypto_major avg `0.1786` n `8`; equity avg `1.0119` n `91`; fx avg `-0.0326` n `6`; index avg `0.2341` n `25`; metal avg `0.4662` n `20`; unknown avg `0.2039` n `764`
- 24h: commodity avg `-1.301` n `12`; crypto_alt avg `1.5729` n `229`; crypto_major avg `1.1754` n `8`; equity avg `3.3809` n `91`; fx avg `0.0575` n `6`; index avg `0.6117` n `25`; metal avg `1.3946` n `20`; unknown avg `1.212` n `748`

## Correlations

- market_context_score -> fx_forward_1h_return_pct: corr `-0.0916`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0871`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0732`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0719`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0665`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0654`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0651`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0616`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0603`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0603`, n `668`, weak_sample_signal
