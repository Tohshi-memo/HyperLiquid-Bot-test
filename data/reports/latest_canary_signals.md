# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-21T00:52:26.168210+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0032` n `13`; crypto_alt avg `0.0249` n `239`; crypto_major avg `-0.004` n `8`; equity avg `0.0189` n `166`; fx avg `0.0035` n `6`; index avg `-0.0143` n `27`; metal avg `-0.0037` n `20`; unknown avg `2.4894` n `1262`
- 1h: commodity avg `-0.0118` n `13`; crypto_alt avg `-0.145` n `239`; crypto_major avg `0.1421` n `8`; equity avg `0.1495` n `166`; fx avg `0.0064` n `6`; index avg `-0.0002` n `27`; metal avg `0.009` n `20`; unknown avg `286.6369` n `1250`
- 4h: commodity avg `-0.067` n `13`; crypto_alt avg `1.343` n `239`; crypto_major avg `1.4607` n `8`; equity avg `1.3003` n `166`; fx avg `-0.0179` n `6`; index avg `0.1575` n `27`; metal avg `0.0939` n `20`; unknown avg `0.2458` n `1200`
- 24h: commodity avg `0.2862` n `13`; crypto_alt avg `-4.8048` n `239`; crypto_major avg `-5.4057` n `8`; equity avg `-5.0005` n `166`; fx avg `-0.0503` n `6`; index avg `-0.5245` n `27`; metal avg `-0.5585` n `20`; unknown avg `12.3181` n `1121`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1615`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.151`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1449`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1206`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0951`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0932`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0924`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0852`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0791`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0775`, n `668`, weak_sample_signal
