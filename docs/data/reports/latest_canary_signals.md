# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-16T10:52:29.183888+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0104` n `13`; crypto_alt avg `0.0071` n `239`; crypto_major avg `-0.0209` n `8`; equity avg `-0.0322` n `162`; fx avg `-0.0064` n `6`; index avg `-0.0176` n `27`; metal avg `-0.0051` n `20`; unknown avg `0.0919` n `1265`
- 1h: commodity avg `-0.0059` n `13`; crypto_alt avg `0.1481` n `239`; crypto_major avg `0.5041` n `8`; equity avg `-0.0356` n `162`; fx avg `0.0208` n `6`; index avg `-0.0201` n `27`; metal avg `0.1348` n `20`; unknown avg `0.2209` n `1263`
- 4h: commodity avg `-0.207` n `13`; crypto_alt avg `-0.3709` n `239`; crypto_major avg `-0.0696` n `8`; equity avg `-0.3833` n `162`; fx avg `-0.0147` n `6`; index avg `-0.0087` n `27`; metal avg `0.0865` n `20`; unknown avg `34.4381` n `1135`
- 24h: commodity avg `-0.3793` n `13`; crypto_alt avg `-1.3598` n `239`; crypto_major avg `-0.9923` n `8`; equity avg `-1.0369` n `162`; fx avg `-0.0619` n `6`; index avg `-0.0776` n `27`; metal avg `0.0368` n `20`; unknown avg `35.9865` n `1053`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1371`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.115`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1127`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1109`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1013`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1007`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0879`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0721`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0716`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0715`, n `668`, weak_sample_signal
