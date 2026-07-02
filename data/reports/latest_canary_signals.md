# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-02T22:36:07.160912+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0073` n `12`; crypto_alt avg `0.0613` n `229`; crypto_major avg `0.1341` n `8`; equity avg `0.0514` n `88`; fx avg `-0.0052` n `6`; index avg `0.0014` n `25`; metal avg `0.0161` n `20`; unknown avg `-0.1038` n `765`
- 1h: commodity avg `-0.0081` n `12`; crypto_alt avg `-0.1758` n `229`; crypto_major avg `-0.1416` n `8`; equity avg `0.0823` n `88`; fx avg `-0.0116` n `6`; index avg `0.0154` n `25`; metal avg `0.0187` n `20`; unknown avg `3.3371` n `765`
- 4h: commodity avg `0.0042` n `12`; crypto_alt avg `-0.2086` n `229`; crypto_major avg `-0.5807` n `8`; equity avg `0.4722` n `88`; fx avg `-0.0027` n `6`; index avg `0.1294` n `25`; metal avg `0.0062` n `20`; unknown avg `3.2466` n `765`
- 24h: commodity avg `0.1206` n `12`; crypto_alt avg `1.2633` n `228`; crypto_major avg `2.1739` n `8`; equity avg `-2.3809` n `88`; fx avg `-0.1491` n `6`; index avg `-0.4519` n `25`; metal avg `0.9262` n `20`; unknown avg `3.7272` n `739`

## Correlations

- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0897`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0894`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0843`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.076`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0674`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0659`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0627`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.061`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0607`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0593`, n `668`, weak_sample_signal
