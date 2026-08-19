# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-19T19:34:55.900866+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.2408` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_equity_divergence: score `1.8478` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_crypto_metal_divergence: score `1.5781` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0376` n `12`; crypto_alt avg `0.0019` n `230`; crypto_major avg `-0.0614` n `8`; equity avg `0.1569` n `121`; fx avg `-0.0046` n `6`; index avg `0.0001` n `25`; metal avg `0.0231` n `20`; unknown avg `0.0238` n `792`
- 1h: commodity avg `-0.1359` n `12`; crypto_alt avg `0.4755` n `230`; crypto_major avg `1.6642` n `8`; equity avg `0.3656` n `121`; fx avg `-0.0031` n `6`; index avg `0.0026` n `25`; metal avg `0.1982` n `20`; unknown avg `0.3149` n `792`
- 4h: commodity avg `-0.4157` n `12`; crypto_alt avg `-0.0355` n `230`; crypto_major avg `1.8251` n `8`; equity avg `-0.0227` n `121`; fx avg `-0.0269` n `6`; index avg `-0.0563` n `25`; metal avg `0.247` n `20`; unknown avg `0.1524` n `792`
- 24h: commodity avg `-0.063` n `12`; crypto_alt avg `3.2371` n `230`; crypto_major avg `6.4983` n `8`; equity avg `-0.2802` n `120`; fx avg `-0.2071` n `6`; index avg `-0.0112` n `25`; metal avg `1.0136` n `20`; unknown avg `0.7086` n `757`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1841`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1624`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1543`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1493`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1434`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1219`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1202`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1153`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1106`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0908`, n `668`, weak_sample_signal
