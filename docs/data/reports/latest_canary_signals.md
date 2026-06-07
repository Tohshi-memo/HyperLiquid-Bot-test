# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-07T18:52:25.347109+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.031` n `12`; crypto_alt avg `-0.2404` n `228`; crypto_major avg `-0.2727` n `8`; equity avg `-0.0731` n `74`; fx avg `-0.0013` n `6`; index avg `-0.0771` n `23`; metal avg `-0.0532` n `18`; unknown avg `-0.1826` n `516`
- 1h: commodity avg `0.1354` n `12`; crypto_alt avg `-0.3238` n `228`; crypto_major avg `-0.1226` n `8`; equity avg `-0.2455` n `74`; fx avg `-0.0085` n `6`; index avg `-0.1883` n `23`; metal avg `-0.1018` n `18`; unknown avg `0.0898` n `516`
- 4h: commodity avg `0.3531` n `12`; crypto_alt avg `-0.4552` n `228`; crypto_major avg `0.3322` n `8`; equity avg `-0.0749` n `74`; fx avg `-0.0053` n `6`; index avg `-0.3272` n `23`; metal avg `0.0396` n `18`; unknown avg `-2.415` n `516`
- 24h: commodity avg `0.3053` n `12`; crypto_alt avg `2.9165` n `228`; crypto_major avg `3.8367` n `8`; equity avg `1.7922` n `74`; fx avg `-0.1094` n `6`; index avg `0.3216` n `23`; metal avg `0.5338` n `18`; unknown avg `-4.7834` n `505`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1372`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1297`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1238`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0966`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0793`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0765`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0642`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0638`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0566`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0551`, n `668`, weak_sample_signal
