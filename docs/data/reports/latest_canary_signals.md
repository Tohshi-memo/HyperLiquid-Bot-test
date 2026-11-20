# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-20T09:37:44.855703+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1321` n `13`; crypto_alt avg `-0.1952` n `239`; crypto_major avg `-0.4342` n `8`; equity avg `-0.4974` n `165`; fx avg `0.009` n `6`; index avg `-0.0636` n `27`; metal avg `-0.0816` n `20`; unknown avg `-0.1297` n `1260`
- 1h: commodity avg `-0.1406` n `13`; crypto_alt avg `-0.489` n `239`; crypto_major avg `-0.8619` n `8`; equity avg `-1.0901` n `165`; fx avg `0.0068` n `6`; index avg `-0.1036` n `27`; metal avg `-0.1797` n `20`; unknown avg `7.2063` n `1246`
- 4h: commodity avg `-0.5244` n `13`; crypto_alt avg `0.389` n `239`; crypto_major avg `-0.0062` n `8`; equity avg `-0.4643` n `165`; fx avg `-0.0148` n `6`; index avg `0.0206` n `27`; metal avg `0.5388` n `20`; unknown avg `8.0939` n `1176`
- 24h: commodity avg `-0.4421` n `13`; crypto_alt avg `-3.5249` n `239`; crypto_major avg `-3.3319` n `8`; equity avg `-7.6755` n `165`; fx avg `-0.0857` n `6`; index avg `-0.687` n `27`; metal avg `-1.4414` n `20`; unknown avg `22.4436` n `1153`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.162`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1608`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.141`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1254`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.1121`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1063`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0857`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0767`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.074`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0707`, n `668`, weak_sample_signal
