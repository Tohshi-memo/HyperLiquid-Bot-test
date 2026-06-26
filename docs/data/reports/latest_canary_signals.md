# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-26T06:37:31.385630+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.0214` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_equity_divergence: score `1.7699` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_crypto_metal_divergence: score `1.5344` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0231` n `12`; crypto_alt avg `0.0729` n `228`; crypto_major avg `0.0968` n `8`; equity avg `0.1965` n `86`; fx avg `0.0159` n `6`; index avg `0.0598` n `23`; metal avg `0.0409` n `20`; unknown avg `0.0039` n `765`
- 1h: commodity avg `0.0519` n `12`; crypto_alt avg `0.156` n `228`; crypto_major avg `0.4193` n `8`; equity avg `0.107` n `86`; fx avg `-0.0652` n `6`; index avg `0.0275` n `23`; metal avg `0.2263` n `20`; unknown avg `-0.1122` n `741`
- 4h: commodity avg `0.0481` n `12`; crypto_alt avg `1.624` n `228`; crypto_major avg `2.0695` n `8`; equity avg `0.2996` n `86`; fx avg `-0.0832` n `6`; index avg `0.0552` n `23`; metal avg `0.5351` n `20`; unknown avg `0.0311` n `725`
- 24h: commodity avg `0.3999` n `12`; crypto_alt avg `-2.3138` n `228`; crypto_major avg `-2.2053` n `8`; equity avg `-3.8142` n `86`; fx avg `-0.0159` n `6`; index avg `-0.5695` n `23`; metal avg `0.5844` n `20`; unknown avg `0.7277` n `693`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.2176`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1732`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1685`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1486`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1041`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1031`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0992`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0992`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0966`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0845`, n `668`, weak_sample_signal
