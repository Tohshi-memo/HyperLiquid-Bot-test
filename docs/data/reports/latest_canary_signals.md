# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-19T20:37:33.067938+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.4015` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_equity_divergence: score `2.0931` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_crypto_metal_divergence: score `1.8625` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0014` n `12`; crypto_alt avg `0.0713` n `230`; crypto_major avg `0.3281` n `8`; equity avg `0.0525` n `121`; fx avg `-0.0004` n `6`; index avg `0.0083` n `25`; metal avg `0.0634` n `20`; unknown avg `0.0211` n `792`
- 1h: commodity avg `0.0551` n `12`; crypto_alt avg `0.374` n `230`; crypto_major avg `0.6116` n `8`; equity avg `0.3079` n `121`; fx avg `-0.0005` n `6`; index avg `0.0032` n `25`; metal avg `0.0824` n `20`; unknown avg `0.3894` n `792`
- 4h: commodity avg `-0.3586` n `12`; crypto_alt avg `0.7123` n `230`; crypto_major avg `2.0429` n `8`; equity avg `-0.0502` n `121`; fx avg `-0.0124` n `6`; index avg `-0.0514` n `25`; metal avg `0.1804` n `20`; unknown avg `0.8785` n `792`
- 24h: commodity avg `-0.096` n `12`; crypto_alt avg `3.9421` n `230`; crypto_major avg `7.2039` n `8`; equity avg `0.0733` n `120`; fx avg `-0.2043` n `6`; index avg `0.0082` n `25`; metal avg `1.1747` n `20`; unknown avg `1.0313` n `757`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.188`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1848`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.155`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1443`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1362`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1323`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1266`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1231`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1119`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1065`, n `668`, weak_sample_signal
