# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-04T04:52:30.828478+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0009` n `12`; crypto_alt avg `0.0991` n `229`; crypto_major avg `0.0728` n `8`; equity avg `0.0272` n `88`; fx avg `0.0` n `6`; index avg `0.0077` n `25`; metal avg `0.0047` n `20`; unknown avg `0.0594` n `765`
- 1h: commodity avg `-0.0422` n `12`; crypto_alt avg `0.1639` n `229`; crypto_major avg `0.4934` n `8`; equity avg `0.1113` n `88`; fx avg `0.0056` n `6`; index avg `0.0059` n `25`; metal avg `0.0176` n `20`; unknown avg `0.856` n `765`
- 4h: commodity avg `-0.085` n `12`; crypto_alt avg `0.0758` n `229`; crypto_major avg `0.4392` n `8`; equity avg `0.1779` n `88`; fx avg `-0.0075` n `6`; index avg `0.0338` n `25`; metal avg `0.0083` n `20`; unknown avg `0.3171` n `763`
- 24h: commodity avg `-0.0933` n `12`; crypto_alt avg `2.5822` n `229`; crypto_major avg `3.6194` n `8`; equity avg `0.477` n `88`; fx avg `-0.1604` n `6`; index avg `0.0373` n `25`; metal avg `-0.104` n `20`; unknown avg `4.3016` n `737`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0989`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0989`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0869`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0805`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0786`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0778`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0707`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0669`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0618`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0538`, n `668`, weak_sample_signal
