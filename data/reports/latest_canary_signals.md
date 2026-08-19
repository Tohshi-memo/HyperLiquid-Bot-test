# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-19T21:13:07.997178+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `5.4781` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `4.8544` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `4.481` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 1h_commodity_crypto_divergence: score `2.9158` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 1h_crypto_metal_divergence: score `2.8707` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_crypto_equity_divergence: score `2.673` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0676` n `12`; crypto_alt avg `0.9115` n `230`; crypto_major avg `1.1561` n `8`; equity avg `0.1634` n `121`; fx avg `-0.0235` n `6`; index avg `0.0329` n `25`; metal avg `0.0544` n `20`; unknown avg `0.2738` n `792`
- 1h: commodity avg `0.0914` n `12`; crypto_alt avg `2.0002` n `230`; crypto_major avg `3.0072` n `8`; equity avg `0.3342` n `121`; fx avg `-0.0293` n `6`; index avg `0.066` n `25`; metal avg `0.1365` n `20`; unknown avg `0.5278` n `792`
- 4h: commodity avg `-0.3294` n `12`; crypto_alt avg `2.862` n `230`; crypto_major avg `5.1487` n `8`; equity avg `0.6677` n `121`; fx avg `-0.0366` n `6`; index avg `0.0354` n `25`; metal avg `0.2943` n `20`; unknown avg `1.5683` n `792`
- 24h: commodity avg `-0.0213` n `12`; crypto_alt avg `6.0978` n `230`; crypto_major avg `10.1186` n `8`; equity avg `0.5006` n `120`; fx avg `-0.2257` n `6`; index avg `0.0794` n `25`; metal avg `1.2532` n `20`; unknown avg `1.3684` n `757`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.2105`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1768`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1582`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1568`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1561`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1389`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1343`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1287`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1247`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1198`, n `668`, weak_sample_signal
