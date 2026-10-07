# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-07T19:56:50.515837+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0048` n `13`; crypto_alt avg `0.0759` n `235`; crypto_major avg `-0.1258` n `8`; equity avg `0.0106` n `150`; fx avg `0.0027` n `6`; index avg `0.0165` n `26`; metal avg `-0.0091` n `20`; unknown avg `2.3625` n `1077`
- 1h: commodity avg `0.093` n `13`; crypto_alt avg `-0.0049` n `235`; crypto_major avg `-0.2241` n `8`; equity avg `-0.0685` n `150`; fx avg `0.0151` n `6`; index avg `-0.0069` n `26`; metal avg `-0.09` n `20`; unknown avg `18.8119` n `1075`
- 4h: commodity avg `-0.1678` n `13`; crypto_alt avg `0.3071` n `235`; crypto_major avg `-0.3149` n `8`; equity avg `0.0287` n `150`; fx avg `0.0154` n `6`; index avg `0.0304` n `26`; metal avg `-0.081` n `20`; unknown avg `13.7311` n `1068`
- 24h: commodity avg `0.3551` n `13`; crypto_alt avg `-4.2617` n `235`; crypto_major avg `-3.4805` n `8`; equity avg `-1.2872` n `150`; fx avg `-0.1605` n `6`; index avg `-0.1888` n `26`; metal avg `-0.7479` n `20`; unknown avg `25.7585` n `988`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1436`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1416`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1386`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1039`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0802`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0784`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.072`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0714`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0683`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0682`, n `668`, weak_sample_signal
