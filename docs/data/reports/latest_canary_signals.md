# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-03T15:07:32.546284+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `3.9976` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `3.0751` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `2.8877` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 1h_commodity_crypto_divergence: score `2.7282` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 1h_crypto_metal_divergence: score `2.2331` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_crypto_equity_divergence: score `1.6475` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0374` n `12`; crypto_alt avg `0.3426` n `232`; crypto_major avg `0.8288` n `8`; equity avg `0.6049` n `133`; fx avg `0.014` n `6`; index avg `0.1299` n `26`; metal avg `0.2279` n `20`; unknown avg `0.6124` n `790`
- 1h: commodity avg `-0.1247` n `12`; crypto_alt avg `1.6337` n `232`; crypto_major avg `2.6035` n `8`; equity avg `0.956` n `133`; fx avg `0.026` n `6`; index avg `0.1576` n `26`; metal avg `0.3704` n `20`; unknown avg `1.1361` n `790`
- 4h: commodity avg `-0.2362` n `12`; crypto_alt avg `1.8785` n `232`; crypto_major avg `3.7614` n `8`; equity avg `0.8737` n `133`; fx avg `-0.0263` n `6`; index avg `0.2162` n `26`; metal avg `0.6863` n `20`; unknown avg `24.1124` n `790`
- 24h: commodity avg `0.1428` n `12`; crypto_alt avg `3.9099` n `232`; crypto_major avg `5.2776` n `8`; equity avg `1.7372` n `133`; fx avg `-0.2913` n `6`; index avg `0.1508` n `26`; metal avg `0.8768` n `20`; unknown avg `0.8242` n `735`

## Correlations

- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.123`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0964`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.09`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.087`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0816`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.074`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0679`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0653`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0552`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0478`, n `668`, weak_sample_signal
