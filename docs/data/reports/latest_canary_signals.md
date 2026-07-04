# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-04T12:52:30.661662+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0008` n `12`; crypto_alt avg `0.0101` n `229`; crypto_major avg `-0.0203` n `8`; equity avg `0.0111` n `88`; fx avg `0.0011` n `6`; index avg `-0.0263` n `25`; metal avg `0.008` n `20`; unknown avg `0.0085` n `765`
- 1h: commodity avg `0.0108` n `12`; crypto_alt avg `0.2115` n `229`; crypto_major avg `0.1224` n `8`; equity avg `-0.0153` n `88`; fx avg `0.0116` n `6`; index avg `-0.0101` n `25`; metal avg `-0.0036` n `20`; unknown avg `-0.0253` n `765`
- 4h: commodity avg `0.1461` n `12`; crypto_alt avg `0.4719` n `229`; crypto_major avg `-0.2204` n `8`; equity avg `-0.042` n `88`; fx avg `0.0107` n `6`; index avg `-0.0075` n `25`; metal avg `0.0092` n `20`; unknown avg `-0.2797` n `765`
- 24h: commodity avg `0.1995` n `12`; crypto_alt avg `1.0766` n `229`; crypto_major avg `1.4863` n `8`; equity avg `0.1684` n `88`; fx avg `-0.0741` n `6`; index avg `-0.0472` n `25`; metal avg `-0.0513` n `20`; unknown avg `2.9757` n `743`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.0935`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0909`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0853`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0844`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.079`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0774`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0709`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0671`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0659`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0598`, n `668`, weak_sample_signal
