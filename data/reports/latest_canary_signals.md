# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-10T17:22:34.360705+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0128` n `12`; crypto_alt avg `0.1941` n `230`; crypto_major avg `0.1829` n `8`; equity avg `-0.0821` n `113`; fx avg `0.0006` n `6`; index avg `0.0176` n `25`; metal avg `0.0429` n `20`; unknown avg `-0.0068` n `785`
- 1h: commodity avg `0.0774` n `12`; crypto_alt avg `0.1762` n `230`; crypto_major avg `0.1662` n `8`; equity avg `-0.1481` n `113`; fx avg `0.0007` n `6`; index avg `-0.0118` n `25`; metal avg `-0.0453` n `20`; unknown avg `0.0508` n `785`
- 4h: commodity avg `0.4237` n `12`; crypto_alt avg `-0.5562` n `230`; crypto_major avg `-0.6825` n `8`; equity avg `-0.4332` n `113`; fx avg `0.0144` n `6`; index avg `0.0111` n `25`; metal avg `0.2248` n `20`; unknown avg `1.5052` n `784`
- 24h: commodity avg `1.208` n `12`; crypto_alt avg `-0.7139` n `230`; crypto_major avg `-1.4299` n `8`; equity avg `-1.3398` n `113`; fx avg `0.2429` n `6`; index avg `-0.0384` n `25`; metal avg `0.0171` n `20`; unknown avg `103.3863` n `752`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1734`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1628`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1551`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1444`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1444`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1443`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1242`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1234`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1167`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1147`, n `668`, weak_sample_signal
