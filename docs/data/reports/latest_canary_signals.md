# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-04T02:07:27.108721+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.01` n `12`; crypto_alt avg `0.0707` n `229`; crypto_major avg `0.0482` n `8`; equity avg `0.0504` n `88`; fx avg `-0.0015` n `6`; index avg `0.0106` n `25`; metal avg `0.0044` n `20`; unknown avg `-0.0063` n `763`
- 1h: commodity avg `-0.0453` n `12`; crypto_alt avg `-0.0018` n `229`; crypto_major avg `-0.1555` n `8`; equity avg `0.0651` n `88`; fx avg `-0.0242` n `6`; index avg `0.0156` n `25`; metal avg `-0.0042` n `20`; unknown avg `3.8578` n `763`
- 4h: commodity avg `-0.0212` n `12`; crypto_alt avg `-0.7298` n `229`; crypto_major avg `-0.4224` n `8`; equity avg `-0.0045` n `88`; fx avg `-0.0185` n `6`; index avg `-0.0396` n `25`; metal avg `-0.0297` n `20`; unknown avg `0.2131` n `763`
- 24h: commodity avg `0.0258` n `12`; crypto_alt avg `1.811` n `229`; crypto_major avg `2.2963` n `8`; equity avg `0.7077` n `88`; fx avg `-0.1209` n `6`; index avg `0.1375` n `25`; metal avg `-0.1412` n `20`; unknown avg `3.1692` n `737`

## Correlations

- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1077`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1063`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0847`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0846`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0822`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0808`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.073`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0674`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0616`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0607`, n `668`, weak_sample_signal
