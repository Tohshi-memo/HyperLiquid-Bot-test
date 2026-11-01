# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-01T09:07:23.331663+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0114` n `13`; crypto_alt avg `-0.0806` n `238`; crypto_major avg `-0.0084` n `8`; equity avg `0.0645` n `156`; fx avg `-0.0103` n `6`; index avg `0.0118` n `27`; metal avg `0.001` n `20`; unknown avg `-0.0476` n `1257`
- 1h: commodity avg `-0.0065` n `13`; crypto_alt avg `0.0534` n `238`; crypto_major avg `0.3295` n `8`; equity avg `0.1557` n `156`; fx avg `-0.0112` n `6`; index avg `0.0123` n `27`; metal avg `-0.0077` n `20`; unknown avg `-0.1092` n `1257`
- 4h: commodity avg `0.0051` n `13`; crypto_alt avg `0.2242` n `238`; crypto_major avg `0.3687` n `8`; equity avg `0.2306` n `156`; fx avg `-0.008` n `6`; index avg `0.0332` n `27`; metal avg `0.0172` n `20`; unknown avg `0.9547` n `1224`
- 24h: commodity avg `-0.0416` n `13`; crypto_alt avg `0.7427` n `238`; crypto_major avg `0.8252` n `8`; equity avg `0.5148` n `156`; fx avg `-0.0154` n `6`; index avg `0.0283` n `27`; metal avg `0.0702` n `20`; unknown avg `2.55` n `996`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1436`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1433`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1432`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1415`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1341`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.113`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1112`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0999`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.083`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0817`, n `668`, weak_sample_signal
