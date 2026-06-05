# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-05T16:22:21.916268+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `2.2424` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `2.1032` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.2387` n `12`; crypto_alt avg `1.4901` n `228`; crypto_major avg `1.7398` n `8`; equity avg `-0.0598` n `74`; fx avg `0.0001` n `6`; index avg `-0.0964` n `23`; metal avg `-0.0089` n `18`; unknown avg `0.8831` n `424`
- 1h: commodity avg `-0.5663` n `12`; crypto_alt avg `0.3416` n `228`; crypto_major avg `0.6716` n `8`; equity avg `-0.8269` n `74`; fx avg `-0.0598` n `6`; index avg `-0.5745` n `23`; metal avg `-0.2851` n `18`; unknown avg `1.2384` n `424`
- 4h: commodity avg `-1.2132` n `12`; crypto_alt avg `-1.6113` n `228`; crypto_major avg `-1.6123` n `8`; equity avg `-3.7155` n `74`; fx avg `-0.2207` n `6`; index avg `-1.9883` n `23`; metal avg `-3.8547` n `18`; unknown avg `0.0809` n `424`
- 24h: commodity avg `-1.4697` n `12`; crypto_alt avg `-8.2` n `228`; crypto_major avg `-5.8833` n `8`; equity avg `-5.5039` n `74`; fx avg `-0.0541` n `6`; index avg `-2.663` n `23`; metal avg `-4.1223` n `18`; unknown avg `-0.0954` n `404`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1228`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1174`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0982`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0906`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0726`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.071`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0595`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0585`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0566`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0549`, n `668`, weak_sample_signal
