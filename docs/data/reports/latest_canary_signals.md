# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-20T17:07:26.497622+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `3.4508` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_commodity_crypto_divergence: score `3.3258` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.8859` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0015` n `12`; crypto_alt avg `0.0811` n `230`; crypto_major avg `0.3839` n `8`; equity avg `-0.067` n `121`; fx avg `0.004` n `6`; index avg `-0.0223` n `25`; metal avg `-0.0008` n `20`; unknown avg `0.6514` n `792`
- 1h: commodity avg `-0.106` n `12`; crypto_alt avg `0.6453` n `230`; crypto_major avg `1.4327` n `8`; equity avg `0.1093` n `121`; fx avg `0.0131` n `6`; index avg `0.0234` n `25`; metal avg `-0.0293` n `20`; unknown avg `1.0386` n `792`
- 4h: commodity avg `-0.1528` n `12`; crypto_alt avg `1.6608` n `230`; crypto_major avg `3.173` n `8`; equity avg `-0.2778` n `121`; fx avg `0.0138` n `6`; index avg `0.0365` n `25`; metal avg `0.2871` n `20`; unknown avg `1.1202` n `792`
- 24h: commodity avg `-0.1636` n `12`; crypto_alt avg `6.6989` n `230`; crypto_major avg `11.4336` n `8`; equity avg `-0.4643` n `121`; fx avg `0.1859` n `6`; index avg `-0.0072` n `25`; metal avg `0.3123` n `20`; unknown avg `3.676` n `776`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.2139`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1869`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1779`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1738`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1411`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1073`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1043`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.103`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1026`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0975`, n `668`, weak_sample_signal
