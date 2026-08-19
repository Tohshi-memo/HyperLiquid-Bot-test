# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-19T21:37:43.562481+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `6.2856` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `5.7406` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `5.0762` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 1h_crypto_metal_divergence: score `3.0938` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_commodity_crypto_divergence: score `3.0927` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 1h_crypto_equity_divergence: score `2.8266` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- polymarket_volume_spike: score `2.04` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0219` n `12`; crypto_alt avg `-0.0575` n `230`; crypto_major avg `0.2193` n `8`; equity avg `0.036` n `121`; fx avg `0.0009` n `6`; index avg `0.012` n `25`; metal avg `-0.0134` n `20`; unknown avg `0.0464` n `792`
- 1h: commodity avg `0.0565` n `12`; crypto_alt avg `1.7431` n `230`; crypto_major avg `3.1492` n `8`; equity avg `0.3226` n `121`; fx avg `-0.0251` n `6`; index avg `0.0618` n `25`; metal avg `0.0554` n `20`; unknown avg `0.3528` n `792`
- 4h: commodity avg `-0.2521` n `12`; crypto_alt avg `2.8445` n `230`; crypto_major avg `6.0335` n `8`; equity avg `0.9573` n `121`; fx avg `-0.0258` n `6`; index avg `0.0713` n `25`; metal avg `0.2929` n `20`; unknown avg `1.7364` n `792`
- 24h: commodity avg `-0.0088` n `12`; crypto_alt avg `5.9354` n `230`; crypto_major avg `10.8898` n `8`; equity avg `0.6062` n `120`; fx avg `-0.2296` n `6`; index avg `0.083` n `25`; metal avg `1.2163` n `20`; unknown avg `1.3736` n `757`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.2342`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1799`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1797`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.167`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1643`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1596`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1542`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1324`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.129`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1136`, n `668`, weak_sample_signal
