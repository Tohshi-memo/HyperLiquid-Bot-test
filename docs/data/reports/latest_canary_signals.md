# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-23T05:22:30.044835+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0144` n `13`; crypto_alt avg `0.3757` n `239`; crypto_major avg `0.4086` n `8`; equity avg `0.3715` n `166`; fx avg `-0.0044` n `6`; index avg `0.0412` n `27`; metal avg `0.1098` n `20`; unknown avg `56.6574` n `1264`
- 1h: commodity avg `-0.0231` n `13`; crypto_alt avg `0.132` n `239`; crypto_major avg `0.0685` n `8`; equity avg `0.1024` n `166`; fx avg `-0.0164` n `6`; index avg `0.0111` n `27`; metal avg `0.0833` n `20`; unknown avg `10.3479` n `1260`
- 4h: commodity avg `0.0224` n `13`; crypto_alt avg `0.9412` n `239`; crypto_major avg `0.92` n `8`; equity avg `0.7525` n `166`; fx avg `0.0664` n `6`; index avg `-0.0127` n `27`; metal avg `0.0367` n `20`; unknown avg `326.2151` n `1243`
- 24h: commodity avg `-0.3207` n `13`; crypto_alt avg `2.5434` n `239`; crypto_major avg `3.423` n `8`; equity avg `2.4344` n `166`; fx avg `0.2189` n `6`; index avg `0.2085` n `27`; metal avg `0.4977` n `20`; unknown avg `292.8177` n `1025`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `-0.1469`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.141`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1372`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1301`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1262`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1228`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1227`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1214`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1192`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1153`, n `668`, weak_sample_signal
