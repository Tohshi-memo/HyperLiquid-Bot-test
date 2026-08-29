# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-29T19:52:28.188662+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0054` n `12`; crypto_alt avg `-0.042` n `231`; crypto_major avg `-0.0408` n `8`; equity avg `0.0026` n `128`; fx avg `-0.0018` n `6`; index avg `0.0081` n `26`; metal avg `-0.0031` n `20`; unknown avg `0.1986` n `792`
- 1h: commodity avg `-0.0088` n `12`; crypto_alt avg `-0.061` n `231`; crypto_major avg `-0.047` n `8`; equity avg `0.1027` n `128`; fx avg `-0.016` n `6`; index avg `0.0292` n `26`; metal avg `-0.0017` n `20`; unknown avg `0.735` n `792`
- 4h: commodity avg `0.0362` n `12`; crypto_alt avg `-0.0867` n `231`; crypto_major avg `0.219` n `8`; equity avg `0.1541` n `128`; fx avg `-0.021` n `6`; index avg `0.0316` n `26`; metal avg `0.0197` n `20`; unknown avg `-0.1525` n `790`
- 24h: commodity avg `0.0018` n `12`; crypto_alt avg `1.0137` n `231`; crypto_major avg `1.2868` n `8`; equity avg `0.3645` n `128`; fx avg `-0.0544` n `6`; index avg `0.0675` n `26`; metal avg `0.1639` n `20`; unknown avg `0.1951` n `728`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.2287`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1445`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1341`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0984`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.083`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.074`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0712`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0609`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0608`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0574`, n `668`, weak_sample_signal
