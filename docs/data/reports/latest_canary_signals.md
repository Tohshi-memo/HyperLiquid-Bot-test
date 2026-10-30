# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-30T20:22:31.858162+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0238` n `13`; crypto_alt avg `-0.3528` n `238`; crypto_major avg `-0.2071` n `8`; equity avg `0.0974` n `156`; fx avg `0.0028` n `6`; index avg `-0.0005` n `27`; metal avg `-0.0739` n `20`; unknown avg `0.1412` n `1211`
- 1h: commodity avg `-0.1565` n `13`; crypto_alt avg `0.4335` n `238`; crypto_major avg `0.2837` n `8`; equity avg `0.7798` n `156`; fx avg `-0.0185` n `6`; index avg `0.1066` n `27`; metal avg `0.063` n `20`; unknown avg `0.9451` n `1169`
- 4h: commodity avg `-0.2527` n `13`; crypto_alt avg `-0.2254` n `238`; crypto_major avg `-0.403` n `8`; equity avg `0.1171` n `156`; fx avg `-0.0156` n `6`; index avg `-0.0026` n `27`; metal avg `-0.0813` n `20`; unknown avg `0.6404` n `1171`
- 24h: commodity avg `0.1059` n `13`; crypto_alt avg `-3.3501` n `238`; crypto_major avg `-3.4272` n `8`; equity avg `-4.1461` n `156`; fx avg `-0.1081` n `6`; index avg `-0.3342` n `27`; metal avg `-1.0335` n `20`; unknown avg `1.8603` n `1008`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1695`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1626`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1571`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1541`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.138`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1298`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1219`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1149`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0899`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0765`, n `668`, weak_sample_signal
