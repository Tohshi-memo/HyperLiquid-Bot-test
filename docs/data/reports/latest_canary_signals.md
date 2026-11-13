# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-13T19:52:26.861517+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0057` n `13`; crypto_alt avg `-0.0327` n `239`; crypto_major avg `-0.1136` n `8`; equity avg `-0.1894` n `162`; fx avg `0.0054` n `6`; index avg `-0.0195` n `27`; metal avg `-0.0275` n `20`; unknown avg `0.8737` n `1262`
- 1h: commodity avg `-0.0795` n `13`; crypto_alt avg `0.188` n `239`; crypto_major avg `0.1183` n `8`; equity avg `-0.0224` n `162`; fx avg `-0.0013` n `6`; index avg `0.0057` n `27`; metal avg `-0.0874` n `20`; unknown avg `0.3299` n `1260`
- 4h: commodity avg `-0.124` n `13`; crypto_alt avg `0.3667` n `239`; crypto_major avg `0.4685` n `8`; equity avg `0.7799` n `162`; fx avg `-0.051` n `6`; index avg `0.0855` n `27`; metal avg `-0.154` n `20`; unknown avg `31.7111` n `1254`
- 24h: commodity avg `-0.397` n `13`; crypto_alt avg `0.0737` n `239`; crypto_major avg `-1.4924` n `8`; equity avg `-2.5435` n `162`; fx avg `-0.0699` n `6`; index avg `-0.1964` n `27`; metal avg `-0.3446` n `20`; unknown avg `0.6932` n `1089`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1282`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1214`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1098`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1061`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1055`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1015`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1012`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0836`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0825`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0825`, n `668`, weak_sample_signal
