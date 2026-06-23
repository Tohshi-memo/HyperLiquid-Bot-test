# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-23T13:52:34.954605+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1019` n `12`; crypto_alt avg `0.3` n `228`; crypto_major avg `0.1965` n `8`; equity avg `1.0078` n `86`; fx avg `-0.0001` n `6`; index avg `0.1441` n `23`; metal avg `0.1486` n `20`; unknown avg `0.0466` n `764`
- 1h: commodity avg `-0.1064` n `12`; crypto_alt avg `0.746` n `228`; crypto_major avg `0.3777` n `8`; equity avg `1.1177` n `86`; fx avg `-0.0194` n `6`; index avg `0.0939` n `23`; metal avg `0.1801` n `20`; unknown avg `0.2378` n `764`
- 4h: commodity avg `-0.0996` n `12`; crypto_alt avg `0.7573` n `228`; crypto_major avg `0.3391` n `8`; equity avg `0.9816` n `86`; fx avg `-0.0447` n `6`; index avg `-0.0078` n `23`; metal avg `0.0807` n `20`; unknown avg `0.0789` n `764`
- 24h: commodity avg `-0.3393` n `12`; crypto_alt avg `-4.4774` n `228`; crypto_major avg `-5.2244` n `8`; equity avg `-4.0378` n `85`; fx avg `-0.1702` n `6`; index avg `-0.9405` n `23`; metal avg `-1.2406` n `20`; unknown avg `-0.3212` n `604`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1509`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1327`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1321`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1158`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0822`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0813`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0742`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0673`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0625`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0591`, n `668`, weak_sample_signal
