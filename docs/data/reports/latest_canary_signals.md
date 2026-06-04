# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-04T14:52:28.023453+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.7648` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.1624` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.1039` n `12`; crypto_alt avg `0.2125` n `228`; crypto_major avg `0.0865` n `8`; equity avg `-0.07` n `74`; fx avg `-0.0048` n `6`; index avg `-0.0496` n `23`; metal avg `-0.268` n `18`; unknown avg `-0.0463` n `424`
- 1h: commodity avg `-0.108` n `12`; crypto_alt avg `-0.0367` n `228`; crypto_major avg `-0.0248` n `8`; equity avg `0.1082` n `74`; fx avg `-0.0013` n `6`; index avg `0.0763` n `23`; metal avg `-0.7647` n `18`; unknown avg `0.9708` n `424`
- 4h: commodity avg `-0.5012` n `12`; crypto_alt avg `2.3822` n `228`; crypto_major avg `2.2636` n `8`; equity avg `1.3703` n `73`; fx avg `-0.0012` n `6`; index avg `0.3566` n `23`; metal avg `0.1012` n `18`; unknown avg `1.9205` n `422`
- 24h: commodity avg `-0.5537` n `12`; crypto_alt avg `-6.6394` n `228`; crypto_major avg `-4.6846` n `8`; equity avg `-2.4823` n `73`; fx avg `0.1042` n `6`; index avg `-0.9134` n `23`; metal avg `-0.306` n `18`; unknown avg `-0.1411` n `401`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1518`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1477`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1424`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1401`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1331`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1231`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.109`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1054`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.079`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0783`, n `668`, weak_sample_signal
