# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-03T16:37:28.919569+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `3.4915` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.6988` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `2.0983` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0744` n `12`; crypto_alt avg `0.1119` n `232`; crypto_major avg `0.0503` n `8`; equity avg `0.0102` n `133`; fx avg `0.0023` n `6`; index avg `-0.0028` n `26`; metal avg `-0.0178` n `20`; unknown avg `0.0388` n `792`
- 1h: commodity avg `-0.0074` n `12`; crypto_alt avg `0.1406` n `232`; crypto_major avg `0.3554` n `8`; equity avg `0.0476` n `133`; fx avg `0.0151` n `6`; index avg `-0.0009` n `26`; metal avg `-0.0746` n `20`; unknown avg `22.4649` n `790`
- 4h: commodity avg `-0.402` n `12`; crypto_alt avg `1.7962` n `232`; crypto_major avg `3.0895` n `8`; equity avg `0.9912` n `133`; fx avg `0.0403` n `6`; index avg `0.205` n `26`; metal avg `0.3907` n `20`; unknown avg `7.9555` n `790`
- 24h: commodity avg `-0.1151` n `12`; crypto_alt avg `3.7563` n `232`; crypto_major avg `4.9149` n `8`; equity avg `1.8127` n `133`; fx avg `-0.2755` n `6`; index avg `0.1829` n `26`; metal avg `0.9462` n `20`; unknown avg `0.7894` n `736`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1325`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1138`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1125`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1106`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0817`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0815`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0807`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.08`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0676`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0667`, n `668`, weak_sample_signal
