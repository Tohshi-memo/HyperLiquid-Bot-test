# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-14T03:07:33.484031+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0166` n `13`; crypto_alt avg `-0.1169` n `239`; crypto_major avg `-0.1995` n `8`; equity avg `-0.0079` n `162`; fx avg `-0.0068` n `6`; index avg `-0.0076` n `27`; metal avg `0.0042` n `20`; unknown avg `0.1233` n `1256`
- 1h: commodity avg `-0.0034` n `13`; crypto_alt avg `-0.5543` n `239`; crypto_major avg `-0.7818` n `8`; equity avg `-0.1324` n `162`; fx avg `0.0069` n `6`; index avg `-0.0224` n `27`; metal avg `-0.0395` n `20`; unknown avg `1.1739` n `1260`
- 4h: commodity avg `0.068` n `13`; crypto_alt avg `-0.707` n `239`; crypto_major avg `-0.95` n `8`; equity avg `-0.1767` n `162`; fx avg `-0.0363` n `6`; index avg `-0.0292` n `27`; metal avg `-0.023` n `20`; unknown avg `7.7037` n `1250`
- 24h: commodity avg `-0.1062` n `13`; crypto_alt avg `-1.5117` n `239`; crypto_major avg `-2.9304` n `8`; equity avg `-3.5196` n `162`; fx avg `-0.0806` n `6`; index avg `-0.3439` n `27`; metal avg `-0.6356` n `20`; unknown avg `63.8217` n `1036`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1217`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1196`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1181`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1144`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1142`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1085`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1073`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1035`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0949`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0924`, n `668`, weak_sample_signal
