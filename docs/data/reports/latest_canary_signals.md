# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-25T06:37:28.801881+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1496` n `13`; crypto_alt avg `0.2637` n `239`; crypto_major avg `0.1008` n `8`; equity avg `0.0143` n `168`; fx avg `-0.0163` n `6`; index avg `-0.0036` n `27`; metal avg `-0.0382` n `20`; unknown avg `-0.1364` n `1263`
- 1h: commodity avg `-0.0158` n `13`; crypto_alt avg `0.7744` n `239`; crypto_major avg `0.367` n `8`; equity avg `0.1156` n `168`; fx avg `-0.0207` n `6`; index avg `0.0183` n `27`; metal avg `-0.0705` n `20`; unknown avg `165.6079` n `1231`
- 4h: commodity avg `-0.1315` n `13`; crypto_alt avg `1.4434` n `239`; crypto_major avg `0.2181` n `8`; equity avg `-0.5218` n `168`; fx avg `-0.0491` n `6`; index avg `0.0127` n `27`; metal avg `-0.4804` n `20`; unknown avg `1.499` n `1219`
- 24h: commodity avg `0.4248` n `13`; crypto_alt avg `-2.5757` n `239`; crypto_major avg `-2.8925` n `8`; equity avg `-5.3365` n `167`; fx avg `0.0853` n `6`; index avg `-0.5086` n `27`; metal avg `-0.961` n `20`; unknown avg `698.8293` n `1029`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1289`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1288`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1262`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1172`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1063`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1054`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0892`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0869`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0824`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0676`, n `668`, weak_sample_signal
