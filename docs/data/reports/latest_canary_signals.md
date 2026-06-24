# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-24T15:22:30.926809+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0684` n `12`; crypto_alt avg `0.2082` n `228`; crypto_major avg `0.2095` n `8`; equity avg `0.0426` n `86`; fx avg `0.0206` n `6`; index avg `0.0035` n `23`; metal avg `0.1257` n `20`; unknown avg `0.1282` n `764`
- 1h: commodity avg `0.0006` n `12`; crypto_alt avg `0.1292` n `228`; crypto_major avg `0.0159` n `8`; equity avg `0.6731` n `86`; fx avg `0.0237` n `6`; index avg `0.0787` n `23`; metal avg `-0.1077` n `20`; unknown avg `-0.0564` n `764`
- 4h: commodity avg `-0.329` n `12`; crypto_alt avg `-0.6068` n `228`; crypto_major avg `-0.9602` n `8`; equity avg `-0.9002` n `86`; fx avg `-0.0201` n `6`; index avg `0.0157` n `23`; metal avg `-0.4856` n `20`; unknown avg `0.1136` n `764`
- 24h: commodity avg `-0.6361` n `12`; crypto_alt avg `-1.3025` n `228`; crypto_major avg `-1.2331` n `8`; equity avg `3.0139` n `86`; fx avg `0.0376` n `6`; index avg `0.1051` n `23`; metal avg `-1.4668` n `20`; unknown avg `-0.4141` n `716`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1195`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1054`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0974`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0854`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0809`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0808`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.074`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0734`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0708`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0681`, n `668`, weak_sample_signal
