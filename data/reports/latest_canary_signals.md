# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-12T12:22:30.022550+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.01` n `13`; crypto_alt avg `-0.1218` n `239`; crypto_major avg `0.0317` n `8`; equity avg `-0.0481` n `162`; fx avg `-0.0074` n `6`; index avg `0.0124` n `27`; metal avg `0.0266` n `20`; unknown avg `-0.0591` n `1255`
- 1h: commodity avg `-0.0222` n `13`; crypto_alt avg `-0.7712` n `239`; crypto_major avg `-0.8322` n `8`; equity avg `-0.4423` n `162`; fx avg `-0.0065` n `6`; index avg `-0.0054` n `27`; metal avg `-0.0193` n `20`; unknown avg `20.8477` n `1243`
- 4h: commodity avg `-0.3158` n `13`; crypto_alt avg `-0.7151` n `239`; crypto_major avg `-0.9092` n `8`; equity avg `-0.2924` n `162`; fx avg `-0.0364` n `6`; index avg `0.0208` n `27`; metal avg `-0.1979` n `20`; unknown avg `18.9844` n `1245`
- 24h: commodity avg `-0.204` n `13`; crypto_alt avg `-2.6014` n `239`; crypto_major avg `-1.7911` n `8`; equity avg `-1.6848` n `162`; fx avg `-0.1053` n `6`; index avg `-0.0911` n `27`; metal avg `-0.8309` n `20`; unknown avg `0.1862` n `1140`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1403`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1362`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1331`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1311`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1224`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1136`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1052`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0982`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0967`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0962`, n `668`, weak_sample_signal
