# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-07T23:52:23.674969+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.046` n `13`; crypto_alt avg `0.1179` n `239`; crypto_major avg `0.1751` n `8`; equity avg `0.0854` n `158`; fx avg `-0.0022` n `6`; index avg `0.0085` n `27`; metal avg `0.0079` n `20`; unknown avg `2.0475` n `1262`
- 1h: commodity avg `-0.0627` n `13`; crypto_alt avg `0.2912` n `239`; crypto_major avg `0.2916` n `8`; equity avg `0.1459` n `158`; fx avg `-0.0075` n `6`; index avg `0.0132` n `27`; metal avg `0.0083` n `20`; unknown avg `0.4987` n `1240`
- 4h: commodity avg `-0.0179` n `13`; crypto_alt avg `0.0565` n `239`; crypto_major avg `0.1523` n `8`; equity avg `0.0012` n `158`; fx avg `-0.0113` n `6`; index avg `-0.0009` n `27`; metal avg `0.0063` n `20`; unknown avg `0.2792` n `1198`
- 24h: commodity avg `0.0077` n `13`; crypto_alt avg `-1.1154` n `239`; crypto_major avg `-0.5064` n `8`; equity avg `0.0566` n `158`; fx avg `-0.0365` n `6`; index avg `0.054` n `27`; metal avg `-0.011` n `20`; unknown avg `160.5191` n `1087`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2119`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1605`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1586`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1276`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1268`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1088`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1051`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1041`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.104`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1026`, n `668`, weak_sample_signal
