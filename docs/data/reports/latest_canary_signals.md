# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-04T01:52:19.929788+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-3.9432` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `3.8723` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_equity_divergence: score `-3.2156` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_commodity_crypto_divergence: score `-3.1966` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 1h_index_leads_crypto: score `1.7217` - Index perps are stronger than crypto majors; possible risk-on canary.
- 1h_crypto_metal_divergence: score `-1.5824` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0179` n `12`; crypto_alt avg `-1.2239` n `228`; crypto_major avg `-1.0118` n `8`; equity avg `-0.491` n `73`; fx avg `0.0046` n `6`; index avg `-0.1538` n `23`; metal avg `-0.4813` n `18`; unknown avg `0.7721` n `420`
- 1h: commodity avg `-0.3368` n `12`; crypto_alt avg `-2.5331` n `228`; crypto_major avg `-1.7831` n `8`; equity avg `-0.5605` n `73`; fx avg `0.0242` n `6`; index avg `-0.0614` n `23`; metal avg `-0.2007` n `18`; unknown avg `0.5366` n `419`
- 4h: commodity avg `-0.7529` n `12`; crypto_alt avg `-4.7078` n `228`; crypto_major avg `-3.9495` n `8`; equity avg `-0.7339` n `73`; fx avg `-0.0121` n `6`; index avg `-0.0772` n `23`; metal avg `-0.0063` n `18`; unknown avg `0.156` n `419`
- 24h: commodity avg `-0.0667` n `12`; crypto_alt avg `-2.279` n `228`; crypto_major avg `-3.8584` n `8`; equity avg `-3.773` n `72`; fx avg `0.0327` n `6`; index avg `-1.0825` n `23`; metal avg `-1.8198` n `18`; unknown avg `1.1735` n `409`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1769`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1468`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1358`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1256`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0974`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.086`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0797`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0787`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0647`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.06`, n `668`, weak_sample_signal
