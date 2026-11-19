# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-19T00:22:34.504709+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0034` n `13`; crypto_alt avg `-0.257` n `239`; crypto_major avg `-0.2645` n `8`; equity avg `-0.1493` n `164`; fx avg `-0.0115` n `6`; index avg `-0.0283` n `27`; metal avg `0.0249` n `20`; unknown avg `1.6517` n `1263`
- 1h: commodity avg `-0.0219` n `13`; crypto_alt avg `-0.0104` n `239`; crypto_major avg `-0.2901` n `8`; equity avg `0.0634` n `164`; fx avg `-0.0549` n `6`; index avg `-0.002` n `27`; metal avg `0.0291` n `20`; unknown avg `1.6974` n `1257`
- 4h: commodity avg `-0.0775` n `13`; crypto_alt avg `0.2853` n `239`; crypto_major avg `0.0979` n `8`; equity avg `0.9214` n `164`; fx avg `-0.0494` n `6`; index avg `0.1122` n `27`; metal avg `0.1961` n `20`; unknown avg `0.5005` n `1223`
- 24h: commodity avg `-0.1877` n `13`; crypto_alt avg `-1.3802` n `239`; crypto_major avg `-2.5927` n `8`; equity avg `-1.7855` n `164`; fx avg `-0.1603` n `6`; index avg `-0.1064` n `27`; metal avg `-0.9442` n `20`; unknown avg `50.125` n `1129`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.1139`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0845`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0824`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0718`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0663`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0652`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0641`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0604`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0601`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0555`, n `668`, weak_sample_signal
