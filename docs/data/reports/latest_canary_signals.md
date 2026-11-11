# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-11T19:07:33.449571+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0309` n `13`; crypto_alt avg `-0.201` n `239`; crypto_major avg `-0.2224` n `8`; equity avg `-0.4185` n `161`; fx avg `0.0174` n `6`; index avg `-0.0322` n `27`; metal avg `-0.0197` n `20`; unknown avg `18.9027` n `1258`
- 1h: commodity avg `-0.0247` n `13`; crypto_alt avg `-0.5738` n `239`; crypto_major avg `-0.419` n `8`; equity avg `-0.344` n `161`; fx avg `0.0193` n `6`; index avg `0.0103` n `27`; metal avg `-0.0538` n `20`; unknown avg `18.8076` n `1256`
- 4h: commodity avg `-0.1721` n `13`; crypto_alt avg `-0.241` n `239`; crypto_major avg `0.6101` n `8`; equity avg `1.0288` n `161`; fx avg `0.042` n `6`; index avg `0.1596` n `27`; metal avg `-0.27` n `20`; unknown avg `0.1514` n `1243`
- 24h: commodity avg `0.4996` n `13`; crypto_alt avg `0.5894` n `239`; crypto_major avg `1.2109` n `8`; equity avg `5.8189` n `161`; fx avg `-0.1465` n `6`; index avg `0.5713` n `27`; metal avg `0.026` n `20`; unknown avg `4.4861` n `1153`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1393`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1257`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1202`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1196`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1144`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1134`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1103`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1058`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.102`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0984`, n `668`, weak_sample_signal
