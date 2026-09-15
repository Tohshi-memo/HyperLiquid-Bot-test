# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-15T04:37:35.889909+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0089` n `12`; crypto_alt avg `-0.1718` n `233`; crypto_major avg `-0.2028` n `8`; equity avg `-0.1951` n `136`; fx avg `-0.0158` n `6`; index avg `-0.0355` n `27`; metal avg `-0.0221` n `20`; unknown avg `0.3486` n `902`
- 1h: commodity avg `0.0457` n `12`; crypto_alt avg `-0.263` n `233`; crypto_major avg `-0.3774` n `8`; equity avg `-0.4317` n `136`; fx avg `-0.0132` n `6`; index avg `-0.0971` n `27`; metal avg `-0.0691` n `20`; unknown avg `0.352` n `892`
- 4h: commodity avg `0.0535` n `12`; crypto_alt avg `-0.8496` n `233`; crypto_major avg `-0.6914` n `8`; equity avg `-0.597` n `136`; fx avg `0.0389` n `6`; index avg `-0.1108` n `27`; metal avg `0.1727` n `20`; unknown avg `0.1285` n `890`
- 24h: commodity avg `0.0192` n `12`; crypto_alt avg `-1.0518` n `233`; crypto_major avg `-0.1122` n `8`; equity avg `-0.4892` n `136`; fx avg `0.108` n `6`; index avg `-0.0946` n `27`; metal avg `-0.2694` n `20`; unknown avg `5.0086` n `788`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1255`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1107`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.104`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0992`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0856`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0845`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0826`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0729`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0686`, n `668`, weak_sample_signal
