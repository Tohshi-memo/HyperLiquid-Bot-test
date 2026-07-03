# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-03T12:07:31.600844+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0434` n `12`; crypto_alt avg `0.1536` n `229`; crypto_major avg `0.0169` n `8`; equity avg `0.017` n `88`; fx avg `-0.0006` n `6`; index avg `0.0153` n `25`; metal avg `0.0075` n `20`; unknown avg `0.0852` n `765`
- 1h: commodity avg `-0.1308` n `12`; crypto_alt avg `0.2056` n `229`; crypto_major avg `0.0863` n `8`; equity avg `0.0025` n `88`; fx avg `-0.0002` n `6`; index avg `0.0192` n `25`; metal avg `0.0174` n `20`; unknown avg `0.3691` n `765`
- 4h: commodity avg `-0.1336` n `12`; crypto_alt avg `1.1642` n `229`; crypto_major avg `0.9961` n `8`; equity avg `0.1941` n `88`; fx avg `0.0329` n `6`; index avg `0.0214` n `25`; metal avg `-0.1318` n `20`; unknown avg `1.1158` n `755`
- 24h: commodity avg `0.3972` n `12`; crypto_alt avg `2.1598` n `229`; crypto_major avg `2.3407` n `8`; equity avg `-0.197` n `88`; fx avg `-0.0605` n `6`; index avg `0.1631` n `25`; metal avg `1.1605` n `20`; unknown avg `6.4254` n `737`

## Correlations

- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1241`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1221`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0766`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0737`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0698`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0687`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0666`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0635`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.063`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0618`, n `668`, weak_sample_signal
