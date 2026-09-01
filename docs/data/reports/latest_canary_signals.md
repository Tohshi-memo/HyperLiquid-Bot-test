# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-01T10:07:28.495587+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0264` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0142` n `12`; crypto_alt avg `-0.111` n `232`; crypto_major avg `-0.0981` n `8`; equity avg `-0.0567` n `130`; fx avg `-0.0055` n `6`; index avg `-0.003` n `26`; metal avg `0.0121` n `20`; unknown avg `-0.0662` n `790`
- 1h: commodity avg `-0.0167` n `12`; crypto_alt avg `0.1791` n `232`; crypto_major avg `-0.0219` n `8`; equity avg `0.0518` n `130`; fx avg `0.013` n `6`; index avg `0.0029` n `26`; metal avg `-0.0384` n `20`; unknown avg `-0.1353` n `790`
- 4h: commodity avg `0.1237` n `12`; crypto_alt avg `-1.3612` n `232`; crypto_major avg `-1.3443` n `8`; equity avg `-1.5284` n `130`; fx avg `0.0174` n `6`; index avg `-0.3179` n `26`; metal avg `-0.662` n `20`; unknown avg `-0.1167` n `788`
- 24h: commodity avg `0.2887` n `12`; crypto_alt avg `0.4622` n `232`; crypto_major avg `0.0428` n `8`; equity avg `-0.525` n `130`; fx avg `0.08` n `6`; index avg `-0.2508` n `26`; metal avg `-0.7803` n `20`; unknown avg `-0.6965` n `750`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1049`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.104`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0926`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0617`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0491`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.045`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0326`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0325`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0309`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0294`, n `668`, weak_sample_signal
