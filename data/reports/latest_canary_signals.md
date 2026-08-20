# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-20T10:22:33.259187+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `2.7957` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_crypto_metal_divergence: score `2.6223` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_commodity_crypto_divergence: score `2.2616` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `-0.0264` n `12`; crypto_alt avg `0.1817` n `230`; crypto_major avg `0.2093` n `8`; equity avg `0.0855` n `121`; fx avg `0.0094` n `6`; index avg `0.0221` n `25`; metal avg `-0.0127` n `20`; unknown avg `0.0965` n `792`
- 1h: commodity avg `-0.0174` n `12`; crypto_alt avg `0.0919` n `230`; crypto_major avg `-0.1404` n `8`; equity avg `0.068` n `121`; fx avg `0.0207` n `6`; index avg `0.0303` n `25`; metal avg `-0.0148` n `20`; unknown avg `0.2211` n `792`
- 4h: commodity avg `0.2802` n `12`; crypto_alt avg `1.9735` n `230`; crypto_major avg `2.5418` n `8`; equity avg `-0.2539` n `121`; fx avg `0.0938` n `6`; index avg `-0.0564` n `25`; metal avg `-0.0805` n `20`; unknown avg `0.4597` n `792`
- 24h: commodity avg `0.1808` n `12`; crypto_alt avg `7.74` n `230`; crypto_major avg `12.7857` n `8`; equity avg `0.7809` n `120`; fx avg `0.2255` n `6`; index avg `0.1427` n `25`; metal avg `0.8753` n `20`; unknown avg `2.5009` n `775`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1914`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1628`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1572`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1474`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1306`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1044`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1038`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0938`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0889`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0886`, n `668`, weak_sample_signal
