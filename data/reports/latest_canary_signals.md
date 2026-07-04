# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-04T05:52:30.938601+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0001` n `12`; crypto_alt avg `0.0972` n `229`; crypto_major avg `0.093` n `8`; equity avg `0.012` n `88`; fx avg `0.0012` n `6`; index avg `-0.0016` n `25`; metal avg `0.0072` n `20`; unknown avg `-0.3592` n `761`
- 1h: commodity avg `0.0035` n `12`; crypto_alt avg `-0.1783` n `229`; crypto_major avg `-0.3204` n `8`; equity avg `-0.0002` n `88`; fx avg `0.0027` n `6`; index avg `-0.0131` n `25`; metal avg `0.0004` n `20`; unknown avg `-0.4078` n `761`
- 4h: commodity avg `-0.03` n `12`; crypto_alt avg `0.4437` n `229`; crypto_major avg `0.7156` n `8`; equity avg `0.2512` n `88`; fx avg `0.0129` n `6`; index avg `0.0149` n `25`; metal avg `0.0278` n `20`; unknown avg `-0.2825` n `759`
- 24h: commodity avg `-0.1566` n `12`; crypto_alt avg `2.1825` n `229`; crypto_major avg `2.6658` n `8`; equity avg `0.6069` n `88`; fx avg `-0.1728` n `6`; index avg `0.0511` n `25`; metal avg `-0.0812` n `20`; unknown avg `4.5057` n `733`

## Correlations

- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1006`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1003`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0869`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0796`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0791`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.079`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0707`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0679`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0603`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0518`, n `668`, weak_sample_signal
