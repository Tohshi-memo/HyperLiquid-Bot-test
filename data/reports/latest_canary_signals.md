# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-01T23:37:36.563210+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0109` n `13`; crypto_alt avg `0.0672` n `234`; crypto_major avg `0.0497` n `8`; equity avg `-0.0146` n `142`; fx avg `-0.0054` n `6`; index avg `-0.0239` n `26`; metal avg `-0.0021` n `20`; unknown avg `0.0855` n `985`
- 1h: commodity avg `-0.0397` n `13`; crypto_alt avg `0.2083` n `234`; crypto_major avg `0.082` n `8`; equity avg `0.0732` n `142`; fx avg `-0.0261` n `6`; index avg `-0.0041` n `26`; metal avg `0.035` n `20`; unknown avg `-0.1009` n `983`
- 4h: commodity avg `-0.0849` n `13`; crypto_alt avg `0.3361` n `234`; crypto_major avg `0.2395` n `8`; equity avg `0.1396` n `142`; fx avg `-0.0143` n `6`; index avg `0.0019` n `26`; metal avg `0.0343` n `20`; unknown avg `-0.173` n `891`
- 24h: commodity avg `0.0953` n `13`; crypto_alt avg `-0.6962` n `234`; crypto_major avg `-0.2331` n `8`; equity avg `0.9711` n `142`; fx avg `-0.134` n `6`; index avg `0.1253` n `26`; metal avg `0.0307` n `20`; unknown avg `0.2071` n `816`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.179`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1581`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1229`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1169`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1168`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1153`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0949`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0947`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0933`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0871`, n `668`, weak_sample_signal
