# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-02T01:22:26.328444+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0584` n `12`; crypto_alt avg `0.2418` n `228`; crypto_major avg `0.2655` n `8`; equity avg `0.2209` n `88`; fx avg `-0.0004` n `6`; index avg `0.0642` n `25`; metal avg `-0.0004` n `20`; unknown avg `0.1392` n `763`
- 1h: commodity avg `-0.0953` n `12`; crypto_alt avg `0.4053` n `228`; crypto_major avg `0.1445` n `8`; equity avg `0.4839` n `88`; fx avg `0.0061` n `6`; index avg `0.1276` n `25`; metal avg `0.1809` n `20`; unknown avg `-0.173` n `763`
- 4h: commodity avg `-0.1628` n `12`; crypto_alt avg `-0.3298` n `228`; crypto_major avg `-0.8028` n `8`; equity avg `-0.0186` n `88`; fx avg `0.0041` n `6`; index avg `-0.0223` n `25`; metal avg `0.3017` n `20`; unknown avg `27.0476` n `763`
- 24h: commodity avg `-0.6842` n `12`; crypto_alt avg `2.5761` n `228`; crypto_major avg `1.5196` n `8`; equity avg `-1.073` n `88`; fx avg `-0.0245` n `6`; index avg `-0.3737` n `25`; metal avg `0.7366` n `20`; unknown avg `25.2546` n `739`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.132`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1063`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1049`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0995`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0984`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0926`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.088`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0817`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.073`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0683`, n `668`, weak_sample_signal
