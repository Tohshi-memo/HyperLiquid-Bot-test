# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-11T16:52:30.183537+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0632` n `13`; crypto_alt avg `-0.0766` n `239`; crypto_major avg `-0.1554` n `8`; equity avg `0.1445` n `161`; fx avg `-0.0028` n `6`; index avg `0.0099` n `27`; metal avg `-0.0606` n `20`; unknown avg `0.0942` n `1262`
- 1h: commodity avg `-0.211` n `13`; crypto_alt avg `-0.0788` n `239`; crypto_major avg `0.103` n `8`; equity avg `0.4876` n `161`; fx avg `-0.0072` n `6`; index avg `0.0491` n `27`; metal avg `-0.0881` n `20`; unknown avg `0.0611` n `1245`
- 4h: commodity avg `0.1534` n `13`; crypto_alt avg `0.5375` n `239`; crypto_major avg `0.7021` n `8`; equity avg `1.599` n `161`; fx avg `-0.0306` n `6`; index avg `0.1369` n `27`; metal avg `-0.4001` n `20`; unknown avg `-0.0974` n `1225`
- 24h: commodity avg `0.6268` n `13`; crypto_alt avg `1.7304` n `239`; crypto_major avg `2.2675` n `8`; equity avg `6.4897` n `161`; fx avg `-0.1108` n `6`; index avg `0.5745` n `27`; metal avg `0.2374` n `20`; unknown avg `2.1492` n `1153`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.136`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1213`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1153`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1141`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1099`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1098`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.099`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0973`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0943`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0897`, n `668`, weak_sample_signal
