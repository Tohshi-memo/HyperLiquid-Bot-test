# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-30T13:16:05.341033+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0068` n `12`; crypto_alt avg `-0.117` n `231`; crypto_major avg `-0.1607` n `8`; equity avg `-0.0083` n `128`; fx avg `0.0` n `6`; index avg `0.0037` n `26`; metal avg `0.0004` n `20`; unknown avg `-0.1145` n `793`
- 1h: commodity avg `0.0437` n `12`; crypto_alt avg `0.2043` n `231`; crypto_major avg `0.089` n `8`; equity avg `-0.0284` n `128`; fx avg `0.0013` n `6`; index avg `0.0237` n `26`; metal avg `0.0234` n `20`; unknown avg `-0.0221` n `793`
- 4h: commodity avg `0.0159` n `12`; crypto_alt avg `0.9813` n `231`; crypto_major avg `0.4521` n `8`; equity avg `0.0003` n `128`; fx avg `0.0011` n `6`; index avg `0.0327` n `26`; metal avg `0.0116` n `20`; unknown avg `0.1516` n `789`
- 24h: commodity avg `-0.0171` n `12`; crypto_alt avg `1.8018` n `231`; crypto_major avg `1.1528` n `8`; equity avg `0.285` n `128`; fx avg `0.0168` n `6`; index avg `0.0753` n `26`; metal avg `0.0789` n `20`; unknown avg `-0.0551` n `730`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1181`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1108`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1065`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1052`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1026`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.094`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0865`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0829`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0655`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0617`, n `668`, weak_sample_signal
