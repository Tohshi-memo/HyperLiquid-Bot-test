# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-17T08:22:30.473818+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0099` n `12`; crypto_alt avg `-0.1156` n `230`; crypto_major avg `-0.1096` n `8`; equity avg `-0.582` n `96`; fx avg `0.0021` n `6`; index avg `-0.1017` n `25`; metal avg `-0.1115` n `20`; unknown avg `-0.0358` n `768`
- 1h: commodity avg `-0.0547` n `12`; crypto_alt avg `-0.1474` n `230`; crypto_major avg `-0.0761` n `8`; equity avg `-0.5905` n `96`; fx avg `0.0266` n `6`; index avg `-0.0903` n `25`; metal avg `-0.0134` n `20`; unknown avg `0.097` n `768`
- 4h: commodity avg `-0.128` n `12`; crypto_alt avg `-0.6953` n `230`; crypto_major avg `-0.7451` n `8`; equity avg `-1.1518` n `96`; fx avg `0.0202` n `6`; index avg `-0.1585` n `25`; metal avg `-0.0994` n `20`; unknown avg `-0.144` n `736`
- 24h: commodity avg `-0.1379` n `12`; crypto_alt avg `-1.6053` n `230`; crypto_major avg `-2.7504` n `8`; equity avg `-5.6817` n `94`; fx avg `-0.0348` n `6`; index avg `-0.7712` n `25`; metal avg `-0.8132` n `20`; unknown avg `-0.4635` n `730`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.135`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0985`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0947`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0865`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0811`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0799`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0765`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0745`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0743`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0712`, n `668`, weak_sample_signal
