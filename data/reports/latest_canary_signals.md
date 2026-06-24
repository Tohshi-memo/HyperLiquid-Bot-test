# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-24T22:37:27.318751+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.315` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `1.8556` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0081` n `12`; crypto_alt avg `-0.1395` n `228`; crypto_major avg `-0.0162` n `8`; equity avg `0.0212` n `86`; fx avg `0.0005` n `6`; index avg `0.0127` n `23`; metal avg `0.0884` n `20`; unknown avg `-0.0042` n `764`
- 1h: commodity avg `-0.0404` n `12`; crypto_alt avg `0.3029` n `228`; crypto_major avg `0.1181` n `8`; equity avg `0.3397` n `86`; fx avg `-0.0198` n `6`; index avg `0.0433` n `23`; metal avg `0.0701` n `20`; unknown avg `0.7344` n `764`
- 4h: commodity avg `-0.0744` n `12`; crypto_alt avg `2.1712` n `228`; crypto_major avg `2.2406` n `8`; equity avg `2.561` n `86`; fx avg `-0.0499` n `6`; index avg `0.6656` n `23`; metal avg `0.385` n `20`; unknown avg `3.7443` n `764`
- 24h: commodity avg `-0.5582` n `12`; crypto_alt avg `-2.1927` n `228`; crypto_major avg `-1.7539` n `8`; equity avg `4.6363` n `86`; fx avg `0.0449` n `6`; index avg `0.6573` n `23`; metal avg `-1.4686` n `20`; unknown avg `0.1618` n `724`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1029`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0842`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0747`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0697`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.069`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0686`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0678`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0659`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0605`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0581`, n `668`, weak_sample_signal
