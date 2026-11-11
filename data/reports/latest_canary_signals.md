# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-11T21:28:20.107186+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0055` n `13`; crypto_alt avg `0.0498` n `239`; crypto_major avg `0.0829` n `8`; equity avg `-0.0144` n `161`; fx avg `-0.0084` n `6`; index avg `-0.0117` n `27`; metal avg `0.0046` n `20`; unknown avg `-0.2368` n `1254`
- 1h: commodity avg `0.0663` n `13`; crypto_alt avg `0.0356` n `239`; crypto_major avg `0.2267` n `8`; equity avg `-0.1313` n `161`; fx avg `-0.0131` n `6`; index avg `-0.0405` n `27`; metal avg `-0.0409` n `20`; unknown avg `3.5788` n `1218`
- 4h: commodity avg `-0.1747` n `13`; crypto_alt avg `-1.2134` n `239`; crypto_major avg `-0.6908` n `8`; equity avg `-1.0251` n `161`; fx avg `0.0138` n `6`; index avg `-0.089` n `27`; metal avg `-0.2495` n `20`; unknown avg `2.3501` n `1210`
- 24h: commodity avg `0.1993` n `13`; crypto_alt avg `0.5873` n `239`; crypto_major avg `1.0581` n `8`; equity avg `4.561` n `161`; fx avg `-0.1419` n `6`; index avg `0.4365` n `27`; metal avg `-0.0733` n `20`; unknown avg `5.4415` n `1141`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1419`, n `669`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1245`, n `669`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1237`, n `669`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1231`, n `669`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1193`, n `669`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1102`, n `669`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1082`, n `669`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1009`, n `669`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1004`, n `669`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0945`, n `669`, weak_sample_signal
