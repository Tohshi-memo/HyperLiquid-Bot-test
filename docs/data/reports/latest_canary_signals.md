# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-06T20:22:42.729587+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0047` n `12`; crypto_alt avg `0.0145` n `229`; crypto_major avg `-0.022` n `8`; equity avg `-0.0144` n `91`; fx avg `-0.0008` n `6`; index avg `0.0044` n `25`; metal avg `-0.0026` n `20`; unknown avg `-0.2103` n `763`
- 1h: commodity avg `-0.022` n `12`; crypto_alt avg `-0.1554` n `229`; crypto_major avg `-0.2417` n `8`; equity avg `-0.1052` n `91`; fx avg `0.0017` n `6`; index avg `-0.033` n `25`; metal avg `-0.0394` n `20`; unknown avg `-0.1777` n `763`
- 4h: commodity avg `0.0606` n `12`; crypto_alt avg `-0.1587` n `229`; crypto_major avg `-0.1352` n `8`; equity avg `-0.4544` n `91`; fx avg `-0.0034` n `6`; index avg `-0.0716` n `25`; metal avg `0.1848` n `20`; unknown avg `-0.3228` n `763`
- 24h: commodity avg `0.0567` n `12`; crypto_alt avg `0.7` n `229`; crypto_major avg `0.3661` n `8`; equity avg `-0.6737` n `90`; fx avg `0.1984` n `6`; index avg `0.0241` n `25`; metal avg `-0.2307` n `20`; unknown avg `0.2209` n `729`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1185`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0967`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0891`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0759`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0732`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0727`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0712`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0702`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0616`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0612`, n `668`, weak_sample_signal
