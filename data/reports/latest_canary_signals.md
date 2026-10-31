# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-31T01:37:30.306612+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0094` n `13`; crypto_alt avg `0.1023` n `238`; crypto_major avg `0.0911` n `8`; equity avg `-0.0032` n `156`; fx avg `-0.0105` n `6`; index avg `-0.0019` n `27`; metal avg `0.0067` n `20`; unknown avg `-0.0649` n `1262`
- 1h: commodity avg `-0.0597` n `13`; crypto_alt avg `-0.1827` n `238`; crypto_major avg `0.0625` n `8`; equity avg `0.0215` n `156`; fx avg `-0.0001` n `6`; index avg `-0.0083` n `27`; metal avg `-0.0092` n `20`; unknown avg `7.7425` n `1256`
- 4h: commodity avg `-0.1284` n `13`; crypto_alt avg `0.812` n `238`; crypto_major avg `0.6362` n `8`; equity avg `0.2844` n `156`; fx avg `-0.0007` n `6`; index avg `0.0186` n `27`; metal avg `0.0449` n `20`; unknown avg `4.0816` n `1249`
- 24h: commodity avg `-0.1788` n `13`; crypto_alt avg `4.3449` n `238`; crypto_major avg `1.5097` n `8`; equity avg `-1.8682` n `156`; fx avg `-0.1314` n `6`; index avg `-0.0775` n `27`; metal avg `-0.6803` n `20`; unknown avg `3.8693` n `1018`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1521`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1472`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1346`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.131`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1237`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1213`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1166`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1103`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0954`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0778`, n `668`, weak_sample_signal
