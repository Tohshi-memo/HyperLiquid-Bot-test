# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-20T08:52:27.789864+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `3.1464` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_crypto_metal_divergence: score `2.5479` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_crypto_equity_divergence: score `2.29` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_commodity_crypto_divergence: score `2.1445` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 1h_crypto_metal_divergence: score `1.7348` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0194` n `12`; crypto_alt avg `0.1773` n `230`; crypto_major avg `0.2687` n `8`; equity avg `0.0467` n `121`; fx avg `0.0313` n `6`; index avg `-0.0084` n `25`; metal avg `-0.0304` n `20`; unknown avg `0.0303` n `792`
- 1h: commodity avg `0.1468` n `12`; crypto_alt avg `1.2641` n `230`; crypto_major avg `1.7396` n `8`; equity avg `-0.5504` n `121`; fx avg `0.0517` n `6`; index avg `-0.1121` n `25`; metal avg `0.0048` n `20`; unknown avg `0.0689` n `792`
- 4h: commodity avg `0.3072` n `12`; crypto_alt avg `1.7963` n `230`; crypto_major avg `2.4517` n `8`; equity avg `-0.6947` n `121`; fx avg `0.0664` n `6`; index avg `-0.1361` n `25`; metal avg `-0.0962` n `20`; unknown avg `0.4102` n `776`
- 24h: commodity avg `0.2432` n `12`; crypto_alt avg `7.0415` n `230`; crypto_major avg `12.1106` n `8`; equity avg `-0.4155` n `120`; fx avg `0.1705` n `6`; index avg `-0.0291` n `25`; metal avg `0.9253` n `20`; unknown avg `2.1138` n `773`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1949`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1621`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1555`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1438`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1335`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1069`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1066`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1014`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0906`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0867`, n `668`, weak_sample_signal
