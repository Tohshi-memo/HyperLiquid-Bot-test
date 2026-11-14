# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-14T07:52:29.140234+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.001` n `13`; crypto_alt avg `-0.1472` n `239`; crypto_major avg `-0.1844` n `8`; equity avg `-0.033` n `162`; fx avg `-0.0079` n `6`; index avg `-0.0063` n `27`; metal avg `-0.0031` n `20`; unknown avg `1.6645` n `1262`
- 1h: commodity avg `0.0214` n `13`; crypto_alt avg `-0.5877` n `239`; crypto_major avg `-0.5414` n `8`; equity avg `-0.0706` n `162`; fx avg `0.0104` n `6`; index avg `-0.0016` n `27`; metal avg `0.0003` n `20`; unknown avg `0.9123` n `1256`
- 4h: commodity avg `0.0521` n `13`; crypto_alt avg `-0.7395` n `239`; crypto_major avg `0.1249` n `8`; equity avg `0.1165` n `162`; fx avg `-0.0035` n `6`; index avg `0.0082` n `27`; metal avg `0.0334` n `20`; unknown avg `1.1548` n `1216`
- 24h: commodity avg `-0.02` n `13`; crypto_alt avg `-2.9982` n `239`; crypto_major avg `-2.9161` n `8`; equity avg `-2.7424` n `162`; fx avg `-0.1559` n `6`; index avg `-0.2262` n `27`; metal avg `-0.4202` n `20`; unknown avg `60.0331` n `1018`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1225`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1208`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1183`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.116`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1144`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1111`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1099`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1013`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0947`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0923`, n `668`, weak_sample_signal
