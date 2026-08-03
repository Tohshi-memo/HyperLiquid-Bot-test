# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-03T08:37:29.675349+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0374` n `12`; crypto_alt avg `0.0762` n `230`; crypto_major avg `-0.0046` n `8`; equity avg `0.0254` n `102`; fx avg `-0.0003` n `6`; index avg `0.0199` n `25`; metal avg `0.0089` n `20`; unknown avg `-0.0068` n `784`
- 1h: commodity avg `0.0836` n `12`; crypto_alt avg `-0.177` n `230`; crypto_major avg `-0.3133` n `8`; equity avg `-0.5739` n `102`; fx avg `0.012` n `6`; index avg `-0.0549` n `25`; metal avg `0.0042` n `20`; unknown avg `-0.115` n `784`
- 4h: commodity avg `0.1398` n `12`; crypto_alt avg `-0.4621` n `230`; crypto_major avg `-0.8081` n `8`; equity avg `-0.996` n `102`; fx avg `0.0179` n `6`; index avg `-0.1112` n `25`; metal avg `-0.0909` n `20`; unknown avg `-0.0216` n `768`
- 24h: commodity avg `-0.0341` n `12`; crypto_alt avg `-1.2426` n `230`; crypto_major avg `-0.9916` n `8`; equity avg `-0.2889` n `102`; fx avg `-0.1789` n `6`; index avg `-0.0985` n `25`; metal avg `-0.1008` n `20`; unknown avg `0.9675` n `766`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1041`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.091`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0818`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0747`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0725`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0708`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0675`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.064`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0629`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0609`, n `668`, weak_sample_signal
