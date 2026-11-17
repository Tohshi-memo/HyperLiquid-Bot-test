# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-17T20:22:31.611596+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0182` n `13`; crypto_alt avg `0.2211` n `239`; crypto_major avg `0.2277` n `8`; equity avg `0.3381` n `163`; fx avg `-0.0019` n `6`; index avg `0.0247` n `27`; metal avg `0.0287` n `20`; unknown avg `0.5986` n `1263`
- 1h: commodity avg `-0.1355` n `13`; crypto_alt avg `0.3355` n `239`; crypto_major avg `0.2905` n `8`; equity avg `-0.0986` n `163`; fx avg `-0.0085` n `6`; index avg `-0.0324` n `27`; metal avg `-0.0971` n `20`; unknown avg `6.7639` n `1255`
- 4h: commodity avg `-0.1919` n `13`; crypto_alt avg `-0.1869` n `239`; crypto_major avg `0.2995` n `8`; equity avg `0.3794` n `163`; fx avg `-0.0132` n `6`; index avg `0.016` n `27`; metal avg `-0.1094` n `20`; unknown avg `5.8679` n `1251`
- 24h: commodity avg `0.1083` n `13`; crypto_alt avg `-0.2826` n `239`; crypto_major avg `-0.0668` n `8`; equity avg `-1.4983` n `163`; fx avg `0.0212` n `6`; index avg `-0.1804` n `27`; metal avg `-0.0868` n `20`; unknown avg `10.341` n `1099`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.1554`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1382`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1217`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1135`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1109`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.1074`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0986`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0933`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0931`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0923`, n `668`, weak_sample_signal
