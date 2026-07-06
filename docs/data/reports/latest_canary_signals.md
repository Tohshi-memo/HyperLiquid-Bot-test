# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-06T17:22:27.332347+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.9219` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.7346` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `1.8755` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0113` n `12`; crypto_alt avg `-0.1476` n `229`; crypto_major avg `-0.0816` n `8`; equity avg `-0.1277` n `88`; fx avg `-0.004` n `6`; index avg `-0.0286` n `25`; metal avg `-0.075` n `20`; unknown avg `0.0484` n `766`
- 1h: commodity avg `-0.1012` n `12`; crypto_alt avg `-0.004` n `229`; crypto_major avg `0.1773` n `8`; equity avg `-0.1316` n `88`; fx avg `0.0078` n `6`; index avg `-0.0607` n `25`; metal avg `0.0881` n `20`; unknown avg `0.0372` n `766`
- 4h: commodity avg `-0.0603` n `12`; crypto_alt avg `2.8676` n `229`; crypto_major avg `2.8616` n `8`; equity avg `0.9861` n `88`; fx avg `0.0261` n `6`; index avg `0.1058` n `25`; metal avg `0.127` n `20`; unknown avg `3.781` n `765`
- 24h: commodity avg `-0.1583` n `12`; crypto_alt avg `1.1503` n `229`; crypto_major avg `0.9599` n `8`; equity avg `-0.1836` n `88`; fx avg `0.2072` n `6`; index avg `0.0492` n `25`; metal avg `-0.3073` n `20`; unknown avg `0.7893` n `731`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1137`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0985`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0893`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0878`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0743`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0727`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0711`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0672`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0624`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0615`, n `668`, weak_sample_signal
