# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-31T02:22:26.009449+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1587` n `13`; crypto_alt avg `0.0686` n `238`; crypto_major avg `0.1136` n `8`; equity avg `0.0138` n `156`; fx avg `-0.003` n `6`; index avg `-0.0007` n `27`; metal avg `0.005` n `20`; unknown avg `-0.2224` n `1262`
- 1h: commodity avg `0.1545` n `13`; crypto_alt avg `-0.2726` n `238`; crypto_major avg `-0.0555` n `8`; equity avg `-0.0741` n `156`; fx avg `-0.0034` n `6`; index avg `-0.0087` n `27`; metal avg `-0.0051` n `20`; unknown avg `-0.3499` n `1256`
- 4h: commodity avg `0.0723` n `13`; crypto_alt avg `0.4156` n `238`; crypto_major avg `0.6799` n `8`; equity avg `0.1759` n `156`; fx avg `0.016` n `6`; index avg `0.0066` n `27`; metal avg `0.0051` n `20`; unknown avg `-0.1178` n `1249`
- 24h: commodity avg `-0.1273` n `13`; crypto_alt avg `3.8448` n `238`; crypto_major avg `0.9368` n `8`; equity avg `-1.9556` n `156`; fx avg `-0.1227` n `6`; index avg `-0.0717` n `27`; metal avg `-0.7051` n `20`; unknown avg `-0.8216` n `1018`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.153`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1472`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1365`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1328`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1235`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1221`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1154`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1113`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0927`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0775`, n `668`, weak_sample_signal
