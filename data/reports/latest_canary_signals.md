# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-29T19:22:24.125769+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0068` n `12`; crypto_alt avg `0.0179` n `231`; crypto_major avg `-0.0121` n `8`; equity avg `0.0154` n `128`; fx avg `0.0046` n `6`; index avg `-0.0002` n `26`; metal avg `-0.0042` n `20`; unknown avg `0.0932` n `792`
- 1h: commodity avg `0.0008` n `12`; crypto_alt avg `0.2059` n `231`; crypto_major avg `0.2349` n `8`; equity avg `0.0702` n `128`; fx avg `-0.0139` n `6`; index avg `0.0229` n `26`; metal avg `0.0029` n `20`; unknown avg `-0.0075` n `792`
- 4h: commodity avg `0.0163` n `12`; crypto_alt avg `0.1156` n `231`; crypto_major avg `0.2715` n `8`; equity avg `0.073` n `128`; fx avg `-0.0103` n `6`; index avg `0.0103` n `26`; metal avg `0.0391` n `20`; unknown avg `-0.1265` n `788`
- 24h: commodity avg `0.0475` n `12`; crypto_alt avg `1.0226` n `231`; crypto_major avg `1.2646` n `8`; equity avg `0.3208` n `128`; fx avg `-0.0477` n `6`; index avg `0.0402` n `26`; metal avg `0.1492` n `20`; unknown avg `0.2016` n `728`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.2259`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1399`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1323`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0946`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.083`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0708`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0689`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0617`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0594`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0575`, n `668`, weak_sample_signal
