# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-14T11:07:25.906919+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0019` n `13`; crypto_alt avg `-0.0364` n `239`; crypto_major avg `-0.1369` n `8`; equity avg `-0.0363` n `162`; fx avg `0.0038` n `6`; index avg `-0.0014` n `27`; metal avg `-0.0054` n `20`; unknown avg `0.2625` n `1256`
- 1h: commodity avg `-0.0014` n `13`; crypto_alt avg `-0.5605` n `239`; crypto_major avg `-0.1927` n `8`; equity avg `-0.0405` n `162`; fx avg `-0.001` n `6`; index avg `-0.0115` n `27`; metal avg `-0.0084` n `20`; unknown avg `80.3413` n `1244`
- 4h: commodity avg `-0.0275` n `13`; crypto_alt avg `-0.8399` n `239`; crypto_major avg `-0.2783` n `8`; equity avg `0.0211` n `162`; fx avg `0.0014` n `6`; index avg `0.0028` n `27`; metal avg `0.019` n `20`; unknown avg `85.8361` n `1168`
- 24h: commodity avg `-0.1656` n `13`; crypto_alt avg `-3.3467` n `239`; crypto_major avg `-3.4609` n `8`; equity avg `-3.1024` n `162`; fx avg `-0.1128` n `6`; index avg `-0.2769` n `27`; metal avg `-0.2987` n `20`; unknown avg `1.5717` n `1096`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1297`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1234`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1184`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1168`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1146`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1089`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1088`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1076`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.094`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0915`, n `668`, weak_sample_signal
