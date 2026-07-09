# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-09T18:37:33.602888+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0763` n `12`; crypto_alt avg `0.0776` n `229`; crypto_major avg `0.066` n `8`; equity avg `-0.0199` n `91`; fx avg `-0.0062` n `6`; index avg `-0.0094` n `25`; metal avg `-0.0463` n `20`; unknown avg `-0.0566` n `765`
- 1h: commodity avg `0.1002` n `12`; crypto_alt avg `0.4555` n `229`; crypto_major avg `0.4237` n `8`; equity avg `-0.0528` n `91`; fx avg `-0.0204` n `6`; index avg `-0.0023` n `25`; metal avg `-0.1263` n `20`; unknown avg `0.3046` n `765`
- 4h: commodity avg `-0.3756` n `12`; crypto_alt avg `0.4146` n `229`; crypto_major avg `0.5477` n `8`; equity avg `0.5584` n `91`; fx avg `-0.0237` n `6`; index avg `0.1449` n `25`; metal avg `-0.0631` n `20`; unknown avg `0.0753` n `765`
- 24h: commodity avg `-0.973` n `12`; crypto_alt avg `1.6227` n `229`; crypto_major avg `1.2174` n `8`; equity avg `2.4586` n `91`; fx avg `0.0449` n `6`; index avg `0.421` n `25`; metal avg `0.7719` n `20`; unknown avg `1.0945` n `748`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1016`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0916`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0804`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0748`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0708`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0651`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.063`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0628`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0607`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0605`, n `668`, weak_sample_signal
