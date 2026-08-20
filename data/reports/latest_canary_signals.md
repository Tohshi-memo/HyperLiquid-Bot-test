# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-20T08:37:24.299465+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `3.1529` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_crypto_metal_divergence: score `2.4887` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_crypto_equity_divergence: score `2.2292` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_commodity_crypto_divergence: score `2.2027` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 1h_crypto_metal_divergence: score `1.5376` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.1034` n `12`; crypto_alt avg `0.1352` n `230`; crypto_major avg `0.4737` n `8`; equity avg `-0.3079` n `121`; fx avg `0.0073` n `6`; index avg `-0.0573` n `25`; metal avg `-0.0487` n `20`; unknown avg `-0.0369` n `792`
- 1h: commodity avg `0.1335` n `12`; crypto_alt avg `1.2865` n `230`; crypto_major avg `1.5951` n `8`; equity avg `-0.6341` n `121`; fx avg `0.0154` n `6`; index avg `-0.1093` n `25`; metal avg `0.0575` n `20`; unknown avg `0.0201` n `792`
- 4h: commodity avg `0.2611` n `12`; crypto_alt avg `1.7777` n `230`; crypto_major avg `2.4638` n `8`; equity avg `-0.6891` n `121`; fx avg `0.0313` n `6`; index avg `-0.1232` n `25`; metal avg `-0.0249` n `20`; unknown avg `0.3761` n `776`
- 24h: commodity avg `0.269` n `12`; crypto_alt avg `6.8251` n `230`; crypto_major avg `11.8735` n `8`; equity avg `-0.3418` n `120`; fx avg `0.1501` n `6`; index avg `-0.0201` n `25`; metal avg `0.9353` n `20`; unknown avg `2.0479` n `773`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1958`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1622`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1536`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1417`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1327`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1082`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1082`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1049`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0899`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0887`, n `668`, weak_sample_signal
