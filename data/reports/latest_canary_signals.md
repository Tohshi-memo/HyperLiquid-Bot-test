# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-11T16:37:30.895067+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0231` n `13`; crypto_alt avg `-0.0196` n `239`; crypto_major avg `0.0292` n `8`; equity avg `0.1641` n `161`; fx avg `-0.0208` n `6`; index avg `0.0184` n `27`; metal avg `-0.0404` n `20`; unknown avg `2.7659` n `1262`
- 1h: commodity avg `-0.198` n `13`; crypto_alt avg `-0.2121` n `239`; crypto_major avg `-0.0115` n `8`; equity avg `0.673` n `161`; fx avg `0.001` n `6`; index avg `0.0921` n `27`; metal avg `-0.0701` n `20`; unknown avg `2.6248` n `1243`
- 4h: commodity avg `0.2373` n `13`; crypto_alt avg `0.7553` n `239`; crypto_major avg `1.0795` n `8`; equity avg `1.3454` n `161`; fx avg `-0.0154` n `6`; index avg `0.118` n `27`; metal avg `-0.299` n `20`; unknown avg `1.9643` n `1225`
- 24h: commodity avg `0.7625` n `13`; crypto_alt avg `1.9176` n `239`; crypto_major avg `2.672` n `8`; equity avg `5.7982` n `161`; fx avg `-0.1015` n `6`; index avg `0.5242` n `27`; metal avg `0.3139` n `20`; unknown avg `4.7948` n `1153`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1547`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1357`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1205`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1147`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1133`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.11`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1098`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1081`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0991`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0974`, n `668`, weak_sample_signal
