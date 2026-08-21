# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-21T23:22:28.600356+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `4.2811` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_commodity_crypto_divergence: score `4.2264` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_equity_divergence: score `4.1902` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0112` n `12`; crypto_alt avg `0.2607` n `230`; crypto_major avg `0.4063` n `8`; equity avg `-0.0354` n `121`; fx avg `0.0001` n `6`; index avg `0.002` n `25`; metal avg `0.0041` n `20`; unknown avg `0.0799` n `793`
- 1h: commodity avg `-0.0059` n `12`; crypto_alt avg `0.3039` n `230`; crypto_major avg `0.6357` n `8`; equity avg `-0.0298` n `121`; fx avg `-0.0064` n `6`; index avg `0.0154` n `25`; metal avg `0.0074` n `20`; unknown avg `-0.0205` n `793`
- 4h: commodity avg `0.0162` n `12`; crypto_alt avg `3.2032` n `230`; crypto_major avg `4.2426` n `8`; equity avg `0.0524` n `121`; fx avg `-0.0115` n `6`; index avg `0.0158` n `25`; metal avg `-0.0385` n `20`; unknown avg `-0.0054` n `793`
- 24h: commodity avg `0.1576` n `12`; crypto_alt avg `8.8892` n `230`; crypto_major avg `8.4615` n `8`; equity avg `0.9107` n `121`; fx avg `-0.0961` n `6`; index avg `0.1205` n `25`; metal avg `0.4413` n `20`; unknown avg `1.4208` n `777`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.2227`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1859`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1762`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1717`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1306`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1012`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1003`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0978`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0961`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0883`, n `668`, weak_sample_signal
