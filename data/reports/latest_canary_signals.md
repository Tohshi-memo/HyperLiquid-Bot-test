# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-15T12:52:23.446938+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `1.7679` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0055` n `13`; crypto_alt avg `0.1244` n `239`; crypto_major avg `-0.0212` n `8`; equity avg `0.0089` n `162`; fx avg `-0.0143` n `6`; index avg `-0.0006` n `27`; metal avg `0.0049` n `20`; unknown avg `0.0075` n `1263`
- 1h: commodity avg `0.0122` n `13`; crypto_alt avg `0.4447` n `239`; crypto_major avg `0.1314` n `8`; equity avg `0.0138` n `162`; fx avg `-0.0063` n `6`; index avg `-0.0074` n `27`; metal avg `0.022` n `20`; unknown avg `-0.0428` n `1253`
- 4h: commodity avg `-0.0355` n `13`; crypto_alt avg `1.8701` n `239`; crypto_major avg `1.8564` n `8`; equity avg `0.3969` n `162`; fx avg `-0.0242` n `6`; index avg `0.0405` n `27`; metal avg `0.0885` n `20`; unknown avg `0.2262` n `1253`
- 24h: commodity avg `0.0524` n `13`; crypto_alt avg `-3.1578` n `239`; crypto_major avg `-2.6011` n `8`; equity avg `-0.6474` n `162`; fx avg `-0.0034` n `6`; index avg `-0.0595` n `27`; metal avg `-0.312` n `20`; unknown avg `-0.0593` n `1136`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1198`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1183`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.117`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1133`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1097`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1015`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0933`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0871`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0871`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.082`, n `668`, weak_sample_signal
