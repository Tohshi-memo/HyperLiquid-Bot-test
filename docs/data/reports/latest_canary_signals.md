# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-01T07:37:26.302277+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0145` n `13`; crypto_alt avg `0.1298` n `238`; crypto_major avg `0.0943` n `8`; equity avg `0.0293` n `156`; fx avg `0.0116` n `6`; index avg `-0.0002` n `27`; metal avg `0.0047` n `20`; unknown avg `0.2796` n `1263`
- 1h: commodity avg `0.0039` n `13`; crypto_alt avg `0.0619` n `238`; crypto_major avg `-0.0475` n `8`; equity avg `-0.0017` n `156`; fx avg `-0.0041` n `6`; index avg `0.0079` n `27`; metal avg `-0.006` n `20`; unknown avg `0.649` n `1257`
- 4h: commodity avg `-0.0228` n `13`; crypto_alt avg `0.2642` n `238`; crypto_major avg `0.0273` n `8`; equity avg `0.1718` n `156`; fx avg `0.0008` n `6`; index avg `0.0235` n `27`; metal avg `0.0169` n `20`; unknown avg `1.1963` n `1230`
- 24h: commodity avg `0.0044` n `13`; crypto_alt avg `0.8249` n `238`; crypto_major avg `0.3838` n `8`; equity avg `0.3071` n `156`; fx avg `-0.005` n `6`; index avg `0.0103` n `27`; metal avg `0.0685` n `20`; unknown avg `2.8297` n `996`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `0.1458`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1444`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1439`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1433`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1359`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1163`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1122`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1007`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0905`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0823`, n `668`, weak_sample_signal
