# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-20T09:35:07.311974+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0068` n `12`; crypto_alt avg `0.0457` n `228`; crypto_major avg `0.1121` n `8`; equity avg `-0.0749` n `78`; fx avg `0.0` n `6`; index avg `-0.0014` n `23`; metal avg `-0.0029` n `18`; unknown avg `-0.0229` n `687`
- 1h: commodity avg `-0.0172` n `12`; crypto_alt avg `0.3212` n `228`; crypto_major avg `0.1897` n `8`; equity avg `-0.1404` n `78`; fx avg `-0.2755` n `6`; index avg `-0.0095` n `23`; metal avg `-0.0121` n `18`; unknown avg `-0.077` n `687`
- 4h: commodity avg `0.012` n `12`; crypto_alt avg `0.3363` n `228`; crypto_major avg `0.2` n `8`; equity avg `-0.111` n `78`; fx avg `0.0235` n `6`; index avg `-0.0354` n `23`; metal avg `-0.0044` n `18`; unknown avg `-0.1075` n `639`
- 24h: commodity avg `0.5067` n `12`; crypto_alt avg `-2.9241` n `228`; crypto_major avg `-3.3963` n `8`; equity avg `1.165` n `78`; fx avg `-0.3724` n `6`; index avg `0.2956` n `23`; metal avg `-4.1072` n `18`; unknown avg `0.0004` n `530`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0973`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0957`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0899`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0775`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0616`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0576`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0568`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0556`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0517`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0506`, n `668`, weak_sample_signal
