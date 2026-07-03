# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-03T12:22:35.601653+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0552` n `12`; crypto_alt avg `-0.1478` n `229`; crypto_major avg `-0.3215` n `8`; equity avg `-0.0623` n `88`; fx avg `-0.0239` n `6`; index avg `-0.0113` n `25`; metal avg `-0.1081` n `20`; unknown avg `0.0289` n `765`
- 1h: commodity avg `-0.0179` n `12`; crypto_alt avg `0.0485` n `229`; crypto_major avg `-0.276` n `8`; equity avg `-0.0938` n `88`; fx avg `-0.0246` n `6`; index avg `-0.0003` n `25`; metal avg `-0.1328` n `20`; unknown avg `0.0357` n `765`
- 4h: commodity avg `-0.0554` n `12`; crypto_alt avg `0.9794` n `229`; crypto_major avg `0.7206` n `8`; equity avg `0.137` n `88`; fx avg `0.0215` n `6`; index avg `0.0245` n `25`; metal avg `-0.2277` n `20`; unknown avg `1.039` n `755`
- 24h: commodity avg `0.5116` n `12`; crypto_alt avg `1.9606` n `229`; crypto_major avg `2.0056` n `8`; equity avg `-0.3598` n `88`; fx avg `-0.0745` n `6`; index avg `0.1143` n `25`; metal avg `1.1213` n `20`; unknown avg `6.1806` n `737`

## Correlations

- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1242`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1223`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0764`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0737`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0698`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0687`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0681`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.065`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0631`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.063`, n `668`, weak_sample_signal
