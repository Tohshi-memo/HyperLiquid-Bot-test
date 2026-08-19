# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-19T20:07:32.336886+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `1.7337` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 1h_crypto_metal_divergence: score `1.611` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0036` n `12`; crypto_alt avg `0.1196` n `230`; crypto_major avg `0.004` n `8`; equity avg `0.2114` n `121`; fx avg `-0.0019` n `6`; index avg `0.0106` n `25`; metal avg `-0.0173` n `20`; unknown avg `0.5807` n `792`
- 1h: commodity avg `-0.0316` n `12`; crypto_alt avg `0.788` n `230`; crypto_major avg `1.6423` n `8`; equity avg `0.5453` n `121`; fx avg `-0.0099` n `6`; index avg `-0.0117` n `25`; metal avg `0.0313` n `20`; unknown avg `1.0575` n `792`
- 4h: commodity avg `-0.3785` n `12`; crypto_alt avg `0.8906` n `230`; crypto_major avg `1.5652` n `8`; equity avg `-0.1685` n `121`; fx avg `-0.0179` n `6`; index avg `-0.1054` n `25`; metal avg `0.1124` n `20`; unknown avg `0.5429` n `792`
- 24h: commodity avg `-0.0567` n `12`; crypto_alt avg `3.8616` n `230`; crypto_major avg `6.7938` n `8`; equity avg `0.121` n `120`; fx avg `-0.1932` n `6`; index avg `0.0145` n `25`; metal avg `1.0881` n `20`; unknown avg `1.0445` n `757`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1856`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1843`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1556`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1448`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.136`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1332`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1252`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1235`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1088`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1087`, n `668`, weak_sample_signal
