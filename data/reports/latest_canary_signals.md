# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-19T01:37:35.146557+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0156` n `13`; crypto_alt avg `-0.5208` n `239`; crypto_major avg `-0.6811` n `8`; equity avg `-0.8918` n `164`; fx avg `-0.0302` n `6`; index avg `-0.1065` n `27`; metal avg `-0.0807` n `20`; unknown avg `0.1555` n `1263`
- 1h: commodity avg `0.1162` n `13`; crypto_alt avg `-0.6802` n `239`; crypto_major avg `-0.7746` n `8`; equity avg `-0.7938` n `164`; fx avg `0.0155` n `6`; index avg `-0.1046` n `27`; metal avg `-0.1299` n `20`; unknown avg `0.5217` n `1263`
- 4h: commodity avg `0.0486` n `13`; crypto_alt avg `-0.1683` n `239`; crypto_major avg `-0.2036` n `8`; equity avg `0.1626` n `164`; fx avg `-0.0244` n `6`; index avg `0.0111` n `27`; metal avg `0.0981` n `20`; unknown avg `3.8789` n `1251`
- 24h: commodity avg `0.017` n `13`; crypto_alt avg `-0.9533` n `239`; crypto_major avg `-2.0355` n `8`; equity avg `-1.2418` n `164`; fx avg `-0.1149` n `6`; index avg `-0.0305` n `27`; metal avg `-0.8794` n `20`; unknown avg `47.4818` n `1127`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.1198`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0882`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0861`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0751`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0669`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.066`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0652`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0636`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0595`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0544`, n `668`, weak_sample_signal
