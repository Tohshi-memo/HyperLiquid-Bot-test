# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-19T20:22:30.618828+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.0889` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_equity_divergence: score `1.8425` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_crypto_metal_divergence: score `1.6041` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0166` n `12`; crypto_alt avg `-0.0173` n `230`; crypto_major avg `0.0882` n `8`; equity avg `-0.0166` n `121`; fx avg `-0.0034` n `6`; index avg `-0.0017` n `25`; metal avg `0.0059` n `20`; unknown avg `0.0622` n `792`
- 1h: commodity avg `0.0235` n `12`; crypto_alt avg `0.4054` n `230`; crypto_major avg `0.1845` n `8`; equity avg `0.4358` n `121`; fx avg `-0.0043` n `6`; index avg `-0.0162` n `25`; metal avg `0.02` n `20`; unknown avg `0.7608` n `792`
- 4h: commodity avg `-0.3697` n `12`; crypto_alt avg `0.7235` n `230`; crypto_major avg `1.7192` n `8`; equity avg `-0.1233` n `121`; fx avg `-0.0291` n `6`; index avg `-0.0931` n `25`; metal avg `0.1151` n `20`; unknown avg `0.5439` n `792`
- 24h: commodity avg `-0.0609` n `12`; crypto_alt avg `3.8707` n `230`; crypto_major avg `6.8544` n `8`; equity avg `0.0977` n `120`; fx avg `-0.2007` n `6`; index avg `0.0181` n `25`; metal avg `1.1061` n `20`; unknown avg `0.9637` n `757`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1863`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1843`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1559`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1457`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.133`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1307`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1283`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.124`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1086`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1042`, n `668`, weak_sample_signal
