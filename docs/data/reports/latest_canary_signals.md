# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-18T15:22:33.668623+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `3.1327` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_crypto_metal_divergence: score `3.0881` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_commodity_crypto_divergence: score `2.5053` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `0.0245` n `12`; crypto_alt avg `0.1708` n `234`; crypto_major avg `0.0966` n `8`; equity avg `-0.0435` n `140`; fx avg `0.0019` n `6`; index avg `-0.0147` n `26`; metal avg `-0.0016` n `20`; unknown avg `0.2953` n `916`
- 1h: commodity avg `-0.0473` n `12`; crypto_alt avg `0.1447` n `234`; crypto_major avg `0.3904` n `8`; equity avg `0.067` n `140`; fx avg `-0.06` n `6`; index avg `-0.0127` n `26`; metal avg `0.0458` n `20`; unknown avg `-0.2089` n `912`
- 4h: commodity avg `0.3287` n `12`; crypto_alt avg `1.798` n `234`; crypto_major avg `2.834` n `8`; equity avg `-0.2987` n `140`; fx avg `-0.0505` n `6`; index avg `-0.1133` n `26`; metal avg `-0.2541` n `20`; unknown avg `1.2922` n `881`
- 24h: commodity avg `0.1705` n `12`; crypto_alt avg `6.7064` n `234`; crypto_major avg `6.7459` n `8`; equity avg `0.776` n `140`; fx avg `0.2126` n `6`; index avg `-0.0837` n `26`; metal avg `0.1315` n `20`; unknown avg `2.2132` n `717`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1598`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1591`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1553`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1435`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1315`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1249`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1198`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1156`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1103`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1093`, n `668`, weak_sample_signal
