# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-20T09:07:26.643288+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `3.0404` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_crypto_metal_divergence: score `2.7771` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_commodity_crypto_divergence: score `2.3956` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 1h_crypto_equity_divergence: score `1.8388` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 1h_crypto_metal_divergence: score `1.7144` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0074` n `12`; crypto_alt avg `0.2064` n `230`; crypto_major avg `0.3612` n `8`; equity avg `0.2376` n `121`; fx avg `-0.0048` n `6`; index avg `0.0347` n `25`; metal avg `0.0092` n `20`; unknown avg `0.0101` n `792`
- 1h: commodity avg `0.2194` n `12`; crypto_alt avg `1.1405` n `230`; crypto_major avg `1.6936` n `8`; equity avg `-0.1452` n `121`; fx avg `0.0328` n `6`; index avg `-0.0552` n `25`; metal avg `-0.0208` n `20`; unknown avg `0.0034` n `792`
- 4h: commodity avg `0.2802` n `12`; crypto_alt avg `1.9701` n `230`; crypto_major avg `2.6758` n `8`; equity avg `-0.3646` n `121`; fx avg `0.0631` n `6`; index avg `-0.0667` n `25`; metal avg `-0.1013` n `20`; unknown avg `0.4417` n `776`
- 24h: commodity avg `0.1446` n `12`; crypto_alt avg `7.3318` n `230`; crypto_major avg `12.6082` n `8`; equity avg `-0.0582` n `120`; fx avg `0.1677` n `6`; index avg `0.0124` n `25`; metal avg `0.9447` n `20`; unknown avg `2.3013` n `775`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1941`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1622`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1575`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1458`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1338`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1076`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1075`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0942`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0907`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0866`, n `668`, weak_sample_signal
