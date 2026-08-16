# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-16T14:43:37.834856+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0109` n `12`; crypto_alt avg `-0.1024` n `230`; crypto_major avg `0.0176` n `8`; equity avg `0.021` n `114`; fx avg `0.0142` n `6`; index avg `0.0007` n `25`; metal avg `0.0042` n `20`; unknown avg `-0.0339` n `791`
- 1h: commodity avg `-0.0033` n `12`; crypto_alt avg `-0.0025` n `230`; crypto_major avg `0.058` n `8`; equity avg `0.0625` n `114`; fx avg `-0.0007` n `6`; index avg `-0.006` n `25`; metal avg `0.0116` n `20`; unknown avg `-0.0352` n `791`
- 4h: commodity avg `-0.0209` n `12`; crypto_alt avg `0.0924` n `230`; crypto_major avg `0.1294` n `8`; equity avg `-0.0425` n `114`; fx avg `-0.0143` n `6`; index avg `0.0048` n `25`; metal avg `0.004` n `20`; unknown avg `-0.0645` n `791`
- 24h: commodity avg `0.0479` n `12`; crypto_alt avg `0.0124` n `230`; crypto_major avg `0.1515` n `8`; equity avg `0.2807` n `114`; fx avg `-0.0127` n `6`; index avg `0.04` n `25`; metal avg `0.0391` n `20`; unknown avg `0.0447` n `759`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2155`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.188`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.174`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.173`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1641`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1568`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1548`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1393`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1326`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.125`, n `668`, weak_sample_signal
