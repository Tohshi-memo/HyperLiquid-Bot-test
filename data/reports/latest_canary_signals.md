# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-14T07:33:22.289412+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0108` n `13`; crypto_alt avg `0.322` n `239`; crypto_major avg `0.302` n `8`; equity avg `0.0688` n `162`; fx avg `0.0042` n `6`; index avg `0.0028` n `27`; metal avg `0.0034` n `20`; unknown avg `0.5173` n `1260`
- 1h: commodity avg `0.0228` n `13`; crypto_alt avg `-0.6494` n `239`; crypto_major avg `-0.2236` n `8`; equity avg `-0.0301` n `162`; fx avg `-0.0047` n `6`; index avg `-0.0042` n `27`; metal avg `0.0084` n `20`; unknown avg `11.2942` n `1254`
- 4h: commodity avg `0.0256` n `13`; crypto_alt avg `-0.5633` n `239`; crypto_major avg `0.2937` n `8`; equity avg `0.0793` n `162`; fx avg `0.0008` n `6`; index avg `0.0069` n `27`; metal avg `0.0092` n `20`; unknown avg `5.2646` n `1216`
- 24h: commodity avg `-0.1033` n `13`; crypto_alt avg `-3.0519` n `239`; crypto_major avg `-2.9574` n `8`; equity avg `-2.6646` n `162`; fx avg `-0.1358` n `6`; index avg `-0.2151` n `27`; metal avg `-0.3778` n `20`; unknown avg `64.7634` n `1018`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1242`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1205`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1182`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.116`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1144`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1116`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1098`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1016`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0948`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0926`, n `668`, weak_sample_signal
