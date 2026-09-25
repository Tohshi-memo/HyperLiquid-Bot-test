# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-25T11:07:31.449965+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.1879` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_equity_divergence: score `1.805` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_crypto_metal_divergence: score `1.7634` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0597` n `12`; crypto_alt avg `0.544` n `234`; crypto_major avg `0.6317` n `8`; equity avg `0.047` n `141`; fx avg `-0.0057` n `6`; index avg `0.0206` n `26`; metal avg `0.0302` n `20`; unknown avg `4.453` n `942`
- 1h: commodity avg `-0.0407` n `12`; crypto_alt avg `1.0088` n `234`; crypto_major avg `1.2435` n `8`; equity avg `0.1211` n `141`; fx avg `-0.0152` n `6`; index avg `0.0083` n `26`; metal avg `0.1482` n `20`; unknown avg `1.6175` n `942`
- 4h: commodity avg `-0.0981` n `12`; crypto_alt avg `2.3465` n `234`; crypto_major avg `2.0898` n `8`; equity avg `0.2848` n `141`; fx avg `-0.0306` n `6`; index avg `0.0447` n `26`; metal avg `0.3264` n `20`; unknown avg `2.0954` n `924`
- 24h: commodity avg `0.0027` n `12`; crypto_alt avg `5.5542` n `234`; crypto_major avg `3.6261` n `8`; equity avg `1.7672` n `141`; fx avg `-0.2354` n `6`; index avg `0.2817` n `26`; metal avg `0.4042` n `20`; unknown avg `12.5391` n `797`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1572`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1425`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1407`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1372`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1318`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1222`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1189`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1014`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0993`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0823`, n `668`, weak_sample_signal
