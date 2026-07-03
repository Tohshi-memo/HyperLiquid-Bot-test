# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-03T19:07:39.656261+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0454` n `12`; crypto_alt avg `-0.0074` n `229`; crypto_major avg `0.0021` n `8`; equity avg `-0.0267` n `88`; fx avg `0.0056` n `6`; index avg `-0.0034` n `25`; metal avg `-0.0028` n `20`; unknown avg `0.2611` n `765`
- 1h: commodity avg `-0.0254` n `12`; crypto_alt avg `0.0208` n `229`; crypto_major avg `0.1636` n `8`; equity avg `-0.0612` n `88`; fx avg `0.0046` n `6`; index avg `-0.0101` n `25`; metal avg `-0.0146` n `20`; unknown avg `0.0642` n `765`
- 4h: commodity avg `0.0177` n `12`; crypto_alt avg `-0.0984` n `229`; crypto_major avg `0.0242` n `8`; equity avg `-0.0128` n `88`; fx avg `-0.0308` n `6`; index avg `0.0217` n `25`; metal avg `-0.0773` n `20`; unknown avg `2.4971` n `765`
- 24h: commodity avg `0.182` n `12`; crypto_alt avg `2.6474` n `229`; crypto_major avg `2.4109` n `8`; equity avg `2.37` n `88`; fx avg `-0.0532` n `6`; index avg `0.6615` n `25`; metal avg `0.6474` n `20`; unknown avg `9.3358` n `739`

## Correlations

- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1043`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0997`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0817`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0812`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0746`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0735`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0734`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0681`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0659`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0544`, n `668`, weak_sample_signal
