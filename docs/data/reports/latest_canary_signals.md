# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-19T23:42:21.298606+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.892` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.8568` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `2.0081` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0401` n `12`; crypto_alt avg `0.2026` n `230`; crypto_major avg `0.3` n `8`; equity avg `0.0472` n `121`; fx avg `0.0056` n `6`; index avg `0.002` n `25`; metal avg `-0.0265` n `20`; unknown avg `0.0362` n `792`
- 1h: commodity avg `0.026` n `12`; crypto_alt avg `0.0694` n `230`; crypto_major avg `-0.2243` n `8`; equity avg `0.1404` n `121`; fx avg `0.0274` n `6`; index avg `0.0204` n `25`; metal avg `0.0032` n `20`; unknown avg `-0.0519` n `792`
- 4h: commodity avg `0.0614` n `12`; crypto_alt avg `1.6489` n `230`; crypto_major avg `2.9534` n `8`; equity avg `0.9453` n `121`; fx avg `0.0086` n `6`; index avg `0.1233` n `25`; metal avg `0.0966` n `20`; unknown avg `0.4789` n `792`
- 24h: commodity avg `-0.1103` n `12`; crypto_alt avg `5.226` n `230`; crypto_major avg `9.703` n `8`; equity avg `1.3401` n `120`; fx avg `-0.1893` n `6`; index avg `0.1673` n `25`; metal avg `1.3161` n `20`; unknown avg `1.4927` n `757`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1932`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1525`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1495`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1417`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1404`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1384`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.126`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1123`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1119`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.099`, n `668`, weak_sample_signal
