# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-19T18:07:32.500997+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0608` n `13`; crypto_alt avg `0.3333` n `237`; crypto_major avg `0.3243` n `8`; equity avg `0.0468` n `151`; fx avg `-0.0099` n `6`; index avg `0.0121` n `26`; metal avg `0.043` n `20`; unknown avg `0.6179` n `1194`
- 1h: commodity avg `0.0489` n `13`; crypto_alt avg `-0.1424` n `237`; crypto_major avg `0.0397` n `8`; equity avg `-0.3121` n `151`; fx avg `0.0155` n `6`; index avg `-0.0225` n `26`; metal avg `0.0759` n `20`; unknown avg `0.401` n `1194`
- 4h: commodity avg `0.3566` n `13`; crypto_alt avg `0.4446` n `237`; crypto_major avg `0.354` n `8`; equity avg `-0.0278` n `151`; fx avg `-0.0038` n `6`; index avg `0.0013` n `26`; metal avg `0.0767` n `20`; unknown avg `0.1674` n `1133`
- 24h: commodity avg `-0.0058` n `13`; crypto_alt avg `1.4771` n `237`; crypto_major avg `1.5463` n `8`; equity avg `2.6515` n `151`; fx avg `-0.0295` n `6`; index avg `0.5378` n `26`; metal avg `0.144` n `20`; unknown avg `3.5583` n `916`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1913`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1384`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1324`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1271`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0926`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0805`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0789`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0682`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0631`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0629`, n `668`, weak_sample_signal
