# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-19T22:10:27.755358+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `5.9691` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `5.4783` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `4.6818` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0493` n `12`; crypto_alt avg `-0.5237` n `230`; crypto_major avg `-0.3557` n `8`; equity avg `-0.0007` n `121`; fx avg `-0.0125` n `6`; index avg `0.009` n `25`; metal avg `-0.0258` n `20`; unknown avg `0.0071` n `792`
- 1h: commodity avg `-0.0675` n `12`; crypto_alt avg `-0.4394` n `230`; crypto_major avg `0.5158` n `8`; equity avg `0.1025` n `121`; fx avg `0.0031` n `6`; index avg `0.0199` n `25`; metal avg `-0.0255` n `20`; unknown avg `0.0605` n `792`
- 4h: commodity avg `-0.2146` n `12`; crypto_alt avg `2.5837` n `230`; crypto_major avg `5.7545` n `8`; equity avg `1.0727` n `121`; fx avg `-0.0258` n `6`; index avg `0.1013` n `25`; metal avg `0.2762` n `20`; unknown avg `1.7043` n `792`
- 24h: commodity avg `-0.1073` n `12`; crypto_alt avg `5.6145` n `230`; crypto_major avg `10.7504` n `8`; equity avg `0.7342` n `120`; fx avg `-0.2257` n `6`; index avg `0.0958` n `25`; metal avg `1.2361` n `20`; unknown avg `1.3996` n `757`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.2446`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1903`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1802`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1723`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1636`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1625`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.159`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.129`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1284`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1248`, n `668`, weak_sample_signal
