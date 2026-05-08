# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-08T08:12:40.550285+00:00`
- Correlation status: `ready`
- Asset price records: `628`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.05` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0824` n `12`; crypto_alt avg `0.2391` n `228`; crypto_major avg `0.157` n `8`; equity avg `0.251` n `65`; fx avg `0.0198` n `5`; index avg `0.1065` n `23`; metal avg `0.0282` n `18`; unknown avg `0.1036` n `375`
- 1h: commodity avg `0.2354` n `12`; crypto_alt avg `0.646` n `228`; crypto_major avg `0.5434` n `8`; equity avg `0.4584` n `65`; fx avg `0.0133` n `5`; index avg `0.0935` n `23`; metal avg `-0.2783` n `18`; unknown avg `0.116` n `375`
- 4h: commodity avg `-0.0189` n `12`; crypto_alt avg `0.1122` n `228`; crypto_major avg `0.1383` n `8`; equity avg `0.8289` n `65`; fx avg `0.0943` n `5`; index avg `0.2171` n `23`; metal avg `0.0555` n `18`; unknown avg `0.3507` n `355`
- 24h: commodity avg `1.2679` n `12`; crypto_alt avg `0.5032` n `228`; crypto_major avg `-2.1858` n `8`; equity avg `-0.8587` n `65`; fx avg `0.3104` n `5`; index avg `-0.6844` n `23`; metal avg `-0.7734` n `18`; unknown avg `-0.2022` n `355`

## Correlations

- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1324`, n `620`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1319`, n `620`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1148`, n `624`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1145`, n `624`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1078`, n `624`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0984`, n `624`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0856`, n `620`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0811`, n `620`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.079`, n `620`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0687`, n `624`, weak_sample_signal
