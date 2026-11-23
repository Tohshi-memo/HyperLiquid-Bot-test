# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-23T07:52:28.315565+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0095` n `13`; crypto_alt avg `0.0033` n `239`; crypto_major avg `0.0167` n `8`; equity avg `-0.0242` n `166`; fx avg `-0.0004` n `6`; index avg `-0.0212` n `27`; metal avg `-0.0198` n `20`; unknown avg `-0.1816` n `1264`
- 1h: commodity avg `-0.0863` n `13`; crypto_alt avg `0.0713` n `239`; crypto_major avg `-0.031` n `8`; equity avg `0.0896` n `166`; fx avg `0.0144` n `6`; index avg `-0.007` n `27`; metal avg `0.023` n `20`; unknown avg `-0.0834` n `1260`
- 4h: commodity avg `-0.2372` n `13`; crypto_alt avg `0.8151` n `239`; crypto_major avg `0.3648` n `8`; equity avg `0.5987` n `166`; fx avg `-0.011` n `6`; index avg `-0.026` n `27`; metal avg `0.2227` n `20`; unknown avg `-0.0248` n `1230`
- 24h: commodity avg `-0.5856` n `13`; crypto_alt avg `2.4366` n `239`; crypto_major avg `2.991` n `8`; equity avg `2.6054` n `166`; fx avg `0.2306` n `6`; index avg `0.1536` n `27`; metal avg `0.5817` n `20`; unknown avg `340.4047` n `1019`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `-0.1515`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1455`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1406`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1293`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1284`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1278`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1267`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1257`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1251`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1208`, n `668`, weak_sample_signal
