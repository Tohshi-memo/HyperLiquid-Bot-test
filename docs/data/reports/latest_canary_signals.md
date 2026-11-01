# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-01T08:22:26.960966+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0001` n `13`; crypto_alt avg `-0.0966` n `238`; crypto_major avg `-0.1253` n `8`; equity avg `-0.0114` n `156`; fx avg `-0.006` n `6`; index avg `-0.0009` n `27`; metal avg `-0.0133` n `20`; unknown avg `0.1226` n `1263`
- 1h: commodity avg `0.0149` n `13`; crypto_alt avg `-0.0057` n `238`; crypto_major avg `0.0493` n `8`; equity avg `0.0283` n `156`; fx avg `0.0076` n `6`; index avg `0.0002` n `27`; metal avg `-0.0023` n `20`; unknown avg `0.3794` n `1241`
- 4h: commodity avg `-0.0238` n `13`; crypto_alt avg `0.0923` n `238`; crypto_major avg `-0.0044` n `8`; equity avg `0.1399` n `156`; fx avg `-0.0041` n `6`; index avg `0.0222` n `27`; metal avg `0.0121` n `20`; unknown avg `1.0309` n `1222`
- 24h: commodity avg `-0.001` n `13`; crypto_alt avg `0.8021` n `238`; crypto_major avg `0.4544` n `8`; equity avg `0.3559` n `156`; fx avg `-0.0159` n `6`; index avg `0.0148` n `27`; metal avg `0.076` n `20`; unknown avg `2.6271` n `996`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1462`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1461`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.143`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1425`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.135`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1156`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1119`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1003`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0828`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0824`, n `668`, weak_sample_signal
