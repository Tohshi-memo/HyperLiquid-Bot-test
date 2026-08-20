# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-20T17:37:34.414936+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `4.6218` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_commodity_crypto_divergence: score `4.1785` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `3.8427` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0665` n `12`; crypto_alt avg `0.0462` n `230`; crypto_major avg `0.2321` n `8`; equity avg `-0.0509` n `121`; fx avg `-0.0039` n `6`; index avg `-0.0162` n `25`; metal avg `0.0155` n `20`; unknown avg `-0.1345` n `792`
- 1h: commodity avg `0.0373` n `12`; crypto_alt avg `0.6668` n `230`; crypto_major avg `1.0575` n `8`; equity avg `-0.0628` n `121`; fx avg `-0.0063` n `6`; index avg `-0.0365` n `25`; metal avg `0.0156` n `20`; unknown avg `0.8276` n `792`
- 4h: commodity avg `-0.0962` n `12`; crypto_alt avg `2.3857` n `230`; crypto_major avg `4.0823` n `8`; equity avg `-0.5395` n `121`; fx avg `0.0384` n `6`; index avg `-0.0899` n `25`; metal avg `0.2396` n `20`; unknown avg `1.1706` n `792`
- 24h: commodity avg `-0.0016` n `12`; crypto_alt avg `6.9547` n `230`; crypto_major avg `11.7992` n `8`; equity avg `-0.3494` n `121`; fx avg `0.1988` n `6`; index avg `-0.0094` n `25`; metal avg `0.315` n `20`; unknown avg `3.5453` n `776`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.2143`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1907`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1797`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.179`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1473`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1133`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1038`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1033`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1027`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0975`, n `668`, weak_sample_signal
