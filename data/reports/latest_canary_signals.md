# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-25T12:07:27.367007+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.4994` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `1.9464` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `1.8387` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0095` n `12`; crypto_alt avg `0.0908` n `234`; crypto_major avg `0.317` n `8`; equity avg `-0.0518` n `141`; fx avg `0.0159` n `6`; index avg `0.0027` n `26`; metal avg `0.035` n `20`; unknown avg `0.1153` n `936`
- 1h: commodity avg `-0.0897` n `12`; crypto_alt avg `0.1774` n `234`; crypto_major avg `0.2691` n `8`; equity avg `-0.0024` n `141`; fx avg `0.0064` n `6`; index avg `0.0192` n `26`; metal avg `-0.0628` n `20`; unknown avg `0.1455` n `936`
- 4h: commodity avg `-0.2984` n `12`; crypto_alt avg `2.1098` n `234`; crypto_major avg `2.201` n `8`; equity avg `0.3623` n `141`; fx avg `-0.0281` n `6`; index avg `0.0874` n `26`; metal avg `0.2546` n `20`; unknown avg `2.0658` n `934`
- 24h: commodity avg `-0.0741` n `12`; crypto_alt avg `5.8702` n `234`; crypto_major avg `4.0445` n `8`; equity avg `1.8975` n `141`; fx avg `-0.2032` n `6`; index avg `0.309` n `26`; metal avg `0.2806` n `20`; unknown avg `12.7519` n `797`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1489`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.137`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1349`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1291`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1289`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1196`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1173`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1043`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0988`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.083`, n `668`, weak_sample_signal
