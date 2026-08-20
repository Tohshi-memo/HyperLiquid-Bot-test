# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-20T18:32:00.684296+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `1.888` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 1h_crypto_metal_divergence: score `-1.7022` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_index_leads_crypto: score `1.6455` - Index perps are stronger than crypto majors; possible risk-on canary.
- 1h_crypto_equity_divergence: score `-1.53` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0918` n `12`; crypto_alt avg `-0.1768` n `230`; crypto_major avg `-0.4997` n `8`; equity avg `-0.0665` n `121`; fx avg `0.0039` n `6`; index avg `-0.0069` n `25`; metal avg `0.0257` n `20`; unknown avg `0.0821` n `792`
- 1h: commodity avg `0.0741` n `12`; crypto_alt avg `-0.9244` n `230`; crypto_major avg `-1.7035` n `8`; equity avg `-0.1735` n `121`; fx avg `0.0153` n `6`; index avg `-0.058` n `25`; metal avg `-0.0013` n `20`; unknown avg `0.4079` n `792`
- 4h: commodity avg `0.1571` n `12`; crypto_alt avg `0.8084` n `230`; crypto_major avg `1.2743` n `8`; equity avg `-0.6137` n `121`; fx avg `0.0447` n `6`; index avg `-0.1241` n `25`; metal avg `0.1712` n `20`; unknown avg `1.8329` n `792`
- 24h: commodity avg `0.3242` n `12`; crypto_alt avg `5.8254` n `230`; crypto_major avg `9.208` n `8`; equity avg `-0.4443` n `121`; fx avg `0.2136` n `6`; index avg `-0.0844` n `25`; metal avg `0.3294` n `20`; unknown avg `3.5816` n `776`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.2189`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1886`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1846`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1768`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1312`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1057`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1044`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1033`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0982`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0982`, n `668`, weak_sample_signal
