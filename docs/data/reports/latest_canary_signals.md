# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-03T17:37:30.926963+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0087` n `12`; crypto_alt avg `0.0534` n `229`; crypto_major avg `0.0848` n `8`; equity avg `-0.0198` n `88`; fx avg `0.0034` n `6`; index avg `0.0304` n `25`; metal avg `0.0017` n `20`; unknown avg `-0.0146` n `765`
- 1h: commodity avg `0.0452` n `12`; crypto_alt avg `0.2504` n `229`; crypto_major avg `0.3574` n `8`; equity avg `0.0427` n `88`; fx avg `-0.0141` n `6`; index avg `0.0196` n `25`; metal avg `0.0456` n `20`; unknown avg `0.0151` n `765`
- 4h: commodity avg `0.0271` n `12`; crypto_alt avg `0.3276` n `229`; crypto_major avg `0.5158` n `8`; equity avg `0.0761` n `88`; fx avg `-0.0332` n `6`; index avg `0.0271` n `25`; metal avg `0.0481` n `20`; unknown avg `0.4707` n `765`
- 24h: commodity avg `0.2511` n `12`; crypto_alt avg `2.759` n `229`; crypto_major avg `2.4215` n `8`; equity avg `2.5237` n `88`; fx avg `-0.0174` n `6`; index avg `0.7154` n `25`; metal avg `0.7244` n `20`; unknown avg `8.3054` n `739`

## Correlations

- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1039`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0996`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0797`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.076`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0736`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0728`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0717`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0678`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0657`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0529`, n `668`, weak_sample_signal
