# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-27T20:22:29.935002+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0151` n `13`; crypto_alt avg `-0.04` n `239`; crypto_major avg `-0.0453` n `8`; equity avg `0.04` n `168`; fx avg `0.0016` n `6`; index avg `0.0052` n `27`; metal avg `0.019` n `20`; unknown avg `0.9879` n `1263`
- 1h: commodity avg `0.0143` n `13`; crypto_alt avg `-0.1831` n `239`; crypto_major avg `-0.2076` n `8`; equity avg `-0.039` n `168`; fx avg `-0.0079` n `6`; index avg `-0.0152` n `27`; metal avg `0.1439` n `20`; unknown avg `2.4184` n `1251`
- 4h: commodity avg `-0.0205` n `13`; crypto_alt avg `0.1367` n `239`; crypto_major avg `-0.2071` n `8`; equity avg `0.7265` n `168`; fx avg `-0.0274` n `6`; index avg `0.0733` n `27`; metal avg `0.2878` n `20`; unknown avg `168.4867` n `1228`
- 24h: commodity avg `-0.5001` n `13`; crypto_alt avg `-0.1239` n `239`; crypto_major avg `-0.0335` n `8`; equity avg `3.1723` n `168`; fx avg `-0.1559` n `6`; index avg `0.3011` n `27`; metal avg `0.9526` n `20`; unknown avg `271.3832` n `1043`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1293`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1259`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.1022`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1007`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0915`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0843`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0833`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0804`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0682`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0652`, n `668`, weak_sample_signal
