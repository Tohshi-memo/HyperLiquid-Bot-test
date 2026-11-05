# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-05T07:22:34.226636+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.2058` n `13`; crypto_alt avg `-0.2744` n `239`; crypto_major avg `-0.2203` n `8`; equity avg `-0.2009` n `158`; fx avg `-0.0155` n `6`; index avg `-0.0348` n `27`; metal avg `-0.0842` n `20`; unknown avg `0.3131` n `1265`
- 1h: commodity avg `0.2536` n `13`; crypto_alt avg `-0.1337` n `239`; crypto_major avg `-0.0256` n `8`; equity avg `0.2526` n `158`; fx avg `-0.0275` n `6`; index avg `0.0125` n `27`; metal avg `-0.0498` n `20`; unknown avg `0.0712` n `1251`
- 4h: commodity avg `0.2189` n `13`; crypto_alt avg `-0.9038` n `239`; crypto_major avg `-0.5323` n `8`; equity avg `-0.5562` n `158`; fx avg `-0.0374` n `6`; index avg `-0.1564` n `27`; metal avg `-0.2124` n `20`; unknown avg `-0.021` n `1209`
- 24h: commodity avg `-1.7969` n `13`; crypto_alt avg `0.6674` n `239`; crypto_major avg `1.9703` n `8`; equity avg `-2.1554` n `158`; fx avg `0.0447` n `6`; index avg `-0.0904` n `27`; metal avg `0.7638` n `20`; unknown avg `30.9856` n `1008`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2503`, n `668`, moderate_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1829`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.182`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1492`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1428`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1426`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1391`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1337`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1305`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1235`, n `668`, weak_sample_signal
