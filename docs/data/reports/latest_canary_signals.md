# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-01T19:37:27.607109+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0415` n `13`; crypto_alt avg `-0.3154` n `234`; crypto_major avg `-0.2337` n `8`; equity avg `-0.0336` n `142`; fx avg `0.0086` n `6`; index avg `-0.0006` n `26`; metal avg `-0.0121` n `20`; unknown avg `-0.6897` n `975`
- 1h: commodity avg `0.0907` n `13`; crypto_alt avg `-0.8565` n `234`; crypto_major avg `-0.6657` n `8`; equity avg `-0.05` n `142`; fx avg `0.0089` n `6`; index avg `0.0025` n `26`; metal avg `0.0208` n `20`; unknown avg `0.4519` n `973`
- 4h: commodity avg `0.0586` n `13`; crypto_alt avg `0.4328` n `234`; crypto_major avg `0.3434` n `8`; equity avg `1.1193` n `142`; fx avg `0.0132` n `6`; index avg `0.2407` n `26`; metal avg `0.173` n `20`; unknown avg `1.397` n `967`
- 24h: commodity avg `0.0672` n `13`; crypto_alt avg `-0.5534` n `234`; crypto_major avg `-0.218` n `8`; equity avg `0.8658` n `142`; fx avg `-0.0878` n `6`; index avg `0.1491` n `26`; metal avg `-0.0147` n `20`; unknown avg `0.4452` n `840`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1762`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1578`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1226`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1204`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1184`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1153`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0979`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0935`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0885`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0867`, n `668`, weak_sample_signal
