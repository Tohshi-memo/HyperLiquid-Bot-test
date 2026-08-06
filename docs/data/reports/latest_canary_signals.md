# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-06T05:22:35.172823+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0275` n `12`; crypto_alt avg `-0.0049` n `230`; crypto_major avg `0.0445` n `8`; equity avg `-0.0424` n `108`; fx avg `-0.0092` n `6`; index avg `-0.0352` n `25`; metal avg `-0.0508` n `20`; unknown avg `-0.0895` n `782`
- 1h: commodity avg `0.0142` n `12`; crypto_alt avg `0.1637` n `230`; crypto_major avg `0.3072` n `8`; equity avg `0.0639` n `108`; fx avg `-0.0046` n `6`; index avg `0.0008` n `25`; metal avg `-0.0558` n `20`; unknown avg `0.6703` n `782`
- 4h: commodity avg `-0.1802` n `12`; crypto_alt avg `0.1353` n `230`; crypto_major avg `0.1428` n `8`; equity avg `0.8299` n `108`; fx avg `0.0035` n `6`; index avg `0.0705` n `25`; metal avg `-0.1056` n `20`; unknown avg `0.4894` n `782`
- 24h: commodity avg `-0.1128` n `12`; crypto_alt avg `0.1089` n `230`; crypto_major avg `0.0374` n `8`; equity avg `-2.0505` n `108`; fx avg `-0.0487` n `6`; index avg `-0.3693` n `25`; metal avg `0.4362` n `20`; unknown avg `0.8893` n `749`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1788`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1621`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1326`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1278`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1048`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0843`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0831`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0768`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0759`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0712`, n `668`, weak_sample_signal
