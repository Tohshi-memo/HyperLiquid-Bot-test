# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-30T21:37:31.439996+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0449` n `13`; crypto_alt avg `0.2281` n `238`; crypto_major avg `0.0502` n `8`; equity avg `0.0074` n `156`; fx avg `-0.013` n `6`; index avg `0.0262` n `27`; metal avg `0.0079` n `20`; unknown avg `0.0368` n `1261`
- 1h: commodity avg `-0.0238` n `13`; crypto_alt avg `0.7165` n `238`; crypto_major avg `0.064` n `8`; equity avg `-0.0047` n `156`; fx avg `-0.0205` n `6`; index avg `0.017` n `27`; metal avg `0.0328` n `20`; unknown avg `0.0488` n `1239`
- 4h: commodity avg `-0.374` n `13`; crypto_alt avg `0.6972` n `238`; crypto_major avg `-0.083` n `8`; equity avg `0.9546` n `156`; fx avg `-0.0088` n `6`; index avg `0.0831` n `27`; metal avg `0.0328` n `20`; unknown avg `1.2344` n `1149`
- 24h: commodity avg `0.1004` n `13`; crypto_alt avg `-0.6333` n `238`; crypto_major avg `-2.2716` n `8`; equity avg `-3.2773` n `156`; fx avg `-0.1147` n `6`; index avg `-0.2979` n `27`; metal avg `-0.9801` n `20`; unknown avg `1.9959` n `1014`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1701`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1632`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1489`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1449`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1388`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1235`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1216`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1092`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0859`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0737`, n `668`, weak_sample_signal
