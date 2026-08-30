# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-30T17:22:27.180925+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0073` n `12`; crypto_alt avg `-0.179` n `231`; crypto_major avg `-0.3641` n `8`; equity avg `-0.0069` n `128`; fx avg `0.0026` n `6`; index avg `0.0009` n `26`; metal avg `-0.0112` n `20`; unknown avg `0.1541` n `793`
- 1h: commodity avg `0.0174` n `12`; crypto_alt avg `0.2142` n `231`; crypto_major avg `-0.1609` n `8`; equity avg `0.0294` n `128`; fx avg `0.0111` n `6`; index avg `0.0169` n `26`; metal avg `0.0056` n `20`; unknown avg `0.059` n `793`
- 4h: commodity avg `0.0263` n `12`; crypto_alt avg `0.3851` n `231`; crypto_major avg `0.4599` n `8`; equity avg `0.159` n `128`; fx avg `0.0121` n `6`; index avg `0.0241` n `26`; metal avg `0.0973` n `20`; unknown avg `0.2555` n `793`
- 24h: commodity avg `0.0348` n `12`; crypto_alt avg `1.7735` n `231`; crypto_major avg `1.1466` n `8`; equity avg `0.4036` n `128`; fx avg `0.0332` n `6`; index avg `0.0977` n `26`; metal avg `0.1289` n `20`; unknown avg `0.0954` n `740`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1271`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1223`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1199`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1154`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1061`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0929`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0852`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0848`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0832`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0606`, n `668`, weak_sample_signal
