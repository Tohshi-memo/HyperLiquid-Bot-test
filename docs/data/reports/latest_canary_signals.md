# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-03T20:37:24.716500+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0337` n `12`; crypto_alt avg `-0.0253` n `230`; crypto_major avg `-0.0277` n `8`; equity avg `-0.0253` n `103`; fx avg `0.0092` n `6`; index avg `0.0135` n `25`; metal avg `0.0532` n `20`; unknown avg `-0.0618` n `784`
- 1h: commodity avg `-0.0759` n `12`; crypto_alt avg `-0.0128` n `230`; crypto_major avg `0.1309` n `8`; equity avg `0.1246` n `103`; fx avg `0.0252` n `6`; index avg `0.0483` n `25`; metal avg `0.0539` n `20`; unknown avg `-0.0241` n `784`
- 4h: commodity avg `-0.0178` n `12`; crypto_alt avg `0.309` n `230`; crypto_major avg `0.1607` n `8`; equity avg `0.8269` n `103`; fx avg `0.0103` n `6`; index avg `0.1681` n `25`; metal avg `0.1624` n `20`; unknown avg `-0.2263` n `784`
- 24h: commodity avg `-0.1715` n `12`; crypto_alt avg `0.467` n `230`; crypto_major avg `0.7141` n `8`; equity avg `1.9566` n `103`; fx avg `-0.2492` n `6`; index avg `0.104` n `25`; metal avg `-0.3616` n `20`; unknown avg `0.0492` n `766`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1222`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0968`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0941`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0886`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0837`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0812`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0795`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0794`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.078`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0773`, n `668`, weak_sample_signal
