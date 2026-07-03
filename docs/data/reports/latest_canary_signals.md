# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-03T13:19:06.148901+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0194` n `12`; crypto_alt avg `0.0597` n `229`; crypto_major avg `0.0586` n `8`; equity avg `0.0272` n `88`; fx avg `0.0025` n `6`; index avg `0.0021` n `25`; metal avg `-0.0298` n `20`; unknown avg `0.621` n `765`
- 1h: commodity avg `0.0689` n `12`; crypto_alt avg `0.1887` n `229`; crypto_major avg `0.3033` n `8`; equity avg `-0.0776` n `88`; fx avg `0.0209` n `6`; index avg `0.0023` n `25`; metal avg `-0.0261` n `20`; unknown avg `1.1586` n `765`
- 4h: commodity avg `0.0025` n `12`; crypto_alt avg `1.0216` n `229`; crypto_major avg `0.8553` n `8`; equity avg `0.0552` n `88`; fx avg `0.028` n `6`; index avg `0.0433` n `25`; metal avg `-0.1807` n `20`; unknown avg `2.3339` n `755`
- 24h: commodity avg `0.4533` n `12`; crypto_alt avg `1.7378` n `229`; crypto_major avg `1.6656` n `8`; equity avg `-0.9138` n `88`; fx avg `-0.1047` n `6`; index avg `0.0413` n `25`; metal avg `0.5578` n `20`; unknown avg `7.803` n `737`

## Correlations

- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1155`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1129`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0736`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0734`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0725`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0696`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0683`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0631`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0605`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0603`, n `668`, weak_sample_signal
