# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-20T23:22:38.942916+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.23` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0076` n `13`; crypto_alt avg `-0.264` n `239`; crypto_major avg `-0.1977` n `8`; equity avg `0.0799` n `166`; fx avg `-0.0104` n `6`; index avg `0.0184` n `27`; metal avg `0.0011` n `20`; unknown avg `0.146` n `1258`
- 1h: commodity avg `-0.0122` n `13`; crypto_alt avg `0.0547` n `239`; crypto_major avg `-0.142` n `8`; equity avg `0.7134` n `166`; fx avg `-0.0197` n `6`; index avg `0.0829` n `27`; metal avg `0.0344` n `20`; unknown avg `0.1912` n `1240`
- 4h: commodity avg `0.1952` n `13`; crypto_alt avg `1.3978` n `239`; crypto_major avg `1.4823` n `8`; equity avg `0.6879` n `166`; fx avg `-0.0444` n `6`; index avg `0.0432` n `27`; metal avg `0.1221` n `20`; unknown avg `173.3231` n `1198`
- 24h: commodity avg `0.2637` n `13`; crypto_alt avg `-4.769` n `239`; crypto_major avg `-5.5522` n `8`; equity avg `-5.6903` n `166`; fx avg `-0.0239` n `6`; index avg `-0.6374` n `27`; metal avg `-0.7488` n `20`; unknown avg `12.1266` n `1123`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1652`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1518`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1503`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1208`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0974`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0961`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0943`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0872`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0848`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0783`, n `668`, weak_sample_signal
