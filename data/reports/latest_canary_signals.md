# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-08T11:07:43.044091+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0515` n `12`; crypto_alt avg `0.048` n `229`; crypto_major avg `-0.0102` n `8`; equity avg `-0.0746` n `91`; fx avg `0.0182` n `6`; index avg `-0.0141` n `25`; metal avg `-0.0633` n `20`; unknown avg `-0.0004` n `763`
- 1h: commodity avg `-0.1735` n `12`; crypto_alt avg `0.3624` n `229`; crypto_major avg `0.3224` n `8`; equity avg `0.5071` n `91`; fx avg `0.0095` n `6`; index avg `0.1023` n `25`; metal avg `-0.0193` n `20`; unknown avg `0.0736` n `763`
- 4h: commodity avg `0.4102` n `12`; crypto_alt avg `-0.8741` n `229`; crypto_major avg `-0.5641` n `8`; equity avg `-1.2301` n `91`; fx avg `0.0378` n `6`; index avg `-0.2964` n `25`; metal avg `-1.0847` n `20`; unknown avg `-0.2443` n `763`
- 24h: commodity avg `1.1238` n `12`; crypto_alt avg `-3.7899` n `229`; crypto_major avg `-2.8546` n `8`; equity avg `-2.7721` n `91`; fx avg `-0.0845` n `6`; index avg `-0.5915` n `25`; metal avg `-1.2576` n `20`; unknown avg `-0.7748` n `733`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1369`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0993`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0987`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0972`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0967`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0934`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0908`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0758`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0715`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0707`, n `668`, weak_sample_signal
