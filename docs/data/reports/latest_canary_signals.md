# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-25T04:22:25.683799+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0017` n `13`; crypto_alt avg `0.0271` n `237`; crypto_major avg `0.0741` n `8`; equity avg `0.0094` n `152`; fx avg `0.0015` n `6`; index avg `-0.0002` n `26`; metal avg `0.0063` n `20`; unknown avg `-0.1006` n `1229`
- 1h: commodity avg `0.0073` n `13`; crypto_alt avg `-0.061` n `237`; crypto_major avg `-0.0159` n `8`; equity avg `0.0313` n `152`; fx avg `0.0152` n `6`; index avg `0.0111` n `26`; metal avg `0.0048` n `20`; unknown avg `1.8549` n `1219`
- 4h: commodity avg `-0.0089` n `13`; crypto_alt avg `-0.3116` n `237`; crypto_major avg `0.3967` n `8`; equity avg `0.1106` n `152`; fx avg `0.0095` n `6`; index avg `0.0319` n `26`; metal avg `0.0092` n `20`; unknown avg `1.4529` n `1205`
- 24h: commodity avg `-0.0137` n `13`; crypto_alt avg `-1.2146` n `237`; crypto_major avg `0.0291` n `8`; equity avg `0.0397` n `152`; fx avg `-0.0285` n `6`; index avg `0.0192` n `26`; metal avg `-0.0735` n `20`; unknown avg `7.5891` n `1060`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1975`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1692`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1633`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1605`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1564`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1554`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1375`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1375`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1167`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1159`, n `668`, weak_sample_signal
