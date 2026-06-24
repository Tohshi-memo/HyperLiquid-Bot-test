# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-24T22:22:27.455507+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.15` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `1.691` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0083` n `12`; crypto_alt avg `-0.0637` n `228`; crypto_major avg `-0.0669` n `8`; equity avg `0.1469` n `86`; fx avg `0.0313` n `6`; index avg `0.0177` n `23`; metal avg `-0.018` n `20`; unknown avg `-0.1304` n `764`
- 1h: commodity avg `-0.0396` n `12`; crypto_alt avg `0.7876` n `228`; crypto_major avg `0.5386` n `8`; equity avg `0.5088` n `86`; fx avg `-0.0371` n `6`; index avg `0.0699` n `23`; metal avg `0.0028` n `20`; unknown avg `10.1658` n `764`
- 4h: commodity avg `-0.1122` n `12`; crypto_alt avg `2.2493` n `228`; crypto_major avg `2.0378` n `8`; equity avg `2.3928` n `86`; fx avg `-0.0347` n `6`; index avg `0.6434` n `23`; metal avg `0.3468` n `20`; unknown avg `1.684` n `764`
- 24h: commodity avg `-0.546` n `12`; crypto_alt avg `-2.3184` n `228`; crypto_major avg `-1.8838` n `8`; equity avg `4.4139` n `86`; fx avg `0.0391` n `6`; index avg `0.5912` n `23`; metal avg `-1.5792` n `20`; unknown avg `-0.3862` n `724`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1028`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0839`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0751`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0696`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0691`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0686`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0682`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0668`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0602`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0582`, n `668`, weak_sample_signal
