# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-14T06:22:28.915399+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0037` n `13`; crypto_alt avg `0.143` n `235`; crypto_major avg `0.0826` n `8`; equity avg `0.1531` n `151`; fx avg `-0.0051` n `6`; index avg `0.0555` n `26`; metal avg `0.0391` n `20`; unknown avg `0.3244` n `1135`
- 1h: commodity avg `-0.0098` n `13`; crypto_alt avg `-0.2802` n `235`; crypto_major avg `-0.0801` n `8`; equity avg `-0.3819` n `151`; fx avg `0.0173` n `6`; index avg `-0.0713` n `26`; metal avg `-0.0268` n `20`; unknown avg `0.2969` n `1117`
- 4h: commodity avg `-0.0788` n `13`; crypto_alt avg `-0.4785` n `235`; crypto_major avg `-0.1547` n `8`; equity avg `-0.7605` n `151`; fx avg `0.0038` n `6`; index avg `-0.1127` n `26`; metal avg `-0.0013` n `20`; unknown avg `0.3355` n `1111`
- 24h: commodity avg `0.9875` n `13`; crypto_alt avg `-1.1851` n `235`; crypto_major avg `-0.5737` n `8`; equity avg `-0.1426` n `151`; fx avg `0.0244` n `6`; index avg `0.0169` n `26`; metal avg `-0.3208` n `20`; unknown avg `0.279` n `979`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1564`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1387`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1209`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1208`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.114`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1006`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0866`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0812`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0752`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0728`, n `666`, weak_sample_signal
