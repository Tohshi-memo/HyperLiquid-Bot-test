# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-30T19:47:15.910286+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.053` n `12`; crypto_alt avg `-0.0251` n `230`; crypto_major avg `-0.0168` n `8`; equity avg `0.0539` n `102`; fx avg `0.0037` n `6`; index avg `-0.0019` n `25`; metal avg `0.0019` n `20`; unknown avg `0.0111` n `779`
- 1h: commodity avg `0.043` n `12`; crypto_alt avg `0.0909` n `230`; crypto_major avg `0.2025` n `8`; equity avg `0.5371` n `102`; fx avg `0.0427` n `6`; index avg `0.0682` n `25`; metal avg `0.1269` n `20`; unknown avg `-0.1235` n `779`
- 4h: commodity avg `-0.0765` n `12`; crypto_alt avg `0.0533` n `230`; crypto_major avg `0.3935` n `8`; equity avg `0.8238` n `102`; fx avg `-0.0108` n `6`; index avg `0.142` n `25`; metal avg `0.1646` n `20`; unknown avg `-0.1565` n `779`
- 24h: commodity avg `-0.1626` n `12`; crypto_alt avg `1.2379` n `230`; crypto_major avg `2.2244` n `8`; equity avg `6.0247` n `102`; fx avg `-0.3811` n `6`; index avg `0.7915` n `25`; metal avg `0.6448` n `20`; unknown avg `0.1129` n `738`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1373`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1372`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1132`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.099`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0884`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0853`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0832`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0647`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0606`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.06`, n `668`, weak_sample_signal
