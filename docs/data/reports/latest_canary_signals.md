# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-10T06:06:00.382434+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-1.6003` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0078` n `12`; crypto_alt avg `0.0516` n `228`; crypto_major avg `0.0346` n `8`; equity avg `0.2678` n `74`; fx avg `0.0054` n `6`; index avg `0.1439` n `23`; metal avg `0.4011` n `18`; unknown avg `-0.0041` n `537`
- 1h: commodity avg `-0.1925` n `12`; crypto_alt avg `-0.1672` n `228`; crypto_major avg `-0.1391` n `8`; equity avg `0.2701` n `74`; fx avg `0.0228` n `6`; index avg `0.0803` n `23`; metal avg `0.9444` n `18`; unknown avg `0.017` n `537`
- 4h: commodity avg `-0.6611` n `12`; crypto_alt avg `-1.1095` n `228`; crypto_major avg `-1.1073` n `8`; equity avg `-0.5018` n `74`; fx avg `0.0685` n `6`; index avg `-0.4018` n `23`; metal avg `0.493` n `18`; unknown avg `-0.3336` n `537`
- 24h: commodity avg `-0.8925` n `12`; crypto_alt avg `-2.0612` n `228`; crypto_major avg `-4.2924` n `8`; equity avg `-3.8293` n `74`; fx avg `0.2514` n `6`; index avg `-1.8306` n `23`; metal avg `-2.6224` n `18`; unknown avg `0.2337` n `535`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1108`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0855`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0791`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0691`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0661`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0644`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0615`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0598`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.059`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0532`, n `668`, weak_sample_signal
