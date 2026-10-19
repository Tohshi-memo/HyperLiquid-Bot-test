# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-19T15:22:31.601685+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0694` n `13`; crypto_alt avg `0.469` n `237`; crypto_major avg `0.3523` n `8`; equity avg `0.2266` n `151`; fx avg `-0.0004` n `6`; index avg `0.0482` n `26`; metal avg `-0.0027` n `20`; unknown avg `0.1143` n `1194`
- 1h: commodity avg `0.0768` n `13`; crypto_alt avg `0.8342` n `237`; crypto_major avg `0.6474` n `8`; equity avg `0.3538` n `151`; fx avg `0.0141` n `6`; index avg `0.033` n `26`; metal avg `-0.0004` n `20`; unknown avg `0.0891` n `1189`
- 4h: commodity avg `-0.1789` n `13`; crypto_alt avg `0.9813` n `237`; crypto_major avg `0.3895` n `8`; equity avg `0.4663` n `151`; fx avg `0.0103` n `6`; index avg `0.1073` n `26`; metal avg `-0.2599` n `20`; unknown avg `0.9336` n `1103`
- 24h: commodity avg `-0.3197` n `13`; crypto_alt avg `1.6639` n `237`; crypto_major avg `1.872` n `8`; equity avg `3.5097` n `151`; fx avg `-0.0196` n `6`; index avg `0.658` n `26`; metal avg `0.0884` n `20`; unknown avg `4.4844` n `916`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.2093`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1561`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1323`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.125`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0893`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0793`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0681`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.061`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0599`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0594`, n `668`, weak_sample_signal
