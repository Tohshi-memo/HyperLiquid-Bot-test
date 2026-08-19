# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-19T23:11:07.401784+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `4.3609` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `4.2208` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `3.1392` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0379` n `12`; crypto_alt avg `0.0652` n `230`; crypto_major avg `0.2738` n `8`; equity avg `0.0551` n `121`; fx avg `-0.0026` n `6`; index avg `0.0068` n `25`; metal avg `0.0173` n `20`; unknown avg `0.0359` n `792`
- 1h: commodity avg `0.0091` n `12`; crypto_alt avg `-0.3669` n `230`; crypto_major avg `-0.8213` n `8`; equity avg `0.2373` n `121`; fx avg `0.0258` n `6`; index avg `0.0485` n `25`; metal avg `-0.0011` n `20`; unknown avg `-0.0601` n `792`
- 4h: commodity avg `0.0012` n `12`; crypto_alt avg `1.955` n `230`; crypto_major avg `4.3621` n `8`; equity avg `1.2229` n `121`; fx avg `-0.0103` n `6`; index avg `0.123` n `25`; metal avg `0.1413` n `20`; unknown avg `0.9752` n `792`
- 24h: commodity avg `-0.098` n `12`; crypto_alt avg `5.2243` n `230`; crypto_major avg `9.8166` n `8`; equity avg `1.2124` n `120`; fx avg `-0.197` n `6`; index avg `0.1661` n `25`; metal avg `1.2728` n `20`; unknown avg `1.4825` n `757`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.2065`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1632`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1586`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1509`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1442`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1442`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1309`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1206`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1153`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.106`, n `668`, weak_sample_signal
