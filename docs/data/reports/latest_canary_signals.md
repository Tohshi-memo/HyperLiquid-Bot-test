# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-30T14:52:25.042791+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0131` n `12`; crypto_alt avg `0.0663` n `231`; crypto_major avg `-0.0115` n `8`; equity avg `-0.0041` n `128`; fx avg `-0.0041` n `6`; index avg `0.01` n `26`; metal avg `-0.0074` n `20`; unknown avg `-0.1229` n `793`
- 1h: commodity avg `-0.0119` n `12`; crypto_alt avg `-0.1237` n `231`; crypto_major avg `-0.1514` n `8`; equity avg `-0.002` n `128`; fx avg `0.0005` n `6`; index avg `-0.0101` n `26`; metal avg `0.0419` n `20`; unknown avg `0.7245` n `793`
- 4h: commodity avg `0.0033` n `12`; crypto_alt avg `0.5492` n `231`; crypto_major avg `0.6945` n `8`; equity avg `0.0248` n `128`; fx avg `-0.0004` n `6`; index avg `0.0325` n `26`; metal avg `0.0659` n `20`; unknown avg `0.5606` n `791`
- 24h: commodity avg `-0.0221` n `12`; crypto_alt avg `1.0082` n `231`; crypto_major avg `0.7845` n `8`; equity avg `0.2655` n `128`; fx avg `0.0099` n `6`; index avg `0.0851` n `26`; metal avg `0.117` n `20`; unknown avg `-0.4185` n `738`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1165`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1109`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1099`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1044`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0951`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0923`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0903`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0834`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0764`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0608`, n `668`, weak_sample_signal
