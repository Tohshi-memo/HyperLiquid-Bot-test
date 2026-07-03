# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-03T10:22:40.672523+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0179` n `12`; crypto_alt avg `0.0813` n `229`; crypto_major avg `0.1755` n `8`; equity avg `0.0559` n `88`; fx avg `0.0003` n `6`; index avg `0.0015` n `25`; metal avg `0.018` n `20`; unknown avg `0.0136` n `765`
- 1h: commodity avg `-0.0402` n `12`; crypto_alt avg `0.1979` n `229`; crypto_major avg `0.1424` n `8`; equity avg `0.0848` n `88`; fx avg `0.0235` n `6`; index avg `0.0254` n `25`; metal avg `0.016` n `20`; unknown avg `0.0197` n `755`
- 4h: commodity avg `-0.1017` n `12`; crypto_alt avg `0.4004` n `229`; crypto_major avg `0.3071` n `8`; equity avg `0.1284` n `88`; fx avg `-0.0197` n `6`; index avg `0.0122` n `25`; metal avg `0.1432` n `20`; unknown avg `0.0059` n `755`
- 24h: commodity avg `0.3963` n `12`; crypto_alt avg `1.7273` n `229`; crypto_major avg `2.4832` n `8`; equity avg `0.3549` n `88`; fx avg `-0.0732` n `6`; index avg `0.2637` n `25`; metal avg `1.1962` n `20`; unknown avg `5.5004` n `737`

## Correlations

- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1245`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1234`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0757`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0731`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0698`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.068`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0613`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0608`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0598`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0585`, n `668`, weak_sample_signal
