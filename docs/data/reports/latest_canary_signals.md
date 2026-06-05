# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-05T19:22:22.827694+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-1.6944` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.027` n `12`; crypto_alt avg `0.2551` n `228`; crypto_major avg `0.1561` n `8`; equity avg `-0.4893` n `74`; fx avg `-0.01` n `6`; index avg `-0.2391` n `23`; metal avg `-0.0901` n `18`; unknown avg `0.1319` n `425`
- 1h: commodity avg `-0.0879` n `12`; crypto_alt avg `-2.0103` n `228`; crypto_major avg `-1.3666` n `8`; equity avg `-0.463` n `74`; fx avg `-0.0331` n `6`; index avg `-0.7051` n `23`; metal avg `-0.1842` n `18`; unknown avg `-0.5858` n `424`
- 4h: commodity avg `-0.6185` n `12`; crypto_alt avg `-2.823` n `228`; crypto_major avg `-2.5942` n `8`; equity avg `-2.748` n `74`; fx avg `-0.1107` n `6`; index avg `-2.3178` n `23`; metal avg `-0.8998` n `18`; unknown avg `-1.0263` n `424`
- 24h: commodity avg `-1.7143` n `12`; crypto_alt avg `-11.0231` n `228`; crypto_major avg `-8.9348` n `8`; equity avg `-7.2584` n `74`; fx avg `-0.0667` n `6`; index avg `-4.5762` n `23`; metal avg `-4.7086` n `18`; unknown avg `-2.7159` n `404`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1296`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1252`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0913`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0855`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0759`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0736`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0658`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.062`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0611`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.058`, n `668`, weak_sample_signal
