# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-05T08:07:29.578669+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0049` n `12`; crypto_alt avg `0.0344` n `229`; crypto_major avg `-0.018` n `8`; equity avg `-0.0347` n `88`; fx avg `0.0007` n `6`; index avg `-0.0007` n `25`; metal avg `-0.0105` n `20`; unknown avg `0.0412` n `765`
- 1h: commodity avg `0.0047` n `12`; crypto_alt avg `0.2622` n `229`; crypto_major avg `0.2246` n `8`; equity avg `0.0166` n `88`; fx avg `-0.0015` n `6`; index avg `-0.0002` n `25`; metal avg `-0.0016` n `20`; unknown avg `0.0172` n `765`
- 4h: commodity avg `0.0091` n `12`; crypto_alt avg `0.1781` n `229`; crypto_major avg `0.197` n `8`; equity avg `0.0767` n `88`; fx avg `0.01` n `6`; index avg `0.037` n `25`; metal avg `-0.0027` n `20`; unknown avg `-0.0777` n `731`
- 24h: commodity avg `0.0669` n `12`; crypto_alt avg `-0.3808` n `229`; crypto_major avg `-0.6794` n `8`; equity avg `0.2174` n `88`; fx avg `0.0205` n `6`; index avg `0.0698` n `25`; metal avg `0.0598` n `20`; unknown avg `-1.2739` n `725`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1044`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1007`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0978`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0941`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.091`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0896`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.089`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0756`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0682`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0667`, n `668`, weak_sample_signal
