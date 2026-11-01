# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-01T22:22:44.593507+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0096` n `13`; crypto_alt avg `-0.3194` n `238`; crypto_major avg `-0.4208` n `8`; equity avg `-0.091` n `156`; fx avg `0.0039` n `6`; index avg `0.0106` n `27`; metal avg `-0.0159` n `20`; unknown avg `0.7235` n `1255`
- 1h: commodity avg `0.0083` n `13`; crypto_alt avg `-0.2182` n `238`; crypto_major avg `-0.4137` n `8`; equity avg `-0.0856` n `156`; fx avg `0.0216` n `6`; index avg `-0.0268` n `27`; metal avg `-0.0138` n `20`; unknown avg `-0.1974` n `1247`
- 4h: commodity avg `0.0686` n `13`; crypto_alt avg `-0.5792` n `238`; crypto_major avg `-0.5573` n `8`; equity avg `-0.0832` n `156`; fx avg `-0.013` n `6`; index avg `-0.0338` n `27`; metal avg `-0.0397` n `20`; unknown avg `12.5705` n `1205`
- 24h: commodity avg `0.009` n `13`; crypto_alt avg `-1.0131` n `238`; crypto_major avg `-0.7447` n `8`; equity avg `0.1932` n `156`; fx avg `-0.0045` n `6`; index avg `0.048` n `27`; metal avg `0.0118` n `20`; unknown avg `3.488` n `1096`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `0.1535`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1525`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1495`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1442`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1424`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.133`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1015`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0883`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0845`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0831`, n `668`, weak_sample_signal
