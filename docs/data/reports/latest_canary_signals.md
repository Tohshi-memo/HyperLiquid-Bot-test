# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-19T09:52:27.416666+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1006` n `13`; crypto_alt avg `-0.0238` n `239`; crypto_major avg `0.0121` n `8`; equity avg `0.2055` n `164`; fx avg `-0.002` n `6`; index avg `0.1202` n `27`; metal avg `-0.0146` n `20`; unknown avg `189.6987` n `1266`
- 1h: commodity avg `-0.0169` n `13`; crypto_alt avg `0.0875` n `239`; crypto_major avg `0.1552` n `8`; equity avg `0.2104` n `164`; fx avg `0.0241` n `6`; index avg `0.1058` n `27`; metal avg `-0.0191` n `20`; unknown avg `261.8614` n `1260`
- 4h: commodity avg `-0.0995` n `13`; crypto_alt avg `0.7331` n `239`; crypto_major avg `0.6328` n `8`; equity avg `1.3886` n `164`; fx avg `0.0773` n `6`; index avg `0.2834` n `27`; metal avg `-0.0762` n `20`; unknown avg `379.9914` n `1202`
- 24h: commodity avg `0.1862` n `13`; crypto_alt avg `0.1577` n `239`; crypto_major avg `-0.4793` n `8`; equity avg `0.1705` n `164`; fx avg `0.0368` n `6`; index avg `0.2438` n `27`; metal avg `-0.2292` n `20`; unknown avg `3.5832` n `1161`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1626`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1599`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1348`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1258`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0759`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0604`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0601`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0579`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0538`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0513`, n `668`, weak_sample_signal
