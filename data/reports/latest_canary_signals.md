# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-18T17:52:25.931289+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0021` n `13`; crypto_alt avg `-0.2055` n `237`; crypto_major avg `-0.1084` n `8`; equity avg `-0.01` n `151`; fx avg `-0.002` n `6`; index avg `0.0031` n `26`; metal avg `-0.0018` n `20`; unknown avg `0.8127` n `1192`
- 1h: commodity avg `-0.0023` n `13`; crypto_alt avg `-0.1572` n `237`; crypto_major avg `0.1045` n `8`; equity avg `-0.1093` n `151`; fx avg `0.0004` n `6`; index avg `-0.0215` n `26`; metal avg `0.0032` n `20`; unknown avg `-0.3806` n `1190`
- 4h: commodity avg `0.0158` n `13`; crypto_alt avg `-1.1939` n `237`; crypto_major avg `-0.7617` n `8`; equity avg `-0.3659` n `151`; fx avg `0.0048` n `6`; index avg `-0.0656` n `26`; metal avg `-0.0255` n `20`; unknown avg `-0.8713` n `1159`
- 24h: commodity avg `-0.0075` n `13`; crypto_alt avg `-2.9042` n `236`; crypto_major avg `-1.127` n `8`; equity avg `-0.8947` n `151`; fx avg `-0.0126` n `6`; index avg `-0.1088` n `26`; metal avg `-0.0375` n `20`; unknown avg `0.4325` n `1015`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.2108`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1407`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1301`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1135`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1091`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0817`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0812`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0802`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0652`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.063`, n `668`, weak_sample_signal
