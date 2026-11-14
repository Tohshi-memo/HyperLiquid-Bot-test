# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-14T00:52:30.158925+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.2088` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0288` n `13`; crypto_alt avg `0.1165` n `239`; crypto_major avg `0.0307` n `8`; equity avg `-0.0592` n `162`; fx avg `0.0006` n `6`; index avg `0.0033` n `27`; metal avg `0.0052` n `20`; unknown avg `0.2501` n `1262`
- 1h: commodity avg `0.078` n `13`; crypto_alt avg `-0.0403` n `239`; crypto_major avg `0.1022` n `8`; equity avg `-0.038` n `162`; fx avg `0.0004` n `6`; index avg `-0.0897` n `27`; metal avg `-0.0001` n `20`; unknown avg `0.3296` n `1254`
- 4h: commodity avg `0.0955` n `13`; crypto_alt avg `-0.8356` n `239`; crypto_major avg `-1.2824` n `8`; equity avg `-1.2333` n `162`; fx avg `-0.026` n `6`; index avg `-0.0736` n `27`; metal avg `-0.0292` n `20`; unknown avg `2.8339` n `1168`
- 24h: commodity avg `-0.1758` n `13`; crypto_alt avg `-1.4665` n `239`; crypto_major avg `-2.8471` n `8`; equity avg `-3.9322` n `162`; fx avg `-0.1112` n `6`; index avg `-0.318` n `27`; metal avg `-0.3588` n `20`; unknown avg `60.0765` n `1036`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.119`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.117`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1156`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1129`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1114`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1059`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1031`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0957`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0934`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0914`, n `668`, weak_sample_signal
