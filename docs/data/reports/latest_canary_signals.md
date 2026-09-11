# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-11T16:07:29.734414+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.68` - Polymarket crypto volume is unusually high.
- 4h_commodity_crypto_divergence: score `2.7535` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.7079` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `2.1678` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0968` n `12`; crypto_alt avg `-0.2618` n `233`; crypto_major avg `-0.2909` n `8`; equity avg `0.0045` n `136`; fx avg `0.0055` n `6`; index avg `-0.005` n `26`; metal avg `-0.0188` n `20`; unknown avg `0.0342` n `794`
- 1h: commodity avg `0.0517` n `12`; crypto_alt avg `-0.5275` n `233`; crypto_major avg `-0.552` n `8`; equity avg `0.1749` n `136`; fx avg `-0.0087` n `6`; index avg `0.0463` n `26`; metal avg `0.0157` n `20`; unknown avg `1.1767` n `794`
- 4h: commodity avg `0.1245` n `12`; crypto_alt avg `2.9798` n `233`; crypto_major avg `2.878` n `8`; equity avg `0.7102` n `136`; fx avg `-0.0382` n `6`; index avg `0.146` n `26`; metal avg `0.1701` n `20`; unknown avg `0.9049` n `772`
- 24h: commodity avg `-0.253` n `12`; crypto_alt avg `1.9725` n `233`; crypto_major avg `2.6474` n `8`; equity avg `0.4649` n `136`; fx avg `-0.1358` n `6`; index avg `0.3225` n `26`; metal avg `0.0773` n `20`; unknown avg `2.4139` n `697`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.121`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1154`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1076`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1022`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1019`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0945`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0927`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0809`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0792`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0771`, n `668`, weak_sample_signal
