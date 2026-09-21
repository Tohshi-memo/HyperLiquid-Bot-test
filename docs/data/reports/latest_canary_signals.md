# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-21T12:07:33.851733+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.7901` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.3809` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `2.0128` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.011` n `12`; crypto_alt avg `-0.1153` n `234`; crypto_major avg `0.0807` n `8`; equity avg `0.108` n `140`; fx avg `0.0106` n `6`; index avg `0.0239` n `26`; metal avg `-0.0163` n `20`; unknown avg `1.7983` n `934`
- 1h: commodity avg `-0.0994` n `12`; crypto_alt avg `-0.1678` n `234`; crypto_major avg `0.2583` n `8`; equity avg `0.1542` n `140`; fx avg `0.0322` n `6`; index avg `0.0411` n `26`; metal avg `0.203` n `20`; unknown avg `2.2742` n `910`
- 4h: commodity avg `-0.2258` n `12`; crypto_alt avg `2.1045` n `234`; crypto_major avg `2.5643` n `8`; equity avg `0.5515` n `140`; fx avg `0.0219` n `6`; index avg `0.0876` n `26`; metal avg `0.1834` n `20`; unknown avg `3.6007` n `910`
- 24h: commodity avg `-0.8416` n `12`; crypto_alt avg `6.5906` n `234`; crypto_major avg `5.7946` n `8`; equity avg `2.1349` n `140`; fx avg `-0.0702` n `6`; index avg `0.398` n `26`; metal avg `0.1763` n `20`; unknown avg `7.4842` n `733`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1941`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1573`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1473`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1166`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1099`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1075`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1048`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0981`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0948`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0884`, n `668`, weak_sample_signal
