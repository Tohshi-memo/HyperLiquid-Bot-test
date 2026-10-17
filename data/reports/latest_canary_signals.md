# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-17T18:22:26.001196+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0184` n `13`; crypto_alt avg `0.2035` n `236`; crypto_major avg `0.0771` n `8`; equity avg `-0.011` n `151`; fx avg `0.0` n `6`; index avg `0.0051` n `26`; metal avg `0.0098` n `20`; unknown avg `2.7448` n `1185`
- 1h: commodity avg `0.0509` n `13`; crypto_alt avg `0.5721` n `236`; crypto_major avg `0.3578` n `8`; equity avg `0.1054` n `151`; fx avg `-0.0121` n `6`; index avg `0.0066` n `26`; metal avg `0.0188` n `20`; unknown avg `-0.2021` n `1183`
- 4h: commodity avg `0.0758` n `13`; crypto_alt avg `-0.5299` n `236`; crypto_major avg `-0.2542` n `8`; equity avg `-0.2318` n `151`; fx avg `-0.031` n `6`; index avg `-0.0552` n `26`; metal avg `-0.0211` n `20`; unknown avg `1.5255` n `1127`
- 24h: commodity avg `0.0189` n `13`; crypto_alt avg `-1.1714` n `236`; crypto_major avg `-0.3238` n `8`; equity avg `-0.5234` n `151`; fx avg `-0.0216` n `6`; index avg `-0.0818` n `26`; metal avg `0.0147` n `20`; unknown avg `4.1833` n `1019`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1712`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1477`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1141`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1129`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0988`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0938`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0746`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0741`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0726`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0628`, n `668`, weak_sample_signal
