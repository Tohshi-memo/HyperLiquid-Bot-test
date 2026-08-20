# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-20T12:07:33.180359+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `2.5901` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_crypto_metal_divergence: score `1.6982` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0396` n `12`; crypto_alt avg `-0.3378` n `230`; crypto_major avg `-0.4227` n `8`; equity avg `-0.3037` n `121`; fx avg `-0.006` n `6`; index avg `-0.0565` n `25`; metal avg `-0.1362` n `20`; unknown avg `-0.049` n `792`
- 1h: commodity avg `0.0498` n `12`; crypto_alt avg `-0.0325` n `230`; crypto_major avg `-0.0543` n `8`; equity avg `-0.8703` n `121`; fx avg `0.0047` n `6`; index avg `-0.1766` n `25`; metal avg `-0.3216` n `20`; unknown avg `0.1634` n `792`
- 4h: commodity avg `0.348` n `12`; crypto_alt avg `1.3461` n `230`; crypto_major avg `1.4167` n `8`; equity avg `-1.1734` n `121`; fx avg `0.0513` n `6`; index avg `-0.2314` n `25`; metal avg `-0.2815` n `20`; unknown avg `0.2012` n `792`
- 24h: commodity avg `0.2234` n `12`; crypto_alt avg `7.4257` n `230`; crypto_major avg `12.1274` n `8`; equity avg `-0.4486` n `120`; fx avg `0.2353` n `6`; index avg `-0.1044` n `25`; metal avg `0.5687` n `20`; unknown avg `2.4623` n `776`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1894`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.166`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1568`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1529`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1415`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1172`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1031`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0998`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0994`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0899`, n `668`, weak_sample_signal
