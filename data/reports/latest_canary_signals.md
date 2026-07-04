# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-04T21:52:24.554350+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0034` n `12`; crypto_alt avg `-0.0908` n `229`; crypto_major avg `-0.0636` n `8`; equity avg `-0.0075` n `88`; fx avg `-0.001` n `6`; index avg `0.0039` n `25`; metal avg `-0.0087` n `20`; unknown avg `0.4715` n `765`
- 1h: commodity avg `-0.0291` n `12`; crypto_alt avg `0.1224` n `229`; crypto_major avg `0.1615` n `8`; equity avg `0.0218` n `88`; fx avg `-0.0022` n `6`; index avg `0.0019` n `25`; metal avg `0.0071` n `20`; unknown avg `4.32` n `765`
- 4h: commodity avg `-0.0873` n `12`; crypto_alt avg `-0.705` n `229`; crypto_major avg `-0.7623` n `8`; equity avg `0.0109` n `88`; fx avg `-0.0412` n `6`; index avg `0.0176` n `25`; metal avg `0.0353` n `20`; unknown avg `-0.9505` n `765`
- 24h: commodity avg `-0.0262` n `12`; crypto_alt avg `0.1944` n `229`; crypto_major avg `0.4958` n `8`; equity avg `0.2399` n `88`; fx avg `-0.0306` n `6`; index avg `-0.0117` n `25`; metal avg `0.0908` n `20`; unknown avg `-0.234` n `741`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0973`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0947`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0936`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0883`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0874`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0814`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0763`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0761`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0717`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0616`, n `668`, weak_sample_signal
