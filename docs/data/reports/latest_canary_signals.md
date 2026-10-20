# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-20T01:22:30.301925+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0187` n `13`; crypto_alt avg `-0.1935` n `237`; crypto_major avg `-0.057` n `8`; equity avg `-0.0295` n `151`; fx avg `0.0042` n `6`; index avg `-0.0221` n `26`; metal avg `-0.0691` n `20`; unknown avg `-0.027` n `1198`
- 1h: commodity avg `0.1005` n `13`; crypto_alt avg `-0.29` n `237`; crypto_major avg `-0.1235` n `8`; equity avg `-0.1713` n `151`; fx avg `0.0066` n `6`; index avg `-0.0572` n `26`; metal avg `-0.0914` n `20`; unknown avg `-0.3842` n `1196`
- 4h: commodity avg `0.1126` n `13`; crypto_alt avg `-0.3421` n `237`; crypto_major avg `-0.5079` n `8`; equity avg `-1.0361` n `151`; fx avg `-0.0336` n `6`; index avg `-0.2003` n `26`; metal avg `-0.2115` n `20`; unknown avg `-0.1819` n `1178`
- 24h: commodity avg `0.1696` n `13`; crypto_alt avg `-0.567` n `237`; crypto_major avg `-0.727` n `8`; equity avg `-0.9112` n `151`; fx avg `-0.0672` n `6`; index avg `-0.1743` n `26`; metal avg `-0.3518` n `20`; unknown avg `5.0261` n `1012`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.2008`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1462`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1017`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1016`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0918`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0872`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0759`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0696`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.069`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.068`, n `668`, weak_sample_signal
