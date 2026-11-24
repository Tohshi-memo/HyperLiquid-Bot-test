# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-24T17:52:39.198610+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0767` n `13`; crypto_alt avg `-0.0645` n `239`; crypto_major avg `-0.2446` n `8`; equity avg `-0.1085` n `168`; fx avg `-0.0037` n `6`; index avg `-0.015` n `27`; metal avg `-0.0192` n `20`; unknown avg `0.5896` n `1257`
- 1h: commodity avg `0.0459` n `13`; crypto_alt avg `0.6414` n `239`; crypto_major avg `0.3973` n `8`; equity avg `0.503` n `168`; fx avg `0.0153` n `6`; index avg `0.0787` n `27`; metal avg `-0.0437` n `20`; unknown avg `0.4168` n `1251`
- 4h: commodity avg `0.2528` n `13`; crypto_alt avg `-0.3548` n `239`; crypto_major avg `-0.6141` n `8`; equity avg `-1.2982` n `168`; fx avg `0.0457` n `6`; index avg `0.0023` n `27`; metal avg `-0.5837` n `20`; unknown avg `-0.4205` n `1233`
- 24h: commodity avg `0.3853` n `13`; crypto_alt avg `-3.6945` n `239`; crypto_major avg `-3.7818` n `8`; equity avg `-4.0249` n `167`; fx avg `0.2724` n `6`; index avg `-0.2339` n `27`; metal avg `-1.2044` n `20`; unknown avg `-0.5799` n `1127`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1311`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1299`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1274`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1225`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1065`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1049`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1012`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0961`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0955`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0799`, n `668`, weak_sample_signal
