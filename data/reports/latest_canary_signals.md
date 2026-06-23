# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-23T02:22:31.367726+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0152` n `12`; crypto_alt avg `-0.099` n `228`; crypto_major avg `0.0897` n `8`; equity avg `0.2031` n `86`; fx avg `-0.0037` n `6`; index avg `0.0226` n `23`; metal avg `0.0866` n `20`; unknown avg `-0.1264` n `716`
- 1h: commodity avg `-0.0098` n `12`; crypto_alt avg `-0.242` n `228`; crypto_major avg `-0.2075` n `8`; equity avg `-0.814` n `86`; fx avg `-0.0147` n `6`; index avg `-0.1837` n `23`; metal avg `-0.2357` n `20`; unknown avg `0.1978` n `716`
- 4h: commodity avg `-0.0316` n `12`; crypto_alt avg `-0.2874` n `228`; crypto_major avg `-0.2705` n `8`; equity avg `-1.6385` n `86`; fx avg `0.0051` n `6`; index avg `-0.3842` n `23`; metal avg `-0.4853` n `20`; unknown avg `-0.5692` n `716`
- 24h: commodity avg `-0.4922` n `12`; crypto_alt avg `-1.4604` n `228`; crypto_major avg `-1.1763` n `8`; equity avg `-2.1191` n `85`; fx avg `-0.0569` n `6`; index avg `-0.3116` n `23`; metal avg `-0.5114` n `18`; unknown avg `0.1771` n `647`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1316`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1167`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0985`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0865`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0823`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0785`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0782`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0673`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0616`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0548`, n `668`, weak_sample_signal
