# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-24T23:07:29.918220+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.2731` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `1.9672` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0165` n `12`; crypto_alt avg `0.1111` n `228`; crypto_major avg `0.1162` n `8`; equity avg `0.0407` n `86`; fx avg `-0.0002` n `6`; index avg `0.0388` n `23`; metal avg `-0.0722` n `20`; unknown avg `-0.1485` n `748`
- 1h: commodity avg `0.0322` n `12`; crypto_alt avg `-0.3342` n `228`; crypto_major avg `-0.1511` n `8`; equity avg `0.125` n `86`; fx avg `0.0292` n `6`; index avg `0.0771` n `23`; metal avg `-0.0978` n `20`; unknown avg `-0.6243` n `748`
- 4h: commodity avg `0.0296` n `12`; crypto_alt avg `2.2266` n `228`; crypto_major avg `2.3027` n `8`; equity avg `3.1977` n `86`; fx avg `-0.0537` n `6`; index avg `0.8057` n `23`; metal avg `0.3355` n `20`; unknown avg `2.9042` n `748`
- 24h: commodity avg `-0.4902` n `12`; crypto_alt avg `-2.0689` n `228`; crypto_major avg `-1.7768` n `8`; equity avg `4.9243` n `86`; fx avg `0.0397` n `6`; index avg `0.7878` n `23`; metal avg `-1.5669` n `20`; unknown avg `-0.5383` n `716`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1046`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0853`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0734`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0708`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0703`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.07`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0653`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0635`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0618`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0574`, n `668`, weak_sample_signal
