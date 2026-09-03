# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-03T18:07:32.809670+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `3.5727` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.8006` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `1.5909` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0852` n `12`; crypto_alt avg `0.1474` n `232`; crypto_major avg `0.0471` n `8`; equity avg `0.0456` n `133`; fx avg `-0.0009` n `6`; index avg `0.017` n `26`; metal avg `-0.0224` n `20`; unknown avg `-0.084` n `790`
- 1h: commodity avg `-0.196` n `12`; crypto_alt avg `0.4357` n `232`; crypto_major avg `0.3169` n `8`; equity avg `0.2041` n `133`; fx avg `-0.0043` n `6`; index avg `0.0456` n `26`; metal avg `-0.0014` n `20`; unknown avg `0.016` n `790`
- 4h: commodity avg `-0.3911` n `12`; crypto_alt avg `2.7857` n `232`; crypto_major avg `3.1816` n `8`; equity avg `1.5907` n `133`; fx avg `0.0408` n `6`; index avg `0.2723` n `26`; metal avg `0.381` n `20`; unknown avg `2.8772` n `790`
- 24h: commodity avg `-0.1937` n `12`; crypto_alt avg `4.6916` n `232`; crypto_major avg `5.466` n `8`; equity avg `1.8318` n `133`; fx avg `-0.2589` n `6`; index avg `0.2175` n `26`; metal avg `0.9025` n `20`; unknown avg `0.8955` n `736`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.118`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1139`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.096`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0928`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0829`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0819`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0814`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0739`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0666`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0664`, n `668`, weak_sample_signal
