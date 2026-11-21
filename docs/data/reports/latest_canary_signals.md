# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-21T02:22:29.419203+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0051` n `13`; crypto_alt avg `0.2239` n `239`; crypto_major avg `-0.0001` n `8`; equity avg `-0.0811` n `166`; fx avg `-0.0088` n `6`; index avg `-0.0068` n `27`; metal avg `0.0126` n `20`; unknown avg `0.5889` n `1260`
- 1h: commodity avg `0.0038` n `13`; crypto_alt avg `0.182` n `239`; crypto_major avg `-0.1547` n `8`; equity avg `-0.0844` n `166`; fx avg `-0.012` n `6`; index avg `-0.0062` n `27`; metal avg `-0.0265` n `20`; unknown avg `158.9017` n `1258`
- 4h: commodity avg `-0.0369` n `13`; crypto_alt avg `-0.2756` n `239`; crypto_major avg `-0.4658` n `8`; equity avg `0.3436` n `166`; fx avg `-0.0249` n `6`; index avg `0.0484` n `27`; metal avg `0.0193` n `20`; unknown avg `1.1943` n `1234`
- 24h: commodity avg `0.3434` n `13`; crypto_alt avg `-3.4722` n `239`; crypto_major avg `-4.6187` n `8`; equity avg `-4.9496` n `166`; fx avg `-0.0206` n `6`; index avg `-0.5855` n `27`; metal avg `-0.0134` n `20`; unknown avg `191.4031` n `1119`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1611`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1509`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1451`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1211`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0966`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0948`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0908`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0889`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0787`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.078`, n `668`, weak_sample_signal
