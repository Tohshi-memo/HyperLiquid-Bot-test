# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-13T20:37:24.496659+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0089` n `13`; crypto_alt avg `-0.4088` n `239`; crypto_major avg `-0.2561` n `8`; equity avg `-0.1582` n `162`; fx avg `-0.005` n `6`; index avg `-0.013` n `27`; metal avg `-0.0272` n `20`; unknown avg `9.6248` n `1262`
- 1h: commodity avg `0.0428` n `13`; crypto_alt avg `-0.3607` n `239`; crypto_major avg `-0.1786` n `8`; equity avg `-0.0672` n `162`; fx avg `0.0039` n `6`; index avg `0.0018` n `27`; metal avg `-0.0258` n `20`; unknown avg `10.0736` n `1246`
- 4h: commodity avg `-0.0077` n `13`; crypto_alt avg `-0.1367` n `239`; crypto_major avg `0.5158` n `8`; equity avg `0.9656` n `162`; fx avg `-0.0469` n `6`; index avg `0.1136` n `27`; metal avg `-0.1369` n `20`; unknown avg `7.7796` n `1246`
- 24h: commodity avg `-0.3303` n `13`; crypto_alt avg `-0.1682` n `239`; crypto_major avg `-1.362` n `8`; equity avg `-2.0196` n `162`; fx avg `-0.0824` n `6`; index avg `-0.1463` n `27`; metal avg `-0.3` n `20`; unknown avg `6.3995` n `1085`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1256`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1186`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1117`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1059`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1044`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1007`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1003`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0861`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0849`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0822`, n `668`, weak_sample_signal
