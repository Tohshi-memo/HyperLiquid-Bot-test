# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-23T08:37:26.031452+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0838` n `13`; crypto_alt avg `0.0233` n `239`; crypto_major avg `0.2256` n `8`; equity avg `-0.0445` n `166`; fx avg `0.0247` n `6`; index avg `-0.0216` n `27`; metal avg `0.0206` n `20`; unknown avg `-0.11` n `1210`
- 1h: commodity avg `-0.1986` n `13`; crypto_alt avg `-0.0751` n `239`; crypto_major avg `0.0831` n `8`; equity avg `0.1406` n `166`; fx avg `0.0133` n `6`; index avg `-0.0094` n `27`; metal avg `-0.1707` n `20`; unknown avg `0.086` n `1172`
- 4h: commodity avg `-0.4709` n `13`; crypto_alt avg `0.6042` n `239`; crypto_major avg `0.4348` n `8`; equity avg `0.6867` n `166`; fx avg `0.0002` n `6`; index avg `0.0077` n `27`; metal avg `0.045` n `20`; unknown avg `-0.2351` n `1152`
- 24h: commodity avg `-0.7954` n `13`; crypto_alt avg `1.1375` n `239`; crypto_major avg `1.5951` n `8`; equity avg `2.1024` n `166`; fx avg `0.2443` n `6`; index avg `0.1001` n `27`; metal avg `0.3695` n `20`; unknown avg `305.9953` n `969`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `-0.1562`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1523`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1406`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1379`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1312`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1306`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1283`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1255`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1252`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1208`, n `668`, weak_sample_signal
