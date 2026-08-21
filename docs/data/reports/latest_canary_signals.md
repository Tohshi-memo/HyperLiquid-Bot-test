# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-21T10:07:28.075493+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `1.6764` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0975` n `12`; crypto_alt avg `-0.1154` n `230`; crypto_major avg `-0.5019` n `8`; equity avg `0.0202` n `121`; fx avg `0.0022` n `6`; index avg `0.019` n `25`; metal avg `-0.0269` n `20`; unknown avg `0.0585` n `793`
- 1h: commodity avg `0.2075` n `12`; crypto_alt avg `1.0333` n `230`; crypto_major avg `0.9685` n `8`; equity avg `0.2976` n `121`; fx avg `0.0313` n `6`; index avg `0.0219` n `25`; metal avg `-0.1376` n `20`; unknown avg `0.1156` n `793`
- 4h: commodity avg `0.2271` n `12`; crypto_alt avg `2.2287` n `230`; crypto_major avg `1.869` n `8`; equity avg `0.7899` n `121`; fx avg `-0.0167` n `6`; index avg `0.0503` n `25`; metal avg `0.1926` n `20`; unknown avg `0.3494` n `793`
- 24h: commodity avg `0.1854` n `12`; crypto_alt avg `6.8714` n `230`; crypto_major avg `6.9526` n `8`; equity avg `0.5806` n `121`; fx avg `-0.0702` n `6`; index avg `0.0255` n `25`; metal avg `0.7928` n `20`; unknown avg `2.5414` n `776`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.2173`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.2153`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.2071`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1878`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1134`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1114`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1085`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0899`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.086`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0851`, n `668`, weak_sample_signal
