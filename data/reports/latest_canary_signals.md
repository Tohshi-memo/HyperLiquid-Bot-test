# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-20T00:24:45.720932+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.6328` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.6098` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `2.0039` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0198` n `12`; crypto_alt avg `0.2892` n `230`; crypto_major avg `0.2385` n `8`; equity avg `0.359` n `121`; fx avg `-0.0354` n `6`; index avg `0.1028` n `25`; metal avg `0.0026` n `20`; unknown avg `0.08` n `792`
- 1h: commodity avg `0.0086` n `12`; crypto_alt avg `0.6296` n `230`; crypto_major avg `0.3266` n `8`; equity avg `0.0322` n `121`; fx avg `-0.0349` n `6`; index avg `-0.0035` n `25`; metal avg `-0.0275` n `20`; unknown avg `0.0494` n `792`
- 4h: commodity avg `0.0536` n `12`; crypto_alt avg `1.7746` n `230`; crypto_major avg `2.6864` n `8`; equity avg `0.6825` n `121`; fx avg `-0.0318` n `6`; index avg `0.123` n `25`; metal avg `0.0766` n `20`; unknown avg `0.31` n `792`
- 24h: commodity avg `-0.0697` n `12`; crypto_alt avg `5.7163` n `230`; crypto_major avg `9.8828` n `8`; equity avg `1.5481` n `120`; fx avg `-0.2107` n `6`; index avg `0.2733` n `25`; metal avg `1.1994` n `20`; unknown avg `1.4979` n `757`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1905`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1539`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1526`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.149`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1454`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1437`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1304`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1207`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1123`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0955`, n `668`, weak_sample_signal
