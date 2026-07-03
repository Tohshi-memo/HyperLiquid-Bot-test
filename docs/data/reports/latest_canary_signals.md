# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-03T10:52:30.264475+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0505` n `12`; crypto_alt avg `0.3737` n `229`; crypto_major avg `0.4055` n `8`; equity avg `0.0954` n `88`; fx avg `0.005` n `6`; index avg `0.012` n `25`; metal avg `-0.0034` n `20`; unknown avg `-0.0027` n `765`
- 1h: commodity avg `-0.0188` n `12`; crypto_alt avg `0.6254` n `229`; crypto_major avg `0.8356` n `8`; equity avg `0.2318` n `88`; fx avg `0.0101` n `6`; index avg `0.0175` n `25`; metal avg `-0.0329` n `20`; unknown avg `0.5613` n `765`
- 4h: commodity avg `-0.1138` n `12`; crypto_alt avg `0.9707` n `229`; crypto_major avg `1.0487` n `8`; equity avg `0.331` n `88`; fx avg `0.0346` n `6`; index avg `0.0542` n `25`; metal avg `0.0109` n `20`; unknown avg `1.057` n `755`
- 24h: commodity avg `0.4091` n `12`; crypto_alt avg `2.0915` n `229`; crypto_major avg `2.6937` n `8`; equity avg `0.3882` n `88`; fx avg `-0.0906` n `6`; index avg `0.2471` n `25`; metal avg `1.2031` n `20`; unknown avg `5.8277` n `737`

## Correlations

- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1251`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.123`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0759`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0734`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0699`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0684`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0644`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0627`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0606`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0604`, n `668`, weak_sample_signal
