# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-23T08:22:37.655462+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1115` n `13`; crypto_alt avg `-0.2562` n `239`; crypto_major avg `-0.3554` n `8`; equity avg `-0.0962` n `166`; fx avg `-0.0155` n `6`; index avg `-0.0104` n `27`; metal avg `0.0021` n `20`; unknown avg `0.2596` n `1232`
- 1h: commodity avg `-0.0954` n `13`; crypto_alt avg `-0.1181` n `239`; crypto_major avg `-0.3003` n `8`; equity avg `0.2163` n `166`; fx avg `0.0058` n `6`; index avg `0.0183` n `27`; metal avg `-0.2508` n `20`; unknown avg `0.4586` n `1226`
- 4h: commodity avg `-0.3918` n `13`; crypto_alt avg `0.3273` n `239`; crypto_major avg `-0.1105` n `8`; equity avg `0.5638` n `166`; fx avg `-0.0208` n `6`; index avg `0.0087` n `27`; metal avg `0.028` n `20`; unknown avg `-0.1506` n `1202`
- 24h: commodity avg `-0.7105` n `13`; crypto_alt avg `1.4174` n `239`; crypto_major avg `1.842` n `8`; equity avg `2.5267` n `166`; fx avg `0.227` n `6`; index avg `0.1521` n `27`; metal avg `0.3692` n `20`; unknown avg `351.2533` n `987`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `-0.155`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1507`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1406`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1353`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1291`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1287`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1275`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1272`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1253`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1208`, n `668`, weak_sample_signal
