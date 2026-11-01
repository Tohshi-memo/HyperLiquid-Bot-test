# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-01T00:22:26.835739+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0119` n `13`; crypto_alt avg `-0.1754` n `238`; crypto_major avg `-0.0496` n `8`; equity avg `0.0002` n `156`; fx avg `0.0` n `6`; index avg `0.0073` n `27`; metal avg `0.0001` n `20`; unknown avg `-0.0168` n `1228`
- 1h: commodity avg `0.0732` n `13`; crypto_alt avg `-0.0764` n `238`; crypto_major avg `0.0522` n `8`; equity avg `-0.0068` n `156`; fx avg `-0.0034` n `6`; index avg `-0.0012` n `27`; metal avg `0.0014` n `20`; unknown avg `0.1743` n `1216`
- 4h: commodity avg `0.1369` n `13`; crypto_alt avg `-0.1322` n `238`; crypto_major avg `-0.1474` n `8`; equity avg `-0.0181` n `156`; fx avg `-0.0072` n `6`; index avg `0.0105` n `27`; metal avg `0.0096` n `20`; unknown avg `0.6054` n `1084`
- 24h: commodity avg `0.0831` n `13`; crypto_alt avg `-1.0769` n `238`; crypto_major avg `-0.599` n `8`; equity avg `-0.0446` n `156`; fx avg `0.0061` n `6`; index avg `-0.0641` n `27`; metal avg `0.0344` n `20`; unknown avg `1.1339` n `1010`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.145`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1419`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1403`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.136`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1291`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1149`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1137`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1051`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0863`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0849`, n `668`, weak_sample_signal
