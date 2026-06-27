# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-27T08:52:27.296143+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.006` n `12`; crypto_alt avg `0.1163` n `228`; crypto_major avg `0.0605` n `8`; equity avg `-0.0195` n `88`; fx avg `0.0062` n `6`; index avg `0.0047` n `23`; metal avg `-0.0046` n `20`; unknown avg `-0.0864` n `764`
- 1h: commodity avg `-0.0198` n `12`; crypto_alt avg `-0.1897` n `228`; crypto_major avg `-0.0756` n `8`; equity avg `0.0251` n `88`; fx avg `0.0345` n `6`; index avg `-0.0053` n `23`; metal avg `-0.0017` n `20`; unknown avg `0.0625` n `764`
- 4h: commodity avg `0.0454` n `12`; crypto_alt avg `-0.2029` n `228`; crypto_major avg `-0.1159` n `8`; equity avg `0.1648` n `88`; fx avg `0.0172` n `6`; index avg `0.0062` n `23`; metal avg `-0.0141` n `20`; unknown avg `-0.1082` n `716`
- 24h: commodity avg `0.0863` n `12`; crypto_alt avg `1.0598` n `228`; crypto_major avg `0.7456` n `8`; equity avg `1.7701` n `87`; fx avg `0.0287` n `6`; index avg `0.0695` n `23`; metal avg `0.6153` n `20`; unknown avg `-0.1291` n `700`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2054`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1603`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1353`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1079`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0998`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0919`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0889`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0839`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0802`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0782`, n `668`, weak_sample_signal
