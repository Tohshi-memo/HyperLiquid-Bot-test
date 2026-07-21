# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-21T10:37:37.231819+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0344` n `12`; crypto_alt avg `-0.0014` n `230`; crypto_major avg `0.0001` n `8`; equity avg `0.0378` n `98`; fx avg `0.007` n `6`; index avg `0.0048` n `25`; metal avg `0.017` n `20`; unknown avg `-0.007` n `771`
- 1h: commodity avg `-0.048` n `12`; crypto_alt avg `0.0767` n `230`; crypto_major avg `-0.0513` n `8`; equity avg `0.001` n `98`; fx avg `0.0075` n `6`; index avg `0.0299` n `25`; metal avg `0.0627` n `20`; unknown avg `-0.0161` n `771`
- 4h: commodity avg `0.1791` n `12`; crypto_alt avg `-0.124` n `230`; crypto_major avg `0.0755` n `8`; equity avg `0.5295` n `98`; fx avg `0.0324` n `6`; index avg `0.0613` n `25`; metal avg `0.1164` n `20`; unknown avg `-0.0229` n `771`
- 24h: commodity avg `0.3141` n `12`; crypto_alt avg `2.2034` n `230`; crypto_major avg `2.639` n `8`; equity avg `1.6248` n `98`; fx avg `-0.0898` n `6`; index avg `0.2755` n `25`; metal avg `0.6741` n `20`; unknown avg `0.1424` n `754`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1472`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1249`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0933`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0838`, n `666`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0768`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0705`, n `666`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0691`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0689`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0668`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0659`, n `666`, weak_sample_signal
