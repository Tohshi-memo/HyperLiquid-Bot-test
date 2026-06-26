# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-26T07:07:32.295281+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.8749` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.2359` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `2.0312` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0009` n `12`; crypto_alt avg `0.3099` n `228`; crypto_major avg `0.4465` n `8`; equity avg `-0.0285` n `86`; fx avg `-0.0035` n `6`; index avg `-0.0023` n `23`; metal avg `0.0147` n `20`; unknown avg `0.011` n `757`
- 1h: commodity avg `-0.0678` n `12`; crypto_alt avg `1.3376` n `228`; crypto_major avg `1.5234` n `8`; equity avg `0.6101` n `86`; fx avg `-0.0622` n `6`; index avg `0.1405` n `23`; metal avg `0.4941` n `20`; unknown avg `0.2786` n `749`
- 4h: commodity avg `0.076` n `12`; crypto_alt avg `2.6972` n `228`; crypto_major avg `2.9509` n `8`; equity avg `0.9197` n `86`; fx avg `-0.0676` n `6`; index avg `0.1881` n `23`; metal avg `0.715` n `20`; unknown avg `0.5223` n `717`
- 24h: commodity avg `0.2996` n `12`; crypto_alt avg `-1.5918` n `228`; crypto_major avg `-1.6084` n `8`; equity avg `-3.7921` n `86`; fx avg `0.0087` n `6`; index avg `-0.5503` n `23`; metal avg `0.6939` n `20`; unknown avg `0.595` n `693`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.2225`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1752`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.165`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1529`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1115`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1044`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1044`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1033`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0924`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0859`, n `668`, weak_sample_signal
