# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-27T15:52:30.967125+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0134` n `12`; crypto_alt avg `0.1725` n `230`; crypto_major avg `0.1262` n `8`; equity avg `0.1256` n `102`; fx avg `0.0019` n `6`; index avg `0.0273` n `25`; metal avg `0.0264` n `20`; unknown avg `0.0638` n `774`
- 1h: commodity avg `-0.0739` n `12`; crypto_alt avg `-0.1694` n `230`; crypto_major avg `-0.1008` n `8`; equity avg `-0.5007` n `102`; fx avg `-0.0211` n `6`; index avg `-0.1041` n `25`; metal avg `0.0655` n `20`; unknown avg `-0.2263` n `774`
- 4h: commodity avg `0.0531` n `12`; crypto_alt avg `-1.7352` n `230`; crypto_major avg `-1.4659` n `8`; equity avg `-2.9282` n `102`; fx avg `-0.0593` n `6`; index avg `-0.5893` n `25`; metal avg `-0.0884` n `20`; unknown avg `-0.1237` n `774`
- 24h: commodity avg `-0.5564` n `12`; crypto_alt avg `-1.4995` n `230`; crypto_major avg `-0.7835` n `8`; equity avg `-2.178` n `102`; fx avg `0.0434` n `6`; index avg `-0.5092` n `25`; metal avg `0.2511` n `20`; unknown avg `-0.3929` n `757`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1962`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1304`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1289`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.114`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.091`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.091`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0873`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0838`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0668`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0657`, n `668`, weak_sample_signal
