# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-22T16:52:30.745893+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.23` - Polymarket crypto volume is unusually high.
- 4h_crypto_equity_divergence: score `1.5341` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0216` n `13`; crypto_alt avg `-0.9209` n `237`; crypto_major avg `-1.0551` n `8`; equity avg `-0.6588` n `151`; fx avg `-0.004` n `6`; index avg `-0.1023` n `26`; metal avg `-0.0566` n `20`; unknown avg `9.2455` n `1233`
- 1h: commodity avg `0.1104` n `13`; crypto_alt avg `-0.8709` n `237`; crypto_major avg `-1.0451` n `8`; equity avg `-0.8951` n `151`; fx avg `0.0203` n `6`; index avg `-0.1248` n `26`; metal avg `-0.1626` n `20`; unknown avg `5.9497` n `1225`
- 4h: commodity avg `-0.0981` n `13`; crypto_alt avg `-1.6578` n `237`; crypto_major avg `-1.1619` n `8`; equity avg `-2.696` n `151`; fx avg `0.0437` n `6`; index avg `-0.2371` n `26`; metal avg `-0.3515` n `20`; unknown avg `3.1808` n `1083`
- 24h: commodity avg `0.435` n `13`; crypto_alt avg `-5.678` n `237`; crypto_major avg `-4.4445` n `8`; equity avg `-5.2301` n `151`; fx avg `-0.1419` n `6`; index avg `-0.6722` n `26`; metal avg `-1.0079` n `20`; unknown avg `7.6` n `908`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1847`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1677`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1523`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1254`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1173`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1136`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1115`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1088`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1045`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1005`, n `668`, weak_sample_signal
