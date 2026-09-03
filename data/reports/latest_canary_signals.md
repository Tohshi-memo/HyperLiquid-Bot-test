# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-03T09:07:34.286248+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0602` n `12`; crypto_alt avg `-0.0309` n `232`; crypto_major avg `0.05` n `8`; equity avg `0.0094` n `133`; fx avg `0.0239` n `6`; index avg `0.0065` n `26`; metal avg `0.0332` n `20`; unknown avg `0.0367` n `790`
- 1h: commodity avg `0.3482` n `12`; crypto_alt avg `-0.3125` n `232`; crypto_major avg `-0.3139` n `8`; equity avg `-0.2297` n `133`; fx avg `-0.0074` n `6`; index avg `-0.0373` n `26`; metal avg `-0.0434` n `20`; unknown avg `0.0743` n `790`
- 4h: commodity avg `0.1076` n `12`; crypto_alt avg `0.1312` n `232`; crypto_major avg `0.1099` n `8`; equity avg `-0.0474` n `133`; fx avg `-0.1232` n `6`; index avg `-0.0316` n `26`; metal avg `0.1189` n `20`; unknown avg `16.2318` n `754`
- 24h: commodity avg `0.3321` n `12`; crypto_alt avg `1.0838` n `232`; crypto_major avg `1.2868` n `8`; equity avg `1.6232` n `133`; fx avg `-0.3784` n `6`; index avg `0.1726` n `26`; metal avg `0.8842` n `20`; unknown avg `-0.182` n `735`

## Correlations

- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1007`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0949`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0765`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0695`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.067`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0651`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0496`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0488`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0452`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0386`, n `668`, weak_sample_signal
