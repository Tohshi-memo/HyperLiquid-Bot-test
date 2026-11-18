# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-18T07:37:42.689880+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0661` n `13`; crypto_alt avg `-0.3175` n `239`; crypto_major avg `-0.3137` n `8`; equity avg `-0.1759` n `163`; fx avg `-0.0299` n `6`; index avg `-0.022` n `27`; metal avg `-0.0543` n `20`; unknown avg `0.4217` n `1266`
- 1h: commodity avg `-0.0073` n `13`; crypto_alt avg `-0.1282` n `239`; crypto_major avg `-0.031` n `8`; equity avg `0.0387` n `163`; fx avg `-0.0547` n `6`; index avg `-0.0141` n `27`; metal avg `-0.1238` n `20`; unknown avg `233.2955` n `1262`
- 4h: commodity avg `-0.2136` n `13`; crypto_alt avg `-0.0319` n `239`; crypto_major avg `0.0426` n `8`; equity avg `0.3537` n `163`; fx avg `-0.068` n `6`; index avg `0.0365` n `27`; metal avg `-0.2933` n `20`; unknown avg `11.3982` n `1224`
- 24h: commodity avg `-0.1189` n `13`; crypto_alt avg `0.0482` n `239`; crypto_major avg `0.4942` n `8`; equity avg `0.6034` n `163`; fx avg `-0.1383` n `6`; index avg `0.0253` n `27`; metal avg `-1.0084` n `20`; unknown avg `234.0716` n `1105`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.1042`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0847`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0805`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0795`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0771`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0746`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0731`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0711`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0599`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0584`, n `668`, weak_sample_signal
