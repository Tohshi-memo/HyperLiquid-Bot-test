# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-26T14:22:32.167895+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0676` n `13`; crypto_alt avg `-0.0002` n `239`; crypto_major avg `-0.0505` n `8`; equity avg `-0.1213` n `168`; fx avg `-0.004` n `6`; index avg `-0.024` n `27`; metal avg `0.0136` n `20`; unknown avg `1.2694` n `1265`
- 1h: commodity avg `0.1258` n `13`; crypto_alt avg `0.0984` n `239`; crypto_major avg `0.0122` n `8`; equity avg `-0.2374` n `168`; fx avg `0.0214` n `6`; index avg `-0.0427` n `27`; metal avg `0.0047` n `20`; unknown avg `114.5461` n `1263`
- 4h: commodity avg `0.2809` n `13`; crypto_alt avg `0.2162` n `239`; crypto_major avg `0.054` n `8`; equity avg `0.1517` n `168`; fx avg `0.0072` n `6`; index avg `0.0053` n `27`; metal avg `-0.0004` n `20`; unknown avg `1.0169` n `1255`
- 24h: commodity avg `0.3756` n `13`; crypto_alt avg `5.524` n `239`; crypto_major avg `4.7989` n `8`; equity avg `5.0126` n `168`; fx avg `0.0792` n `6`; index avg `0.4562` n `27`; metal avg `1.0799` n `20`; unknown avg `425.732` n `1061`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1265`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1253`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1153`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1147`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1131`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1127`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1013`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.1008`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0907`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0877`, n `668`, weak_sample_signal
