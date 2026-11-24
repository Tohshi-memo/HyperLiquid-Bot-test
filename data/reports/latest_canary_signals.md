# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-24T03:52:29.485491+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0251` n `13`; crypto_alt avg `-0.0394` n `239`; crypto_major avg `0.0167` n `8`; equity avg `-0.0745` n `166`; fx avg `-0.0098` n `6`; index avg `0.0027` n `27`; metal avg `-0.031` n `20`; unknown avg `157.6729` n `1266`
- 1h: commodity avg `0.0087` n `13`; crypto_alt avg `-0.0516` n `239`; crypto_major avg `0.2333` n `8`; equity avg `-0.0332` n `166`; fx avg `-0.0058` n `6`; index avg `0.0003` n `27`; metal avg `-0.0983` n `20`; unknown avg `158.7848` n `1258`
- 4h: commodity avg `-0.1225` n `13`; crypto_alt avg `-0.4333` n `239`; crypto_major avg `-0.5487` n `8`; equity avg `-0.1646` n `166`; fx avg `0.0355` n `6`; index avg `0.1955` n `27`; metal avg `-0.1905` n `20`; unknown avg `488.8226` n `1252`
- 24h: commodity avg `-1.2152` n `13`; crypto_alt avg `0.2065` n `239`; crypto_major avg `-0.1245` n `8`; equity avg `4.8374` n `166`; fx avg `-0.2892` n `6`; index avg `0.6367` n `27`; metal avg `0.0677` n `20`; unknown avg `240.4276` n `1044`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1345`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1318`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1282`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1101`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0993`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0962`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0932`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0928`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0924`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0815`, n `668`, weak_sample_signal
