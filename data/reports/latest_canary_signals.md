# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-09T17:37:26.340950+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0023` n `12`; crypto_alt avg `0.0247` n `230`; crypto_major avg `-0.0077` n `8`; equity avg `-0.0056` n `112`; fx avg `-0.0052` n `6`; index avg `-0.0022` n `25`; metal avg `0.0002` n `20`; unknown avg `-0.01` n `785`
- 1h: commodity avg `0.0154` n `12`; crypto_alt avg `0.1214` n `230`; crypto_major avg `-0.012` n `8`; equity avg `0.0363` n `112`; fx avg `-0.008` n `6`; index avg `0.0029` n `25`; metal avg `-0.0088` n `20`; unknown avg `-0.0997` n `785`
- 4h: commodity avg `-0.055` n `12`; crypto_alt avg `0.7341` n `230`; crypto_major avg `0.3346` n `8`; equity avg `0.1026` n `112`; fx avg `0.011` n `6`; index avg `0.0254` n `25`; metal avg `0.023` n `20`; unknown avg `-0.0941` n `785`
- 24h: commodity avg `0.018` n `12`; crypto_alt avg `1.1781` n `230`; crypto_major avg `0.0269` n `8`; equity avg `0.2332` n `112`; fx avg `-0.0015` n `6`; index avg `0.0262` n `25`; metal avg `0.0755` n `20`; unknown avg `0.4231` n `752`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1487`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1078`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1008`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1001`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0831`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.071`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0654`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0639`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0617`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0555`, n `668`, weak_sample_signal
