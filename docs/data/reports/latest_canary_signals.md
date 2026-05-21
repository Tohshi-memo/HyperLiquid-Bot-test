# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-21T10:52:18.908975+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.35` - Polymarket crypto volume is unusually high.
- 1h_commodity_crypto_divergence: score `-2.0846` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `0.502` n `12`; crypto_alt avg `-0.3679` n `228`; crypto_major avg `-0.3521` n `8`; equity avg `-0.3922` n `66`; fx avg `0.0004` n `6`; index avg `-0.2568` n `23`; metal avg `-0.2311` n `18`; unknown avg `-0.1786` n `386`
- 1h: commodity avg `1.4098` n `12`; crypto_alt avg `-0.8051` n `228`; crypto_major avg `-0.6748` n `8`; equity avg `-0.7544` n `66`; fx avg `-0.0017` n `6`; index avg `-0.4808` n `23`; metal avg `-0.66` n `18`; unknown avg `0.8605` n `386`
- 4h: commodity avg `0.5364` n `12`; crypto_alt avg `-0.5428` n `228`; crypto_major avg `-0.0634` n `8`; equity avg `-0.3457` n `66`; fx avg `0.0108` n `6`; index avg `-0.2878` n `23`; metal avg `-0.1387` n `18`; unknown avg `1.6462` n `385`
- 24h: commodity avg `-0.6129` n `12`; crypto_alt avg `1.4879` n `228`; crypto_major avg `2.1052` n `8`; equity avg `0.8709` n `66`; fx avg `0.1112` n `6`; index avg `0.8383` n `23`; metal avg `-0.4011` n `18`; unknown avg `7.0759` n `374`

## Correlations

- risk_on_score -> equity_forward_1h_return_pct: corr `0.0753`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0726`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0648`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0644`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0599`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0575`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0568`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.054`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0521`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0513`, n `668`, weak_sample_signal
