# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-20T00:22:31.815600+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.657` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.639` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `1.9455` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0233` n `12`; crypto_alt avg `0.2154` n `230`; crypto_major avg `0.2649` n `8`; equity avg `0.4456` n `121`; fx avg `-0.0387` n `6`; index avg `0.1284` n `25`; metal avg `0.0012` n `20`; unknown avg `0.0804` n `792`
- 1h: commodity avg `0.0121` n `12`; crypto_alt avg `0.5556` n `230`; crypto_major avg `0.3534` n `8`; equity avg `0.1179` n `121`; fx avg `-0.0383` n `6`; index avg `0.0219` n `25`; metal avg `-0.029` n `20`; unknown avg `0.0593` n `792`
- 4h: commodity avg `0.0571` n `12`; crypto_alt avg `1.6989` n `230`; crypto_major avg `2.7141` n `8`; equity avg `0.7686` n `121`; fx avg `-0.0352` n `6`; index avg `0.1487` n `25`; metal avg `0.0751` n `20`; unknown avg `0.3088` n `792`
- 24h: commodity avg `-0.0662` n `12`; crypto_alt avg `5.636` n `230`; crypto_major avg `9.9106` n `8`; equity avg `1.6312` n `120`; fx avg `-0.214` n `6`; index avg `0.2994` n `25`; metal avg `1.1977` n `20`; unknown avg `1.498` n `757`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1906`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1542`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1521`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1491`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1455`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1423`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1299`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1195`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1126`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0949`, n `668`, weak_sample_signal
