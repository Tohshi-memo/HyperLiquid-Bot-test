# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-24T22:07:31.545856+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `3.1501` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.5699` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0342` n `12`; crypto_alt avg `0.415` n `228`; crypto_major avg `0.2145` n `8`; equity avg `0.0393` n `86`; fx avg `-0.0199` n `6`; index avg `0.007` n `23`; metal avg `-0.0208` n `20`; unknown avg `0.743` n `764`
- 1h: commodity avg `-0.0421` n `12`; crypto_alt avg `0.9923` n `228`; crypto_major avg `0.758` n `8`; equity avg `0.1678` n `86`; fx avg `-0.0713` n `6`; index avg `0.0472` n `23`; metal avg `0.0317` n `20`; unknown avg `1.3034` n `764`
- 4h: commodity avg `-0.0946` n `12`; crypto_alt avg `3.3339` n `228`; crypto_major avg `3.0555` n `8`; equity avg `2.6854` n `86`; fx avg `-0.0687` n `6`; index avg `0.684` n `23`; metal avg `0.4856` n `20`; unknown avg `8.3528` n `764`
- 24h: commodity avg `-0.5534` n `12`; crypto_alt avg `-2.296` n `228`; crypto_major avg `-1.9447` n `8`; equity avg `4.2498` n `86`; fx avg `0.0052` n `6`; index avg `0.5652` n `23`; metal avg `-1.6334` n `20`; unknown avg `-0.6178` n `724`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1028`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0836`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0765`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0696`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0695`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0687`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0678`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0667`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0601`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0586`, n `668`, weak_sample_signal
