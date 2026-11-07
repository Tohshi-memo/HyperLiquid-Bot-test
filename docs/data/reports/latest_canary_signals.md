# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-07T01:52:26.821826+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0247` n `13`; crypto_alt avg `0.0586` n `239`; crypto_major avg `0.0701` n `8`; equity avg `0.2341` n `158`; fx avg `-0.0005` n `6`; index avg `0.0052` n `27`; metal avg `0.0013` n `20`; unknown avg `-0.1335` n `1261`
- 1h: commodity avg `-0.0486` n `13`; crypto_alt avg `0.0444` n `239`; crypto_major avg `0.1936` n `8`; equity avg `0.1695` n `158`; fx avg `0.0064` n `6`; index avg `0.0142` n `27`; metal avg `0.0149` n `20`; unknown avg `6.5627` n `1255`
- 4h: commodity avg `-0.0378` n `13`; crypto_alt avg `-0.0732` n `239`; crypto_major avg `0.346` n `8`; equity avg `0.0968` n `158`; fx avg `-0.0045` n `6`; index avg `0.0134` n `27`; metal avg `0.0353` n `20`; unknown avg `1.2039` n `1227`
- 24h: commodity avg `-0.0324` n `13`; crypto_alt avg `1.0539` n `239`; crypto_major avg `-0.0483` n `8`; equity avg `1.6234` n `158`; fx avg `-0.0744` n `6`; index avg `0.2307` n `27`; metal avg `0.06` n `20`; unknown avg `8.2621` n `1022`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2134`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1657`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1584`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1402`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1177`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1139`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1111`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1108`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1024`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0999`, n `668`, weak_sample_signal
