# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-09T16:07:32.877598+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0428` n `12`; crypto_alt avg `0.1165` n `233`; crypto_major avg `0.0816` n `8`; equity avg `-0.02` n `134`; fx avg `-0.0215` n `6`; index avg `-0.0254` n `26`; metal avg `-0.0342` n `20`; unknown avg `-0.2175` n `795`
- 1h: commodity avg `0.0056` n `12`; crypto_alt avg `-0.2201` n `233`; crypto_major avg `-0.0303` n `8`; equity avg `-0.1207` n `134`; fx avg `-0.0264` n `6`; index avg `-0.0394` n `26`; metal avg `0.0446` n `20`; unknown avg `0.1739` n `795`
- 4h: commodity avg `0.0876` n `12`; crypto_alt avg `-1.097` n `233`; crypto_major avg `-0.9745` n `8`; equity avg `0.2806` n `134`; fx avg `-0.0031` n `6`; index avg `-0.0052` n `26`; metal avg `0.3429` n `20`; unknown avg `6.8471` n `766`
- 24h: commodity avg `0.6179` n `12`; crypto_alt avg `-1.6335` n `233`; crypto_major avg `-0.5563` n `8`; equity avg `-0.6625` n `134`; fx avg `-0.1068` n `6`; index avg `-0.2417` n `26`; metal avg `0.3497` n `20`; unknown avg `5.0209` n `685`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `0.115`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1105`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0924`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0867`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0862`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0859`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0796`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0791`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0791`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0772`, n `668`, weak_sample_signal
