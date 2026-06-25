# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-25T20:22:31.127554+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0273` n `12`; crypto_alt avg `0.2977` n `228`; crypto_major avg `0.0743` n `8`; equity avg `0.14` n `86`; fx avg `0.0041` n `6`; index avg `0.0157` n `23`; metal avg `0.0078` n `20`; unknown avg `0.4392` n `765`
- 1h: commodity avg `-0.0921` n `12`; crypto_alt avg `0.7803` n `228`; crypto_major avg `0.8871` n `8`; equity avg `0.7442` n `86`; fx avg `-0.0033` n `6`; index avg `0.1126` n `23`; metal avg `-0.0677` n `20`; unknown avg `0.4391` n `765`
- 4h: commodity avg `0.0034` n `12`; crypto_alt avg `-0.3269` n `228`; crypto_major avg `0.2603` n `8`; equity avg `0.0062` n `86`; fx avg `0.0095` n `6`; index avg `-0.0` n `23`; metal avg `-0.2446` n `20`; unknown avg `0.2355` n `765`
- 24h: commodity avg `0.5056` n `12`; crypto_alt avg `-1.1666` n `228`; crypto_major avg `-1.0444` n `8`; equity avg `-1.2582` n `86`; fx avg `0.0879` n `6`; index avg `0.0544` n `23`; metal avg `0.3978` n `20`; unknown avg `0.3728` n `700`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1823`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1194`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1102`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1013`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0896`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0859`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0838`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0827`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0601`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0599`, n `668`, weak_sample_signal
