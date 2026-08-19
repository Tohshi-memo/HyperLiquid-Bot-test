# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-19T23:37:25.613665+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.6424` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.6145` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `1.8114` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.022` n `12`; crypto_alt avg `0.0653` n `230`; crypto_major avg `0.0761` n `8`; equity avg `0.013` n `121`; fx avg `0.0119` n `6`; index avg `0.0057` n `25`; metal avg `-0.0157` n `20`; unknown avg `0.0237` n `792`
- 1h: commodity avg `0.0442` n `12`; crypto_alt avg `-0.0666` n `230`; crypto_major avg `-0.4469` n `8`; equity avg `0.1062` n `121`; fx avg `0.0337` n `6`; index avg `0.0241` n `25`; metal avg `0.014` n `20`; unknown avg `-0.0651` n `792`
- 4h: commodity avg `0.0796` n `12`; crypto_alt avg `1.5105` n `230`; crypto_major avg `2.722` n `8`; equity avg `0.9106` n `121`; fx avg `0.0149` n `6`; index avg `0.127` n `25`; metal avg `0.1075` n `20`; unknown avg `0.4652` n `792`
- 24h: commodity avg `-0.0922` n `12`; crypto_alt avg `5.0758` n `230`; crypto_major avg `9.4534` n `8`; equity avg `1.306` n `120`; fx avg `-0.183` n `6`; index avg `0.1711` n `25`; metal avg `1.3274` n `20`; unknown avg `1.4779` n `757`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1911`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1508`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1481`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1406`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1387`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1381`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1247`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1121`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.111`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0979`, n `668`, weak_sample_signal
