# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-23T13:37:31.842798+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1175` n `12`; crypto_alt avg `0.4927` n `228`; crypto_major avg `0.2572` n `8`; equity avg `0.359` n `86`; fx avg `-0.0101` n `6`; index avg `0.0126` n `23`; metal avg `0.1119` n `20`; unknown avg `0.3527` n `764`
- 1h: commodity avg `-0.1493` n `12`; crypto_alt avg `0.158` n `228`; crypto_major avg `-0.0406` n `8`; equity avg `0.0947` n `86`; fx avg `-0.0107` n `6`; index avg `-0.053` n `23`; metal avg `0.1032` n `20`; unknown avg `0.0837` n `764`
- 4h: commodity avg `-0.1912` n `12`; crypto_alt avg `0.5039` n `228`; crypto_major avg `0.1872` n `8`; equity avg `-0.0405` n `86`; fx avg `-0.0656` n `6`; index avg `-0.1651` n `23`; metal avg `-0.0675` n `20`; unknown avg `-0.0121` n `764`
- 24h: commodity avg `-0.5064` n `12`; crypto_alt avg `-4.6203` n `228`; crypto_major avg `-5.3741` n `8`; equity avg `-4.6763` n `85`; fx avg `-0.1781` n `6`; index avg `-1.0845` n `23`; metal avg `-1.2828` n `20`; unknown avg `0.0267` n `604`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1566`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.137`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1332`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1173`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0824`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0802`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0733`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0673`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0625`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.06`, n `668`, weak_sample_signal
