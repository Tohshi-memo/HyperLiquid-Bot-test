# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-05T06:22:27.553485+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0032` n `12`; crypto_alt avg `-0.0228` n `229`; crypto_major avg `0.0706` n `8`; equity avg `0.0171` n `88`; fx avg `0.0` n `6`; index avg `0.0324` n `25`; metal avg `0.004` n `20`; unknown avg `-0.0083` n `763`
- 1h: commodity avg `-0.0063` n `12`; crypto_alt avg `-0.3186` n `229`; crypto_major avg `0.0299` n `8`; equity avg `0.0205` n `88`; fx avg `0.0005` n `6`; index avg `0.0098` n `25`; metal avg `0.0041` n `20`; unknown avg `-0.0635` n `731`
- 4h: commodity avg `-0.015` n `12`; crypto_alt avg `-0.4634` n `229`; crypto_major avg `-0.172` n `8`; equity avg `0.1343` n `88`; fx avg `-0.0046` n `6`; index avg `0.0437` n `25`; metal avg `-0.0031` n `20`; unknown avg `-0.0187` n `731`
- 24h: commodity avg `0.0462` n `12`; crypto_alt avg `-0.8432` n `229`; crypto_major avg `-0.7043` n `8`; equity avg `0.2163` n `88`; fx avg `-0.0176` n `6`; index avg `0.0659` n `25`; metal avg `0.0731` n `20`; unknown avg `-1.0036` n `725`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1017`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0997`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0954`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0944`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.09`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0885`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.088`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0759`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0758`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0675`, n `668`, weak_sample_signal
