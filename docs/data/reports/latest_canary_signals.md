# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-09T19:52:29.326599+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0112` n `12`; crypto_alt avg `-0.0754` n `229`; crypto_major avg `-0.0398` n `8`; equity avg `-0.1786` n `91`; fx avg `0.0046` n `6`; index avg `-0.0021` n `25`; metal avg `0.0141` n `20`; unknown avg `0.0077` n `765`
- 1h: commodity avg `0.0221` n `12`; crypto_alt avg `-0.1642` n `229`; crypto_major avg `-0.0663` n `8`; equity avg `-0.4308` n `91`; fx avg `-0.0065` n `6`; index avg `-0.0202` n `25`; metal avg `-0.1643` n `20`; unknown avg `0.0011` n `765`
- 4h: commodity avg `-0.1055` n `12`; crypto_alt avg `0.3068` n `229`; crypto_major avg `0.1969` n `8`; equity avg `-0.4724` n `91`; fx avg `-0.0297` n `6`; index avg `0.0239` n `25`; metal avg `-0.3477` n `20`; unknown avg `-0.0984` n `765`
- 24h: commodity avg `-1.0475` n `12`; crypto_alt avg `1.315` n `229`; crypto_major avg `0.7478` n `8`; equity avg `1.687` n `91`; fx avg `0.0407` n `6`; index avg `0.3391` n `25`; metal avg `0.5731` n `20`; unknown avg `0.0835` n `748`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1096`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0942`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0811`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0749`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0735`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0721`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0628`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0618`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0616`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0591`, n `668`, weak_sample_signal
