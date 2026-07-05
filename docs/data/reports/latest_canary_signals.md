# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-05T09:22:28.662348+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0171` n `12`; crypto_alt avg `0.0329` n `229`; crypto_major avg `-0.1281` n `8`; equity avg `-0.0529` n `88`; fx avg `-0.0015` n `6`; index avg `0.0065` n `25`; metal avg `0.0024` n `20`; unknown avg `-0.0741` n `765`
- 1h: commodity avg `-0.0001` n `12`; crypto_alt avg `0.0343` n `229`; crypto_major avg `-0.0969` n `8`; equity avg `-0.0388` n `88`; fx avg `0.0007` n `6`; index avg `0.0094` n `25`; metal avg `0.0132` n `20`; unknown avg `-0.0799` n `765`
- 4h: commodity avg `0.0308` n `12`; crypto_alt avg `0.1265` n `229`; crypto_major avg `0.1803` n `8`; equity avg `-0.0012` n `88`; fx avg `0.0109` n `6`; index avg `0.0016` n `25`; metal avg `0.0233` n `20`; unknown avg `-0.091` n `731`
- 24h: commodity avg `0.0874` n `12`; crypto_alt avg `-0.4114` n `229`; crypto_major avg `-0.7684` n `8`; equity avg `0.1904` n `88`; fx avg `0.0136` n `6`; index avg `0.0588` n `25`; metal avg `0.071` n `20`; unknown avg `-1.1819` n `725`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1034`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0984`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0954`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.095`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0916`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0887`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0874`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0754`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0676`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0633`, n `668`, weak_sample_signal
