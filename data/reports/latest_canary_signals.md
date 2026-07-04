# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-04T18:46:31.687444+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0018` n `12`; crypto_alt avg `-0.0454` n `229`; crypto_major avg `-0.0137` n `8`; equity avg `-0.0013` n `88`; fx avg `0.0` n `6`; index avg `-0.0055` n `25`; metal avg `-0.0105` n `20`; unknown avg `-0.1098` n `765`
- 1h: commodity avg `-0.0433` n `12`; crypto_alt avg `-0.4383` n `229`; crypto_major avg `-0.4764` n `8`; equity avg `-0.0942` n `88`; fx avg `-0.0103` n `6`; index avg `-0.0097` n `25`; metal avg `-0.0195` n `20`; unknown avg `-0.222` n `765`
- 4h: commodity avg `-0.0325` n `12`; crypto_alt avg `0.7682` n `229`; crypto_major avg `0.5473` n `8`; equity avg `-0.0077` n `88`; fx avg `0.0008` n `6`; index avg `-0.032` n `25`; metal avg `0.0029` n `20`; unknown avg `-0.0623` n `765`
- 24h: commodity avg `-0.0364` n `12`; crypto_alt avg `1.2687` n `229`; crypto_major avg `1.5823` n `8`; equity avg `0.138` n `88`; fx avg `-0.0119` n `6`; index avg `-0.0819` n `25`; metal avg `0.0312` n `20`; unknown avg `0.8114` n `741`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0942`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0929`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0919`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0908`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.081`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0764`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0741`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.069`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0686`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0645`, n `668`, weak_sample_signal
