# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-20T17:16:28.909811+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `3.3307` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_commodity_crypto_divergence: score `3.0752` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.6093` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0007` n `12`; crypto_alt avg `0.0169` n `230`; crypto_major avg `-0.1505` n `8`; equity avg `-0.1835` n `121`; fx avg `0.0021` n `6`; index avg `-0.0192` n `25`; metal avg `-0.0144` n `20`; unknown avg `0.087` n `792`
- 1h: commodity avg `-0.1002` n `12`; crypto_alt avg `0.8297` n `230`; crypto_major avg `1.28` n `8`; equity avg `-0.1082` n `121`; fx avg `-0.0176` n `6`; index avg `-0.0034` n `25`; metal avg `0.0078` n `20`; unknown avg `1.1701` n `792`
- 4h: commodity avg `-0.159` n `12`; crypto_alt avg `1.7759` n `230`; crypto_major avg `2.9162` n `8`; equity avg `-0.4145` n `121`; fx avg `0.0337` n `6`; index avg `0.0402` n `25`; metal avg `0.3069` n `20`; unknown avg `1.2727` n `792`
- 24h: commodity avg `-0.1214` n `12`; crypto_alt avg `6.9094` n `230`; crypto_major avg `11.5865` n `8`; equity avg `-0.4757` n `121`; fx avg `0.1915` n `6`; index avg `0.0048` n `25`; metal avg `0.3161` n `20`; unknown avg `3.7957` n `776`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.2168`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1907`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1816`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1784`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1442`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1105`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1038`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1037`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1024`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0971`, n `668`, weak_sample_signal
