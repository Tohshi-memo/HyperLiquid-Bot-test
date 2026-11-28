# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-28T04:22:26.672134+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0095` n `13`; crypto_alt avg `0.0951` n `239`; crypto_major avg `0.0534` n `8`; equity avg `0.0828` n `168`; fx avg `-0.0095` n `6`; index avg `0.0024` n `27`; metal avg `0.0054` n `20`; unknown avg `2.4848` n `1263`
- 1h: commodity avg `-0.0216` n `13`; crypto_alt avg `0.1168` n `239`; crypto_major avg `0.1359` n `8`; equity avg `0.0578` n `168`; fx avg `0.0032` n `6`; index avg `0.0026` n `27`; metal avg `-0.0117` n `20`; unknown avg `0.8008` n `1247`
- 4h: commodity avg `-0.0732` n `13`; crypto_alt avg `-0.4248` n `239`; crypto_major avg `0.243` n `8`; equity avg `0.1575` n `168`; fx avg `0.0065` n `6`; index avg `0.0028` n `27`; metal avg `0.0199` n `20`; unknown avg `1.6453` n `1247`
- 24h: commodity avg `-0.7972` n `13`; crypto_alt avg `-1.4021` n `239`; crypto_major avg `-1.6487` n `8`; equity avg `0.7873` n `168`; fx avg `-0.1465` n `6`; index avg `0.0561` n `27`; metal avg `0.0932` n `20`; unknown avg `214.5242` n `981`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `-0.145`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1395`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.1209`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1066`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0994`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0865`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.07`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.067`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.065`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0634`, n `668`, weak_sample_signal
