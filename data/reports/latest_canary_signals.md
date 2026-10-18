# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-18T04:37:28.793576+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.003` n `13`; crypto_alt avg `-0.2385` n `237`; crypto_major avg `-0.1616` n `8`; equity avg `-0.0118` n `151`; fx avg `0.0` n `6`; index avg `0.0047` n `26`; metal avg `0.0008` n `20`; unknown avg `-0.0402` n `1193`
- 1h: commodity avg `-0.0229` n `13`; crypto_alt avg `-0.2503` n `237`; crypto_major avg `-0.155` n `8`; equity avg `0.044` n `151`; fx avg `0.001` n `6`; index avg `0.019` n `26`; metal avg `0.0048` n `20`; unknown avg `-0.0784` n `1185`
- 4h: commodity avg `0.0655` n `13`; crypto_alt avg `-0.0177` n `237`; crypto_major avg `0.4915` n `8`; equity avg `0.2808` n `151`; fx avg `-0.0222` n `6`; index avg `0.0556` n `26`; metal avg `0.0262` n `20`; unknown avg `0.1739` n `1185`
- 24h: commodity avg `-0.1217` n `13`; crypto_alt avg `-2.7723` n `236`; crypto_major avg `-0.6052` n `8`; equity avg `-0.8665` n `151`; fx avg `-0.0467` n `6`; index avg `-0.0832` n `26`; metal avg `-0.0632` n `20`; unknown avg `3.593` n `1051`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1674`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1363`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.109`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1056`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0984`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0906`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0815`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0743`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0722`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0576`, n `668`, weak_sample_signal
