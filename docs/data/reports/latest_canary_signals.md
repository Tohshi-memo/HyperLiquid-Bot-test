# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-22T07:07:36.605556+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0236` n `13`; crypto_alt avg `-0.1808` n `239`; crypto_major avg `0.0675` n `8`; equity avg `-0.0514` n `166`; fx avg `-0.0014` n `6`; index avg `-0.0008` n `27`; metal avg `0.0129` n `20`; unknown avg `0.3695` n `1255`
- 1h: commodity avg `-0.031` n `13`; crypto_alt avg `-0.1765` n `239`; crypto_major avg `-0.0038` n `8`; equity avg `-0.0359` n `166`; fx avg `-0.0014` n `6`; index avg `0.0044` n `27`; metal avg `-0.0009` n `20`; unknown avg `1.4762` n `1253`
- 4h: commodity avg `-0.071` n `13`; crypto_alt avg `-0.0066` n `239`; crypto_major avg `-0.3605` n `8`; equity avg `-0.1731` n `166`; fx avg `-0.0046` n `6`; index avg `0.0011` n `27`; metal avg `-0.0166` n `20`; unknown avg `1.0137` n `1217`
- 24h: commodity avg `-0.0389` n `13`; crypto_alt avg `0.7812` n `239`; crypto_major avg `1.3888` n `8`; equity avg `0.4148` n `166`; fx avg `0.0681` n `6`; index avg `0.0817` n `27`; metal avg `0.0247` n `20`; unknown avg `235.4531` n `1072`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1435`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1312`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1212`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1117`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1112`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1091`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1024`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0989`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0983`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0976`, n `668`, weak_sample_signal
