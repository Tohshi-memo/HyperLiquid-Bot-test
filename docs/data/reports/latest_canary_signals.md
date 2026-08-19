# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-19T19:57:00.850035+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.352` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_equity_divergence: score `2.0085` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_crypto_metal_divergence: score `1.8547` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_crypto_metal_divergence: score `1.6117` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0435` n `12`; crypto_alt avg `0.2008` n `230`; crypto_major avg `0.1913` n `8`; equity avg `0.0575` n `121`; fx avg `0.0052` n `6`; index avg `-0.014` n `25`; metal avg `0.0303` n `20`; unknown avg `-0.0863` n `792`
- 1h: commodity avg `-0.0486` n `12`; crypto_alt avg `0.6964` n `230`; crypto_major avg `1.7185` n `8`; equity avg `0.4309` n `121`; fx avg `-0.0036` n `6`; index avg `-0.0175` n `25`; metal avg `0.1068` n `20`; unknown avg `0.3895` n `792`
- 4h: commodity avg `-0.3115` n `12`; crypto_alt avg `0.9731` n `230`; crypto_major avg `2.0405` n `8`; equity avg `0.032` n `121`; fx avg `-0.0073` n `6`; index avg `-0.0654` n `25`; metal avg `0.1858` n `20`; unknown avg `0.3549` n `792`
- 24h: commodity avg `-0.0452` n `12`; crypto_alt avg `3.7195` n `230`; crypto_major avg `6.7702` n `8`; equity avg `-0.1113` n `120`; fx avg `-0.1995` n `6`; index avg `-0.0236` n `25`; metal avg `1.1152` n `20`; unknown avg `0.8627` n `757`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1853`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1745`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1544`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1443`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1428`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1255`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1223`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.119`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1144`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1012`, n `668`, weak_sample_signal
