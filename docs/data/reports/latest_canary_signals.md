# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-14T01:07:25.928021+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0058` n `13`; crypto_alt avg `0.0019` n `239`; crypto_major avg `-0.0519` n `8`; equity avg `0.0027` n `162`; fx avg `-0.0034` n `6`; index avg `-0.0033` n `27`; metal avg `-0.0014` n `20`; unknown avg `4.3767` n `1256`
- 1h: commodity avg `0.0583` n `13`; crypto_alt avg `-0.3121` n `239`; crypto_major avg `-0.3098` n `8`; equity avg `-0.1271` n `162`; fx avg `-0.0167` n `6`; index avg `-0.0978` n `27`; metal avg `0.0003` n `20`; unknown avg `4.3048` n `1260`
- 4h: commodity avg `0.0367` n `13`; crypto_alt avg `-0.5284` n `239`; crypto_major avg `-0.9543` n `8`; equity avg `-0.6266` n `162`; fx avg `-0.0492` n `6`; index avg `-0.0139` n `27`; metal avg `0.0126` n `20`; unknown avg `0.9534` n `1200`
- 24h: commodity avg `-0.1604` n `13`; crypto_alt avg `-1.5563` n `239`; crypto_major avg `-2.8719` n `8`; equity avg `-3.9475` n `162`; fx avg `-0.0881` n `6`; index avg `-0.3183` n `27`; metal avg `-0.3975` n `20`; unknown avg `59.8054` n `1036`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1193`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.117`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1143`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1134`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.112`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1078`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1069`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0964`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0933`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0912`, n `668`, weak_sample_signal
