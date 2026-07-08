# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-08T01:07:24.534592+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0133` n `12`; crypto_alt avg `-0.1346` n `229`; crypto_major avg `-0.1654` n `8`; equity avg `-0.1823` n `91`; fx avg `-0.0054` n `6`; index avg `-0.0486` n `25`; metal avg `-0.1807` n `20`; unknown avg `-0.1046` n `763`
- 1h: commodity avg `-0.1038` n `12`; crypto_alt avg `0.1524` n `229`; crypto_major avg `-0.0918` n `8`; equity avg `0.8723` n `91`; fx avg `-0.0149` n `6`; index avg `0.1887` n `25`; metal avg `-0.0347` n `20`; unknown avg `-0.0398` n `763`
- 4h: commodity avg `-0.0679` n `12`; crypto_alt avg `-0.502` n `229`; crypto_major avg `-0.7599` n `8`; equity avg `0.448` n `91`; fx avg `0.0355` n `6`; index avg `0.1441` n `25`; metal avg `-0.1506` n `20`; unknown avg `0.0387` n `763`
- 24h: commodity avg `0.8383` n `12`; crypto_alt avg `-2.2299` n `229`; crypto_major avg `-1.7954` n `8`; equity avg `-1.8764` n `91`; fx avg `-0.2037` n `6`; index avg `-0.2025` n `25`; metal avg `-0.4366` n `20`; unknown avg `-0.2061` n `729`

## Correlations

- market_context_score -> fx_forward_1h_return_pct: corr `-0.1264`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1257`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1013`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0999`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0924`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0814`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.071`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0662`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0648`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0614`, n `668`, weak_sample_signal
