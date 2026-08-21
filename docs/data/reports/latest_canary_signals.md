# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-21T10:52:27.630813+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `2.019` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `1.6149` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.052` n `12`; crypto_alt avg `0.5203` n `230`; crypto_major avg `0.1968` n `8`; equity avg `0.0355` n `121`; fx avg `-0.0067` n `6`; index avg `-0.0` n `25`; metal avg `-0.0303` n `20`; unknown avg `0.0706` n `793`
- 1h: commodity avg `0.066` n `12`; crypto_alt avg `0.5076` n `230`; crypto_major avg `-0.566` n `8`; equity avg `0.0111` n `121`; fx avg `0.0029` n `6`; index avg `0.0001` n `25`; metal avg `-0.0347` n `20`; unknown avg `0.0702` n `793`
- 4h: commodity avg `0.1285` n `12`; crypto_alt avg `2.8998` n `230`; crypto_major avg `2.1125` n `8`; equity avg `0.4976` n `121`; fx avg `-0.0305` n `6`; index avg `-0.002` n `25`; metal avg `0.0935` n `20`; unknown avg `0.6486` n `793`
- 24h: commodity avg `0.1526` n `12`; crypto_alt avg `7.1937` n `230`; crypto_major avg `6.7784` n `8`; equity avg `0.5114` n `121`; fx avg `-0.0835` n `6`; index avg `-0.0286` n `25`; metal avg `0.7294` n `20`; unknown avg `2.4923` n `776`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.2231`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.2122`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.2053`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1907`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1129`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1123`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.105`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0967`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0892`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0859`, n `668`, weak_sample_signal
