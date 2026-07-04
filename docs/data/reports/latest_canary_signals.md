# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-04T23:22:25.551996+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0112` n `12`; crypto_alt avg `-0.1523` n `229`; crypto_major avg `-0.2287` n `8`; equity avg `-0.0642` n `88`; fx avg `0.0046` n `6`; index avg `0.0063` n `25`; metal avg `-0.0003` n `20`; unknown avg `0.3856` n `765`
- 1h: commodity avg `0.0327` n `12`; crypto_alt avg `-0.2769` n `229`; crypto_major avg `-0.2721` n `8`; equity avg `-0.0233` n `88`; fx avg `0.0148` n `6`; index avg `0.0143` n `25`; metal avg `-0.0018` n `20`; unknown avg `0.001` n `765`
- 4h: commodity avg `0.0493` n `12`; crypto_alt avg `-0.7184` n `229`; crypto_major avg `-0.5836` n `8`; equity avg `0.0111` n `88`; fx avg `-0.0132` n `6`; index avg `0.0403` n `25`; metal avg `0.0127` n `20`; unknown avg `13.9563` n `765`
- 24h: commodity avg `0.0475` n `12`; crypto_alt avg `-0.0871` n `229`; crypto_major avg `0.3236` n `8`; equity avg `0.2342` n `88`; fx avg `-0.0098` n `6`; index avg `0.0119` n `25`; metal avg `0.0667` n `20`; unknown avg `-0.6266` n `741`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0982`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0968`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0921`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0889`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0863`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.084`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0772`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0745`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0726`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0578`, n `668`, weak_sample_signal
