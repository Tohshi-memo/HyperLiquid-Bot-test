# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-30T21:07:25.388916+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0151` n `13`; crypto_alt avg `0.0261` n `238`; crypto_major avg `-0.0838` n `8`; equity avg `0.0174` n `156`; fx avg `0.0222` n `6`; index avg `0.0201` n `27`; metal avg `0.0269` n `20`; unknown avg `-0.0666` n `1239`
- 1h: commodity avg `-0.0682` n `13`; crypto_alt avg `-0.0679` n `238`; crypto_major avg `-0.1483` n `8`; equity avg `0.1074` n `156`; fx avg `0.04` n `6`; index avg `-0.0052` n `27`; metal avg `-0.0733` n `20`; unknown avg `0.1495` n `1181`
- 4h: commodity avg `-0.4038` n `13`; crypto_alt avg `0.0641` n `238`; crypto_major avg `-0.2833` n `8`; equity avg `0.731` n `156`; fx avg `0.0296` n `6`; index avg `0.0506` n `27`; metal avg `-0.0625` n `20`; unknown avg `1.4037` n `1149`
- 24h: commodity avg `0.0467` n `13`; crypto_alt avg `-0.2318` n `238`; crypto_major avg `-1.0872` n `8`; equity avg `-3.4237` n `156`; fx avg `-0.0757` n `6`; index avg `-0.3035` n `27`; metal avg `-0.9745` n `20`; unknown avg `2.2124` n `1014`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1728`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1652`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1496`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1457`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1416`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1239`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1228`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1103`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0875`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0738`, n `668`, weak_sample_signal
