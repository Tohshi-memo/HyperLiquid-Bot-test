# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-13T01:22:33.424449+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0442` n `12`; crypto_alt avg `0.1278` n `233`; crypto_major avg `0.069` n `8`; equity avg `-0.0012` n `136`; fx avg `-0.0021` n `6`; index avg `-0.0004` n `26`; metal avg `0.0065` n `20`; unknown avg `0.0757` n `838`
- 1h: commodity avg `-0.0166` n `12`; crypto_alt avg `0.2657` n `233`; crypto_major avg `0.1277` n `8`; equity avg `0.0095` n `136`; fx avg `-0.0015` n `6`; index avg `0.003` n `26`; metal avg `0.0074` n `20`; unknown avg `42.0811` n `830`
- 4h: commodity avg `-0.0186` n `12`; crypto_alt avg `0.5745` n `233`; crypto_major avg `0.1722` n `8`; equity avg `-0.026` n `136`; fx avg `-0.0004` n `6`; index avg `-0.0115` n `26`; metal avg `0.0021` n `20`; unknown avg `7.2678` n `804`
- 24h: commodity avg `-0.0699` n `12`; crypto_alt avg `1.1275` n `233`; crypto_major avg `0.2557` n `8`; equity avg `-0.389` n `136`; fx avg `-0.0126` n `6`; index avg `-0.0389` n `26`; metal avg `0.0208` n `20`; unknown avg `0.8879` n `724`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0729`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0722`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0654`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0648`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0631`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0579`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0513`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0502`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0498`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0438`, n `668`, weak_sample_signal
