# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-01T15:00:03.318288+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0542` n `12`; crypto_alt avg `-0.0944` n `232`; crypto_major avg `-0.1015` n `8`; equity avg `0.1158` n `131`; fx avg `0.0023` n `6`; index avg `-0.0073` n `26`; metal avg `-0.0001` n `20`; unknown avg `-0.104` n `790`
- 1h: commodity avg `0.0491` n `12`; crypto_alt avg `-0.0979` n `232`; crypto_major avg `-0.2166` n `8`; equity avg `0.3278` n `131`; fx avg `-0.0049` n `6`; index avg `0.0588` n `26`; metal avg `-0.0087` n `20`; unknown avg `-0.3153` n `790`
- 4h: commodity avg `-0.0495` n `12`; crypto_alt avg `0.4563` n `232`; crypto_major avg `0.0869` n `8`; equity avg `-0.2565` n `130`; fx avg `-0.0186` n `6`; index avg `0.0487` n `26`; metal avg `-0.0274` n `20`; unknown avg `-0.057` n `790`
- 24h: commodity avg `0.3582` n `12`; crypto_alt avg `1.2583` n `232`; crypto_major avg `0.0251` n `8`; equity avg `-0.8549` n `130`; fx avg `0.0366` n `6`; index avg `-0.14` n `26`; metal avg `-0.5336` n `20`; unknown avg `-0.1296` n `752`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1042`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1025`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0865`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0526`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0471`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0414`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0358`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0331`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0327`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0304`, n `668`, weak_sample_signal
