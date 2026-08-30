# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-30T13:52:29.574263+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0049` n `12`; crypto_alt avg `0.1523` n `231`; crypto_major avg `0.2474` n `8`; equity avg `0.0191` n `128`; fx avg `0.0` n `6`; index avg `0.0018` n `26`; metal avg `0.0182` n `20`; unknown avg `0.0083` n `793`
- 1h: commodity avg `0.0072` n `12`; crypto_alt avg `0.293` n `231`; crypto_major avg `0.5044` n `8`; equity avg `0.0109` n `128`; fx avg `-0.0028` n `6`; index avg `0.0114` n `26`; metal avg `0.0275` n `20`; unknown avg `-0.0911` n `793`
- 4h: commodity avg `0.0184` n `12`; crypto_alt avg `1.2517` n `231`; crypto_major avg `1.1727` n `8`; equity avg `0.0527` n `128`; fx avg `-0.0017` n `6`; index avg `0.0242` n `26`; metal avg `0.0262` n `20`; unknown avg `-0.0308` n `789`
- 24h: commodity avg `-0.0158` n `12`; crypto_alt avg `1.9062` n `231`; crypto_major avg `1.6103` n `8`; equity avg `0.3149` n `128`; fx avg `0.0154` n `6`; index avg `0.1025` n `26`; metal avg `0.105` n `20`; unknown avg `0.1071` n `730`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.115`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1084`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1034`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1026`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0957`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0929`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0912`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.082`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0741`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0624`, n `668`, weak_sample_signal
