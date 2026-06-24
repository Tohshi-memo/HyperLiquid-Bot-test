# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-24T23:52:26.064873+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.2735` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `1.9006` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0048` n `12`; crypto_alt avg `-0.1325` n `228`; crypto_major avg `-0.1726` n `8`; equity avg `-0.0224` n `86`; fx avg `-0.0002` n `6`; index avg `-0.0353` n `23`; metal avg `-0.0214` n `20`; unknown avg `-0.2019` n `764`
- 1h: commodity avg `0.0366` n `12`; crypto_alt avg `0.188` n `228`; crypto_major avg `0.2245` n `8`; equity avg `0.3602` n `86`; fx avg `0.0206` n `6`; index avg `-0.0213` n `23`; metal avg `0.0757` n `20`; unknown avg `-0.6475` n `748`
- 4h: commodity avg `-0.0062` n `12`; crypto_alt avg `2.0928` n `228`; crypto_major avg `2.2673` n `8`; equity avg `2.9661` n `86`; fx avg `-0.0164` n `6`; index avg `0.6037` n `23`; metal avg `0.3667` n `20`; unknown avg `2.6205` n `748`
- 24h: commodity avg `-0.4249` n `12`; crypto_alt avg `-2.1757` n `228`; crypto_major avg `-1.9288` n `8`; equity avg `5.384` n `86`; fx avg `0.0288` n `6`; index avg `0.5909` n `23`; metal avg `-1.4634` n `20`; unknown avg `-1.3674` n `716`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1067`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0869`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.074`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0731`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0712`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0712`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.068`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0644`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0639`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0636`, n `668`, weak_sample_signal
