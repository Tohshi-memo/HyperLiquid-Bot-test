# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-22T13:52:30.238813+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.0779` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `1.5796` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0677` n `12`; crypto_alt avg `0.1459` n `228`; crypto_major avg `0.0344` n `8`; equity avg `0.2557` n `79`; fx avg `-0.008` n `6`; index avg `-0.0122` n `23`; metal avg `0.1035` n `20`; unknown avg `0.3025` n `722`
- 1h: commodity avg `-0.196` n `12`; crypto_alt avg `0.2719` n `228`; crypto_major avg `0.4706` n `8`; equity avg `0.5536` n `79`; fx avg `-0.0379` n `6`; index avg `0.0391` n `23`; metal avg `0.1604` n `20`; unknown avg `0.1864` n `722`
- 4h: commodity avg `-0.4366` n `12`; crypto_alt avg `1.5319` n `228`; crypto_major avg `1.6413` n `8`; equity avg `0.9097` n `79`; fx avg `-0.007` n `6`; index avg `0.1505` n `23`; metal avg `0.0617` n `18`; unknown avg `1.305` n `701`
- 24h: commodity avg `-0.7007` n `12`; crypto_alt avg `1.13` n `228`; crypto_major avg `1.7983` n `8`; equity avg `0.8354` n `79`; fx avg `0.0188` n `6`; index avg `0.1798` n `23`; metal avg `0.6225` n `18`; unknown avg `1.0012` n `637`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0896`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0853`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0826`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0823`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0803`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0757`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0744`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.066`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0637`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0597`, n `668`, weak_sample_signal
