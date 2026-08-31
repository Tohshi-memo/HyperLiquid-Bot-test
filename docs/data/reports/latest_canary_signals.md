# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-31T18:22:32.113219+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0511` n `12`; crypto_alt avg `0.1394` n `232`; crypto_major avg `0.0863` n `8`; equity avg `-0.0263` n `129`; fx avg `-0.0008` n `6`; index avg `0.0014` n `26`; metal avg `0.007` n `20`; unknown avg `-0.0004` n `793`
- 1h: commodity avg `-0.0308` n `12`; crypto_alt avg `0.2823` n `232`; crypto_major avg `0.2243` n `8`; equity avg `0.0398` n `129`; fx avg `0.0089` n `6`; index avg `0.0216` n `26`; metal avg `-0.0062` n `20`; unknown avg `-0.5189` n `791`
- 4h: commodity avg `0.1182` n `12`; crypto_alt avg `1.0602` n `232`; crypto_major avg `1.3945` n `8`; equity avg `0.2436` n `129`; fx avg `0.016` n `6`; index avg `-0.0251` n `26`; metal avg `0.0083` n `20`; unknown avg `0.1349` n `791`
- 24h: commodity avg `0.5616` n `12`; crypto_alt avg `-0.9389` n `231`; crypto_major avg `-1.1659` n `8`; equity avg `-0.4288` n `129`; fx avg `-0.0934` n `6`; index avg `-0.2244` n `26`; metal avg `-0.5609` n `20`; unknown avg `0.1501` n `758`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1004`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1002`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0926`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0868`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0755`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0584`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0555`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0552`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0519`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0501`, n `668`, weak_sample_signal
