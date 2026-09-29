# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-29T00:52:28.664618+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0475` n `12`; crypto_alt avg `-0.5711` n `234`; crypto_major avg `-0.4836` n `8`; equity avg `-0.3186` n `141`; fx avg `0.0146` n `6`; index avg `-0.0596` n `26`; metal avg `-0.0707` n `20`; unknown avg `0.4322` n `963`
- 1h: commodity avg `0.0237` n `12`; crypto_alt avg `-0.4163` n `234`; crypto_major avg `-0.367` n `8`; equity avg `-0.252` n `141`; fx avg `0.0125` n `6`; index avg `-0.0554` n `26`; metal avg `-0.0651` n `20`; unknown avg `0.1366` n `955`
- 4h: commodity avg `-0.0243` n `12`; crypto_alt avg `0.3266` n `234`; crypto_major avg `-0.2542` n `8`; equity avg `-0.1504` n `141`; fx avg `0.0069` n `6`; index avg `-0.0448` n `26`; metal avg `0.0041` n `20`; unknown avg `0.0547` n `929`
- 24h: commodity avg `0.1452` n `12`; crypto_alt avg `-3.9098` n `234`; crypto_major avg `-2.2919` n `8`; equity avg `-3.0322` n `141`; fx avg `-0.0088` n `6`; index avg `-0.3356` n `26`; metal avg `-0.8183` n `20`; unknown avg `143.7262` n `804`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1759`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.164`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1317`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1138`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.109`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1081`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1022`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0994`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0945`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0906`, n `668`, weak_sample_signal
