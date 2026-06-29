# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-29T09:07:26.353776+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.15` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.017` n `12`; crypto_alt avg `-0.0829` n `228`; crypto_major avg `-0.1293` n `8`; equity avg `-0.1228` n `88`; fx avg `-0.0057` n `6`; index avg `-0.0187` n `23`; metal avg `-0.032` n `20`; unknown avg `-0.1851` n `764`
- 1h: commodity avg `0.0726` n `12`; crypto_alt avg `-0.1514` n `228`; crypto_major avg `-0.0682` n `8`; equity avg `-0.1326` n `88`; fx avg `-0.0085` n `6`; index avg `-0.0028` n `23`; metal avg `-0.1135` n `20`; unknown avg `-0.3322` n `764`
- 4h: commodity avg `-0.0541` n `12`; crypto_alt avg `0.6126` n `228`; crypto_major avg `0.7443` n `8`; equity avg `0.7546` n `88`; fx avg `0.0071` n `6`; index avg `0.2057` n `23`; metal avg `0.0153` n `20`; unknown avg `1.2026` n `732`
- 24h: commodity avg `-0.4196` n `12`; crypto_alt avg `-0.3713` n `228`; crypto_major avg `-0.5659` n `8`; equity avg `0.2892` n `88`; fx avg `0.0344` n `6`; index avg `0.0696` n `23`; metal avg `-0.2925` n `20`; unknown avg `-0.2228` n `718`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.168`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1405`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1266`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1175`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1164`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1114`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1088`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1068`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1041`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.097`, n `668`, weak_sample_signal
