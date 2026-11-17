# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-17T18:52:31.092109+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0075` n `13`; crypto_alt avg `-0.1431` n `239`; crypto_major avg `-0.0741` n `8`; equity avg `-0.276` n `163`; fx avg `0.0013` n `6`; index avg `-0.025` n `27`; metal avg `-0.0583` n `20`; unknown avg `-0.1555` n `1265`
- 1h: commodity avg `0.1401` n `13`; crypto_alt avg `-0.1433` n `239`; crypto_major avg `-0.0636` n `8`; equity avg `-0.019` n `163`; fx avg `0.0024` n `6`; index avg `-0.0019` n `27`; metal avg `-0.0257` n `20`; unknown avg `-0.4038` n `1263`
- 4h: commodity avg `0.1316` n `13`; crypto_alt avg `-1.3877` n `239`; crypto_major avg `-1.0424` n `8`; equity avg `-1.0484` n `163`; fx avg `0.0425` n `6`; index avg `-0.0929` n `27`; metal avg `-0.1363` n `20`; unknown avg `2.359` n `1245`
- 24h: commodity avg `0.3645` n `13`; crypto_alt avg `-0.9286` n `239`; crypto_major avg `-0.4285` n `8`; equity avg `-2.0996` n `163`; fx avg `0.0518` n `6`; index avg `-0.2513` n `27`; metal avg `-0.0066` n `20`; unknown avg `8.1849` n `1097`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.1662`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1563`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.1396`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1377`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1314`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1275`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1218`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1169`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1057`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1039`, n `668`, weak_sample_signal
