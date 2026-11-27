# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-27T19:52:38.688598+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0651` n `13`; crypto_alt avg `-0.1952` n `239`; crypto_major avg `-0.2524` n `8`; equity avg `-0.0652` n `168`; fx avg `0.0009` n `6`; index avg `-0.0133` n `27`; metal avg `0.1043` n `20`; unknown avg `5.047` n `1265`
- 1h: commodity avg `0.0954` n `13`; crypto_alt avg `0.1097` n `239`; crypto_major avg `0.1273` n `8`; equity avg `0.0578` n `168`; fx avg `0.0064` n `6`; index avg `0.0003` n `27`; metal avg `0.1243` n `20`; unknown avg `160.2192` n `1259`
- 4h: commodity avg `-0.1174` n `13`; crypto_alt avg `0.3309` n `239`; crypto_major avg `-0.0086` n `8`; equity avg `0.828` n `168`; fx avg `-0.0282` n `6`; index avg `0.083` n `27`; metal avg `0.1891` n `20`; unknown avg `167.5558` n `1228`
- 24h: commodity avg `-0.5163` n `13`; crypto_alt avg `-0.0868` n `239`; crypto_major avg `0.1142` n `8`; equity avg `3.2002` n `168`; fx avg `-0.1518` n `6`; index avg `0.3086` n `27`; metal avg `0.9199` n `20`; unknown avg `265.1375` n `1043`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1291`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1254`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.1022`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0974`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0928`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0834`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0817`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0814`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0668`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0649`, n `668`, weak_sample_signal
