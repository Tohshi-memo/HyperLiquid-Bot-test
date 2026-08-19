# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-19T19:22:36.169891+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `3.997` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_equity_divergence: score `3.7959` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_crypto_metal_divergence: score `3.3619` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_commodity_crypto_divergence: score `2.115` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 1h_crypto_metal_divergence: score `1.7028` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_crypto_equity_divergence: score `1.647` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0384` n `12`; crypto_alt avg `0.3683` n `230`; crypto_major avg `1.5627` n `8`; equity avg `0.0869` n `121`; fx avg `-0.0089` n `6`; index avg `0.0028` n `25`; metal avg `0.0173` n `20`; unknown avg `0.2934` n `792`
- 1h: commodity avg `-0.2068` n `12`; crypto_alt avg `0.577` n `230`; crypto_major avg `1.9082` n `8`; equity avg `0.2612` n `121`; fx avg `0.0086` n `6`; index avg `0.0435` n `25`; metal avg `0.2054` n `20`; unknown avg `0.2868` n `792`
- 4h: commodity avg `-0.3889` n `12`; crypto_alt avg `1.3049` n `230`; crypto_major avg `3.6081` n `8`; equity avg `-0.1878` n `121`; fx avg `-0.0173` n `6`; index avg `-0.0734` n `25`; metal avg `0.2462` n `20`; unknown avg `0.2323` n `792`
- 24h: commodity avg `-0.0338` n `12`; crypto_alt avg `3.2577` n `230`; crypto_major avg `6.6238` n `8`; equity avg `-0.2891` n `120`; fx avg `-0.1993` n `6`; index avg `-0.003` n `25`; metal avg `0.9739` n `20`; unknown avg `0.6971` n `757`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1847`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1538`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1536`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1484`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1434`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1235`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1209`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1044`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1039`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0911`, n `668`, weak_sample_signal
