# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-19T21:46:17.325339+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `6.5173` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `5.9705` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `5.4146` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 1h_commodity_crypto_divergence: score `2.3467` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 1h_crypto_metal_divergence: score `2.3362` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_crypto_equity_divergence: score `2.1346` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0194` n `12`; crypto_alt avg `0.3826` n `230`; crypto_major avg `0.6118` n `8`; equity avg `0.0525` n `121`; fx avg `0.0149` n `6`; index avg `0.0073` n `25`; metal avg `0.0188` n `20`; unknown avg `0.0439` n `792`
- 1h: commodity avg `0.0453` n `12`; crypto_alt avg `1.1159` n `230`; crypto_major avg `2.392` n `8`; equity avg `0.2574` n `121`; fx avg `-0.0065` n `6`; index avg `0.0412` n `25`; metal avg `0.0558` n `20`; unknown avg `0.3091` n `792`
- 4h: commodity avg `-0.2376` n `12`; crypto_alt avg `3.1003` n `230`; crypto_major avg `6.2797` n `8`; equity avg `0.8651` n `121`; fx avg `-0.0225` n `6`; index avg `0.0685` n `25`; metal avg `0.3092` n `20`; unknown avg `1.6836` n `792`
- 24h: commodity avg `-0.0209` n `12`; crypto_alt avg `6.3936` n `230`; crypto_major avg `11.5882` n `8`; equity avg `0.7019` n `120`; fx avg `-0.2105` n `6`; index avg `0.0992` n `25`; metal avg `1.2496` n `20`; unknown avg `1.4358` n `757`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.2436`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1889`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1869`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1699`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1645`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1639`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1635`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1299`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1295`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1274`, n `668`, weak_sample_signal
