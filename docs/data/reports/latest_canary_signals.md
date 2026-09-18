# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-18T15:37:31.026052+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `2.7281` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `2.6886` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_commodity_crypto_divergence: score `2.0601` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `0.0228` n `12`; crypto_alt avg `-0.0362` n `234`; crypto_major avg `-0.1631` n `8`; equity avg `0.0866` n `140`; fx avg `-0.0094` n `6`; index avg `0.0017` n `26`; metal avg `-0.0055` n `20`; unknown avg `-0.3305` n `928`
- 1h: commodity avg `0.0052` n `12`; crypto_alt avg `0.2075` n `234`; crypto_major avg `0.1757` n `8`; equity avg `0.133` n `140`; fx avg `-0.0714` n `6`; index avg `-0.0048` n `26`; metal avg `0.0418` n `20`; unknown avg `-0.4728` n `914`
- 4h: commodity avg `0.3994` n `12`; crypto_alt avg `1.3676` n `234`; crypto_major avg `2.4595` n `8`; equity avg `-0.2291` n `140`; fx avg `-0.0449` n `6`; index avg `-0.1312` n `26`; metal avg `-0.2686` n `20`; unknown avg `0.9941` n `884`
- 24h: commodity avg `0.1816` n `12`; crypto_alt avg `6.1806` n `234`; crypto_major avg `6.0845` n `8`; equity avg `0.7416` n `140`; fx avg `0.2243` n `6`; index avg `-0.1035` n `26`; metal avg `0.112` n `20`; unknown avg `2.9177` n `717`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1636`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1612`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.157`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1445`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1311`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1238`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.119`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1149`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1099`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1087`, n `668`, weak_sample_signal
