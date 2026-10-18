# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-18T10:06:48.301453+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0034` n `13`; crypto_alt avg `-0.1761` n `237`; crypto_major avg `-0.1104` n `8`; equity avg `-0.0321` n `151`; fx avg `-0.0088` n `6`; index avg `-0.0031` n `26`; metal avg `-0.0006` n `20`; unknown avg `0.0016` n `1191`
- 1h: commodity avg `0.0768` n `13`; crypto_alt avg `0.1509` n `237`; crypto_major avg `0.1251` n `8`; equity avg `-0.0019` n `151`; fx avg `0.0041` n `6`; index avg `0.0215` n `26`; metal avg `0.0129` n `20`; unknown avg `-0.0359` n `1159`
- 4h: commodity avg `0.0811` n `13`; crypto_alt avg `0.3531` n `237`; crypto_major avg `0.4208` n `8`; equity avg `0.3026` n `151`; fx avg `-0.0061` n `6`; index avg `0.0634` n `26`; metal avg `0.0172` n `20`; unknown avg `1.2454` n `1079`
- 24h: commodity avg `0.103` n `13`; crypto_alt avg `-2.0375` n `236`; crypto_major avg `-0.3079` n `8`; equity avg `-0.6098` n `151`; fx avg `-0.052` n `6`; index avg `-0.0656` n `26`; metal avg `-0.037` n `20`; unknown avg `4.4148` n `1033`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1962`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.135`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1264`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1133`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1037`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0887`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0806`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0747`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0675`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0581`, n `668`, weak_sample_signal
