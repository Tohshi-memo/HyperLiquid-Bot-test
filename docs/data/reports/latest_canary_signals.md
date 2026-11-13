# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-13T00:52:31.578296+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0053` n `13`; crypto_alt avg `0.1639` n `239`; crypto_major avg `0.1782` n `8`; equity avg `0.0342` n `162`; fx avg `0.0138` n `6`; index avg `0.0137` n `27`; metal avg `-0.0091` n `20`; unknown avg `4.115` n `1261`
- 1h: commodity avg `-0.0693` n `13`; crypto_alt avg `0.01` n `239`; crypto_major avg `-0.1494` n `8`; equity avg `-0.0817` n `162`; fx avg `0.0332` n `6`; index avg `0.0307` n `27`; metal avg `-0.0065` n `20`; unknown avg `15.984` n `1253`
- 4h: commodity avg `-0.0545` n `13`; crypto_alt avg `0.264` n `239`; crypto_major avg `0.0747` n `8`; equity avg `0.8874` n `162`; fx avg `0.0002` n `6`; index avg `0.1195` n `27`; metal avg `0.0704` n `20`; unknown avg `192.9036` n `1193`
- 24h: commodity avg `0.8563` n `13`; crypto_alt avg `-1.0709` n `239`; crypto_major avg `-2.0452` n `8`; equity avg `-0.1686` n `162`; fx avg `-0.0707` n `6`; index avg `0.1012` n `27`; metal avg `-0.6296` n `20`; unknown avg `51.6639` n `1121`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1314`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1079`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0953`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0915`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0898`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0863`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0858`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0855`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0836`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0827`, n `668`, weak_sample_signal
