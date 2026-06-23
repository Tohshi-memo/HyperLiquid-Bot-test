# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-23T12:22:34.859406+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0195` n `12`; crypto_alt avg `-0.1396` n `228`; crypto_major avg `-0.1982` n `8`; equity avg `-0.3884` n `86`; fx avg `-0.0207` n `6`; index avg `-0.0738` n `23`; metal avg `-0.1167` n `20`; unknown avg `-0.1537` n `764`
- 1h: commodity avg `-0.0807` n `12`; crypto_alt avg `-0.0275` n `228`; crypto_major avg `-0.1371` n `8`; equity avg `-0.1141` n `86`; fx avg `-0.0405` n `6`; index avg `-0.0205` n `23`; metal avg `-0.166` n `20`; unknown avg `0.0506` n `764`
- 4h: commodity avg `-0.1134` n `12`; crypto_alt avg `0.7169` n `228`; crypto_major avg `0.1397` n `8`; equity avg `0.5121` n `86`; fx avg `-0.0596` n `6`; index avg `0.0022` n `23`; metal avg `-0.0213` n `20`; unknown avg `-0.3816` n `764`
- 24h: commodity avg `-0.5029` n `12`; crypto_alt avg `-4.4598` n `228`; crypto_major avg `-4.5516` n `8`; equity avg `-4.5318` n `85`; fx avg `-0.1926` n `6`; index avg `-0.9634` n `23`; metal avg `-1.4679` n `20`; unknown avg `0.1209` n `604`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1511`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1337`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1285`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1111`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0798`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0742`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.069`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0674`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.066`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0623`, n `668`, weak_sample_signal
