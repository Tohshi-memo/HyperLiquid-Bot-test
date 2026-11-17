# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-17T20:52:46.775516+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0233` n `13`; crypto_alt avg `-0.3649` n `239`; crypto_major avg `-0.3523` n `8`; equity avg `-0.3335` n `163`; fx avg `-0.0045` n `6`; index avg `-0.0504` n `27`; metal avg `-0.0705` n `20`; unknown avg `0.3413` n `1265`
- 1h: commodity avg `0.0712` n `13`; crypto_alt avg `0.2437` n `239`; crypto_major avg `0.185` n `8`; equity avg `0.1405` n `163`; fx avg `-0.0178` n `6`; index avg `0.0178` n `27`; metal avg `-0.0437` n `20`; unknown avg `3.9651` n `1255`
- 4h: commodity avg `-0.0596` n `13`; crypto_alt avg `0.6923` n `239`; crypto_major avg `0.9296` n `8`; equity avg `0.7543` n `163`; fx avg `-0.0099` n `6`; index avg `0.0735` n `27`; metal avg `-0.1` n `20`; unknown avg `3.2034` n `1251`
- 24h: commodity avg `0.1064` n `13`; crypto_alt avg `-0.3498` n `239`; crypto_major avg `-0.2821` n `8`; equity avg `-1.8372` n `163`; fx avg `0.0271` n `6`; index avg `-0.2051` n `27`; metal avg `-0.1071` n `20`; unknown avg `6.423` n `1097`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.1575`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1395`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1234`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1136`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1074`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.1004`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0941`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0931`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0914`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0902`, n `668`, weak_sample_signal
