# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-28T05:07:19.046329+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.3366` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `-0.0111` n `12`; crypto_alt avg `-0.0267` n `228`; crypto_major avg `0.0139` n `8`; equity avg `-0.0421` n `67`; fx avg `-0.0038` n `6`; index avg `0.0209` n `23`; metal avg `-0.0103` n `18`; unknown avg `-0.2363` n `419`
- 1h: commodity avg `-0.0412` n `12`; crypto_alt avg `-0.1595` n `228`; crypto_major avg `0.1598` n `8`; equity avg `0.0454` n `67`; fx avg `-0.0112` n `6`; index avg `-0.1018` n `23`; metal avg `-0.3549` n `18`; unknown avg `1.3699` n `419`
- 4h: commodity avg `0.6476` n `12`; crypto_alt avg `-2.8709` n `228`; crypto_major avg `-1.689` n `8`; equity avg `-1.8743` n `67`; fx avg `-0.1008` n `6`; index avg `-0.805` n `23`; metal avg `-1.8076` n `18`; unknown avg `-0.2468` n `419`
- 24h: commodity avg `0.2607` n `12`; crypto_alt avg `-4.3757` n `228`; crypto_major avg `-3.3119` n `8`; equity avg `-2.1891` n `67`; fx avg `-0.1216` n `6`; index avg `-1.3507` n `23`; metal avg `-3.1836` n `18`; unknown avg `-1.4751` n `400`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1875`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1764`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1735`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1732`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1714`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1653`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1599`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.159`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1488`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1481`, n `668`, weak_sample_signal
