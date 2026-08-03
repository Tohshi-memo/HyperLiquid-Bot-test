# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-03T10:52:25.562110+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0676` n `12`; crypto_alt avg `-0.0985` n `230`; crypto_major avg `-0.0334` n `8`; equity avg `-0.0661` n `102`; fx avg `0.0053` n `6`; index avg `0.0069` n `25`; metal avg `-0.0339` n `20`; unknown avg `-0.0186` n `785`
- 1h: commodity avg `-0.1325` n `12`; crypto_alt avg `-0.1901` n `230`; crypto_major avg `-0.0653` n `8`; equity avg `-0.48` n `102`; fx avg `-0.0222` n `6`; index avg `-0.0326` n `25`; metal avg `-0.1033` n `20`; unknown avg `-0.0449` n `784`
- 4h: commodity avg `0.0899` n `12`; crypto_alt avg `-0.0108` n `230`; crypto_major avg `0.0653` n `8`; equity avg `-1.2058` n `102`; fx avg `-0.0308` n `6`; index avg `-0.1248` n `25`; metal avg `-0.1971` n `20`; unknown avg `-0.0391` n `784`
- 24h: commodity avg `-0.3999` n `12`; crypto_alt avg `-0.8326` n `230`; crypto_major avg `-0.2835` n `8`; equity avg `-0.7552` n `102`; fx avg `-0.1636` n `6`; index avg `-0.1438` n `25`; metal avg `-0.2368` n `20`; unknown avg `1.0335` n `766`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1096`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0961`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.079`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0754`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0744`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0703`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0673`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0665`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0625`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0625`, n `668`, weak_sample_signal
