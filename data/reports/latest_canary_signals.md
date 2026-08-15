# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-15T08:07:31.718324+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0099` n `12`; crypto_alt avg `0.0124` n `230`; crypto_major avg `0.0028` n `8`; equity avg `0.0061` n `114`; fx avg `0.0777` n `6`; index avg `-0.0021` n `25`; metal avg `0.0158` n `20`; unknown avg `2.607` n `791`
- 1h: commodity avg `-0.1521` n `12`; crypto_alt avg `-0.091` n `230`; crypto_major avg `-0.1036` n `8`; equity avg `0.0225` n `114`; fx avg `0.0749` n `6`; index avg `0.0039` n `25`; metal avg `0.0097` n `20`; unknown avg `2.6548` n `791`
- 4h: commodity avg `-0.1768` n `12`; crypto_alt avg `0.1847` n `230`; crypto_major avg `-0.1313` n `8`; equity avg `-0.0542` n `114`; fx avg `0.0715` n `6`; index avg `-0.02` n `25`; metal avg `0.0169` n `20`; unknown avg `2.6244` n `759`
- 24h: commodity avg `-0.302` n `12`; crypto_alt avg `1.0413` n `230`; crypto_major avg `0.0915` n `8`; equity avg `-0.377` n `114`; fx avg `0.2186` n `6`; index avg `-0.0957` n `25`; metal avg `0.2837` n `20`; unknown avg `2.6307` n `754`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2158`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1899`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1767`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1746`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1567`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.155`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1471`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1434`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1419`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.137`, n `668`, weak_sample_signal
