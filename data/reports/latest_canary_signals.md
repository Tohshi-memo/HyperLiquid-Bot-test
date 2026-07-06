# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-06T18:07:31.577572+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `2.2765` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_commodity_crypto_divergence: score `2.0197` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `1.8721` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0234` n `12`; crypto_alt avg `-0.0012` n `229`; crypto_major avg `0.0241` n `8`; equity avg `-0.0174` n `91`; fx avg `-0.0028` n `6`; index avg `0.0206` n `25`; metal avg `-0.0276` n `20`; unknown avg `-0.0651` n `763`
- 1h: commodity avg `0.1233` n `12`; crypto_alt avg `-0.2304` n `229`; crypto_major avg `-0.3111` n `8`; equity avg `-0.528` n `91`; fx avg `-0.0153` n `6`; index avg `-0.0538` n `25`; metal avg `-0.0034` n `20`; unknown avg `0.0223` n `763`
- 4h: commodity avg `0.0048` n `12`; crypto_alt avg `1.9593` n `229`; crypto_major avg `2.0245` n `8`; equity avg `-0.252` n `90`; fx avg `0.0223` n `6`; index avg `-0.0037` n `25`; metal avg `0.1524` n `20`; unknown avg `2.4409` n `763`
- 24h: commodity avg `-0.0508` n `12`; crypto_alt avg `0.9128` n `229`; crypto_major avg `0.6972` n `8`; equity avg `-0.6348` n `90`; fx avg `0.1977` n `6`; index avg `0.0214` n `25`; metal avg `-0.2359` n `20`; unknown avg `0.8025` n `729`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1148`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0978`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0882`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.081`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0736`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0734`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0718`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0717`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0639`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0599`, n `668`, weak_sample_signal
