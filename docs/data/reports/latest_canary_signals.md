# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-20T11:57:49.963240+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `3.2969` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_crypto_metal_divergence: score `2.3674` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0232` n `12`; crypto_alt avg `-0.1851` n `230`; crypto_major avg `-0.4078` n `8`; equity avg `-0.3938` n `121`; fx avg `0.0053` n `6`; index avg `-0.0666` n `25`; metal avg `-0.144` n `20`; unknown avg `0.0628` n `792`
- 1h: commodity avg `0.1237` n `12`; crypto_alt avg `0.2217` n `230`; crypto_major avg `0.24` n `8`; equity avg `-0.8297` n `121`; fx avg `0.0124` n `6`; index avg `-0.1736` n `25`; metal avg `-0.1982` n `20`; unknown avg `0.3685` n `792`
- 4h: commodity avg `0.3075` n `12`; crypto_alt avg `2.0238` n `230`; crypto_major avg `2.2563` n `8`; equity avg `-1.0406` n `121`; fx avg `0.0714` n `6`; index avg `-0.1978` n `25`; metal avg `-0.1111` n `20`; unknown avg `0.648` n `792`
- 24h: commodity avg `0.28` n `12`; crypto_alt avg `7.7959` n `230`; crypto_major avg `12.5902` n `8`; equity avg `-0.0147` n `120`; fx avg `0.2275` n `6`; index avg `-0.0095` n `25`; metal avg `0.7467` n `20`; unknown avg `2.8516` n `776`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1894`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1661`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1577`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1536`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1365`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1118`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.103`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.095`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0895`, n `668`, weak_sample_signal
