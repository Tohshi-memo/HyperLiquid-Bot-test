# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-04T19:07:29.806009+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.005` n `12`; crypto_alt avg `-0.1125` n `229`; crypto_major avg `-0.1004` n `8`; equity avg `0.0064` n `88`; fx avg `0.0005` n `6`; index avg `0.0045` n `25`; metal avg `0.0122` n `20`; unknown avg `-0.1799` n `765`
- 1h: commodity avg `-0.0211` n `12`; crypto_alt avg `-0.3592` n `229`; crypto_major avg `-0.3087` n `8`; equity avg `-0.0511` n `88`; fx avg `0.0031` n `6`; index avg `-0.0056` n `25`; metal avg `-0.0052` n `20`; unknown avg `-0.1388` n `765`
- 4h: commodity avg `-0.0786` n `12`; crypto_alt avg `0.4604` n `229`; crypto_major avg `0.3716` n `8`; equity avg `-0.0025` n `88`; fx avg `-0.0139` n `6`; index avg `-0.026` n `25`; metal avg `0.0115` n `20`; unknown avg `-0.2715` n `765`
- 24h: commodity avg `-0.0009` n `12`; crypto_alt avg `1.213` n `229`; crypto_major avg `1.5164` n `8`; equity avg `0.1708` n `88`; fx avg `-0.017` n `6`; index avg `-0.0728` n `25`; metal avg `0.0459` n `20`; unknown avg `-0.04` n `741`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0943`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0937`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.092`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0906`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.081`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0803`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0738`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0702`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0701`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0661`, n `668`, weak_sample_signal
