# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-03T19:22:30.707679+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0339` n `12`; crypto_alt avg `0.2793` n `229`; crypto_major avg `0.321` n `8`; equity avg `0.1222` n `88`; fx avg `-0.001` n `6`; index avg `-0.0067` n `25`; metal avg `-0.0102` n `20`; unknown avg `0.0246` n `765`
- 1h: commodity avg `0.0137` n `12`; crypto_alt avg `0.3056` n `229`; crypto_major avg `0.4067` n `8`; equity avg `0.0795` n `88`; fx avg `0.0019` n `6`; index avg `-0.0175` n `25`; metal avg `-0.0138` n `20`; unknown avg `-0.181` n `765`
- 4h: commodity avg `0.0862` n `12`; crypto_alt avg `0.4239` n `229`; crypto_major avg `0.6807` n `8`; equity avg `0.1895` n `88`; fx avg `-0.0212` n `6`; index avg `0.0052` n `25`; metal avg `-0.0541` n `20`; unknown avg `2.1948` n `765`
- 24h: commodity avg `0.2276` n `12`; crypto_alt avg `3.0224` n `229`; crypto_major avg `2.9532` n `8`; equity avg `2.6996` n `88`; fx avg `-0.0511` n `6`; index avg `0.6912` n `25`; metal avg `0.7299` n `20`; unknown avg `9.0085` n `739`

## Correlations

- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1031`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0992`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.082`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0818`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0749`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0739`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0716`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0683`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0661`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.056`, n `668`, weak_sample_signal
