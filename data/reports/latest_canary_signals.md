# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-17T14:09:43.481831+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0406` n `12`; crypto_alt avg `0.7247` n `230`; crypto_major avg `0.7211` n `8`; equity avg `1.5149` n `96`; fx avg `0.0061` n `6`; index avg `0.2011` n `25`; metal avg `0.0912` n `20`; unknown avg `0.1351` n `769`
- 1h: commodity avg `0.0495` n `12`; crypto_alt avg `1.148` n `230`; crypto_major avg `1.0128` n `8`; equity avg `1.5436` n `96`; fx avg `0.0053` n `6`; index avg `0.1844` n `25`; metal avg `0.2035` n `20`; unknown avg `0.3757` n `769`
- 4h: commodity avg `0.3358` n `12`; crypto_alt avg `-0.0192` n `230`; crypto_major avg `-0.0309` n `8`; equity avg `0.7943` n `96`; fx avg `0.006` n `6`; index avg `0.1019` n `25`; metal avg `-0.0487` n `20`; unknown avg `0.2729` n `769`
- 24h: commodity avg `0.238` n `12`; crypto_alt avg `-1.7805` n `230`; crypto_major avg `-2.7766` n `8`; equity avg `-3.0378` n `94`; fx avg `-0.0568` n `6`; index avg `-0.5057` n `25`; metal avg `-0.4167` n `20`; unknown avg `-0.3193` n `736`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1353`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0942`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0935`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0839`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0799`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0784`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0777`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0747`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0729`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0703`, n `668`, weak_sample_signal
