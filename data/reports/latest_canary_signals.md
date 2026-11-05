# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-05T13:22:42.437676+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0361` n `13`; crypto_alt avg `0.1456` n `239`; crypto_major avg `0.0407` n `8`; equity avg `0.2056` n `158`; fx avg `-0.0118` n `6`; index avg `0.0274` n `27`; metal avg `-0.0313` n `20`; unknown avg `0.2681` n `1255`
- 1h: commodity avg `0.1374` n `13`; crypto_alt avg `-0.2181` n `239`; crypto_major avg `-0.4438` n `8`; equity avg `-0.3729` n `158`; fx avg `-0.0239` n `6`; index avg `-0.0094` n `27`; metal avg `-0.0128` n `20`; unknown avg `0.9765` n `1253`
- 4h: commodity avg `0.4867` n `13`; crypto_alt avg `-1.1527` n `239`; crypto_major avg `-0.9294` n `8`; equity avg `-0.7652` n `158`; fx avg `0.0133` n `6`; index avg `-0.0058` n `27`; metal avg `0.0505` n `20`; unknown avg `16.9868` n `1201`
- 24h: commodity avg `-0.8939` n `13`; crypto_alt avg `0.2584` n `239`; crypto_major avg `1.196` n `8`; equity avg `-2.3788` n `158`; fx avg `-0.0266` n `6`; index avg `-0.251` n `27`; metal avg `0.7139` n `20`; unknown avg `19.0861` n `1068`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2405`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1965`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1874`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1596`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1517`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1417`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1412`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1387`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1277`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1142`, n `668`, weak_sample_signal
