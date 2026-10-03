# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-03T17:52:24.861462+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0738` n `13`; crypto_alt avg `-0.0548` n `235`; crypto_major avg `0.0761` n `8`; equity avg `0.0022` n `143`; fx avg `-0.0025` n `6`; index avg `0.007` n `26`; metal avg `0.0004` n `20`; unknown avg `-0.0248` n `1078`
- 1h: commodity avg `-0.1211` n `13`; crypto_alt avg `0.188` n `235`; crypto_major avg `0.3084` n `8`; equity avg `0.0317` n `143`; fx avg `-0.0093` n `6`; index avg `0.0096` n `26`; metal avg `-0.0055` n `20`; unknown avg `-0.0374` n `1076`
- 4h: commodity avg `0.0117` n `13`; crypto_alt avg `0.7284` n `235`; crypto_major avg `0.6028` n `8`; equity avg `0.0942` n `143`; fx avg `-0.0112` n `6`; index avg `0.0237` n `26`; metal avg `-0.0043` n `20`; unknown avg `-0.2528` n `964`
- 24h: commodity avg `0.2127` n `13`; crypto_alt avg `0.1564` n `235`; crypto_major avg `0.1009` n `8`; equity avg `0.1377` n `143`; fx avg `-0.0501` n `6`; index avg `0.0575` n `26`; metal avg `0.0817` n `20`; unknown avg `0.0502` n `868`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1982`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1868`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1674`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1582`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1211`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1182`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1172`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.111`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1063`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.084`, n `668`, weak_sample_signal
