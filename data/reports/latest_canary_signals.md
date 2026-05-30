# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-30T09:37:17.909499+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0005` n `12`; crypto_alt avg `0.1324` n `228`; crypto_major avg `0.0457` n `8`; equity avg `0.0126` n `69`; fx avg `0.0224` n `6`; index avg `-0.0291` n `23`; metal avg `0.0382` n `18`; unknown avg `0.7757` n `421`
- 1h: commodity avg `-0.0285` n `12`; crypto_alt avg `0.0981` n `228`; crypto_major avg `0.1069` n `8`; equity avg `0.0743` n `69`; fx avg `0.2101` n `6`; index avg `0.0249` n `23`; metal avg `0.1155` n `18`; unknown avg `0.8241` n `421`
- 4h: commodity avg `-0.0703` n `12`; crypto_alt avg `-0.0244` n `228`; crypto_major avg `0.2351` n `8`; equity avg `0.0968` n `69`; fx avg `0.0323` n `6`; index avg `0.0331` n `23`; metal avg `0.0605` n `18`; unknown avg `-0.2239` n `401`
- 24h: commodity avg `-0.23` n `12`; crypto_alt avg `1.0705` n `228`; crypto_major avg `1.5854` n `8`; equity avg `1.0226` n `69`; fx avg `0.1232` n `6`; index avg `0.0418` n `23`; metal avg `0.0092` n `18`; unknown avg `0.1904` n `399`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1933`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1639`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1617`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1513`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1301`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1166`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1165`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1125`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1118`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1107`, n `668`, weak_sample_signal
