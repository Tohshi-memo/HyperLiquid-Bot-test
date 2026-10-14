# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-14T06:37:36.232338+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0239` n `13`; crypto_alt avg `-0.006` n `235`; crypto_major avg `-0.0166` n `8`; equity avg `0.084` n `151`; fx avg `-0.0123` n `6`; index avg `-0.0093` n `26`; metal avg `-0.0212` n `20`; unknown avg `0.3357` n `1135`
- 1h: commodity avg `-0.0059` n `13`; crypto_alt avg `0.0133` n `235`; crypto_major avg `0.021` n `8`; equity avg `-0.1059` n `151`; fx avg `-0.0147` n `6`; index avg `-0.0506` n `26`; metal avg `-0.0518` n `20`; unknown avg `0.3874` n `1117`
- 4h: commodity avg `-0.1432` n `13`; crypto_alt avg `-0.3115` n `235`; crypto_major avg `-0.0221` n `8`; equity avg `-0.661` n `151`; fx avg `-0.0004` n `6`; index avg `-0.1151` n `26`; metal avg `-0.0277` n `20`; unknown avg `0.4883` n `1111`
- 24h: commodity avg `0.9785` n `13`; crypto_alt avg `-1.3619` n `235`; crypto_major avg `-0.7281` n `8`; equity avg `-0.0367` n `151`; fx avg `0.0248` n `6`; index avg `0.0238` n `26`; metal avg `-0.3134` n `20`; unknown avg `0.4932` n `979`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1566`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.139`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.121`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.121`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1132`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1007`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0876`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0818`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0752`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0717`, n `666`, weak_sample_signal
