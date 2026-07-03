# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-03T10:07:35.774594+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0038` n `12`; crypto_alt avg `0.0722` n `229`; crypto_major avg `0.0308` n `8`; equity avg `0.0311` n `88`; fx avg `0.007` n `6`; index avg `0.0037` n `25`; metal avg `0.0104` n `20`; unknown avg `-0.0532` n `765`
- 1h: commodity avg `-0.0079` n `12`; crypto_alt avg `0.089` n `229`; crypto_major avg `-0.1118` n `8`; equity avg `0.087` n `88`; fx avg `0.0195` n `6`; index avg `0.0375` n `25`; metal avg `-0.0207` n `20`; unknown avg `0.2433` n `755`
- 4h: commodity avg `-0.117` n `12`; crypto_alt avg `0.3891` n `229`; crypto_major avg `0.0211` n `8`; equity avg `0.067` n `88`; fx avg `-0.0359` n `6`; index avg `0.027` n `25`; metal avg `0.0598` n `20`; unknown avg `-0.006` n `755`
- 24h: commodity avg `0.4205` n `12`; crypto_alt avg `1.5855` n `229`; crypto_major avg `2.4189` n `8`; equity avg `0.3056` n `88`; fx avg `-0.0814` n `6`; index avg `0.2635` n `25`; metal avg `1.1983` n `20`; unknown avg `5.5214` n `737`

## Correlations

- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1236`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.123`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0762`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0729`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0698`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0677`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0617`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0599`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0596`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0584`, n `668`, weak_sample_signal
