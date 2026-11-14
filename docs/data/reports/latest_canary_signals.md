# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-14T11:37:28.096969+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0088` n `13`; crypto_alt avg `-0.0972` n `239`; crypto_major avg `-0.2104` n `8`; equity avg `-0.031` n `162`; fx avg `0.011` n `6`; index avg `-0.0012` n `27`; metal avg `-0.0028` n `20`; unknown avg `-0.1204` n `1262`
- 1h: commodity avg `-0.031` n `13`; crypto_alt avg `-0.0726` n `239`; crypto_major avg `-0.2144` n `8`; equity avg `-0.0299` n `162`; fx avg `-0.0016` n `6`; index avg `-0.0055` n `27`; metal avg `-0.0085` n `20`; unknown avg `0.3396` n `1258`
- 4h: commodity avg `-0.0777` n `13`; crypto_alt avg `-0.3971` n `239`; crypto_major avg `-0.0181` n `8`; equity avg `0.0419` n `162`; fx avg `-0.0048` n `6`; index avg `-0.0034` n `27`; metal avg `0.0158` n `20`; unknown avg `128.3328` n `1168`
- 24h: commodity avg `-0.1555` n `13`; crypto_alt avg `-3.2213` n `239`; crypto_major avg `-3.505` n `8`; equity avg `-2.9454` n `162`; fx avg `-0.1384` n `6`; index avg `-0.2572` n `27`; metal avg `-0.3323` n `20`; unknown avg `1.7513` n `1096`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1345`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1238`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1191`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.117`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1146`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1104`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1095`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1072`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0944`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0915`, n `668`, weak_sample_signal
