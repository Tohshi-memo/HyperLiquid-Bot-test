# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-06T03:52:25.595227+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_index_leads_crypto: score `1.134` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.2329` n `12`; crypto_alt avg `-0.2047` n `228`; crypto_major avg `-0.1033` n `8`; equity avg `0.2171` n `74`; fx avg `0.0` n `6`; index avg `0.2188` n `23`; metal avg `-0.0759` n `18`; unknown avg `-0.3723` n `425`
- 1h: commodity avg `0.1262` n `12`; crypto_alt avg `-1.3563` n `228`; crypto_major avg `-1.0994` n `8`; equity avg `0.2233` n `74`; fx avg `-0.0188` n `6`; index avg `0.0346` n `23`; metal avg `-0.177` n `18`; unknown avg `-0.7184` n `425`
- 4h: commodity avg `0.5459` n `12`; crypto_alt avg `-1.4645` n `228`; crypto_major avg `-0.6338` n `8`; equity avg `-0.9651` n `74`; fx avg `-0.0436` n `6`; index avg `-0.4023` n `23`; metal avg `-0.3863` n `18`; unknown avg `-0.1461` n `425`
- 24h: commodity avg `-0.9897` n `12`; crypto_alt avg `-5.731` n `228`; crypto_major avg `-4.8772` n `8`; equity avg `-6.3268` n `74`; fx avg `-0.2294` n `6`; index avg `-3.9059` n `23`; metal avg `-4.0892` n `18`; unknown avg `-0.7995` n `404`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1236`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1199`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.092`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0892`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0868`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0843`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0745`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0736`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.073`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0664`, n `668`, weak_sample_signal
