# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-10T08:46:01.855379+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.029` n `12`; crypto_alt avg `0.0071` n `229`; crypto_major avg `-0.0485` n `8`; equity avg `0.0655` n `91`; fx avg `-0.0236` n `6`; index avg `0.0091` n `25`; metal avg `0.0046` n `20`; unknown avg `0.0023` n `765`
- 1h: commodity avg `0.1052` n `12`; crypto_alt avg `0.3121` n `229`; crypto_major avg `0.4694` n `8`; equity avg `0.0223` n `91`; fx avg `-0.014` n `6`; index avg `-0.0024` n `25`; metal avg `-0.0847` n `20`; unknown avg `0.1068` n `765`
- 4h: commodity avg `-0.1066` n `12`; crypto_alt avg `0.1276` n `229`; crypto_major avg `0.181` n `8`; equity avg `-0.7639` n `91`; fx avg `-0.1075` n `6`; index avg `-0.1433` n `25`; metal avg `-0.1952` n `20`; unknown avg `1.1665` n `733`
- 24h: commodity avg `-0.8499` n `12`; crypto_alt avg `0.8447` n `229`; crypto_major avg `1.265` n `8`; equity avg `0.1716` n `91`; fx avg `-0.1416` n `6`; index avg `0.1582` n `25`; metal avg `0.0798` n `20`; unknown avg `0.0378` n `732`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1064`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1057`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0902`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0859`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0841`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0815`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0814`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.079`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0757`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0743`, n `668`, weak_sample_signal
