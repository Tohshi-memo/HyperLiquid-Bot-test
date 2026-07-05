# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-05T14:07:25.083137+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0002` n `12`; crypto_alt avg `-0.0255` n `229`; crypto_major avg `0.0832` n `8`; equity avg `-0.0577` n `88`; fx avg `-0.0114` n `6`; index avg `-0.0337` n `25`; metal avg `-0.0196` n `20`; unknown avg `0.0185` n `765`
- 1h: commodity avg `0.019` n `12`; crypto_alt avg `-0.0576` n `229`; crypto_major avg `0.0054` n `8`; equity avg `-0.0583` n `88`; fx avg `-0.0102` n `6`; index avg `-0.0082` n `25`; metal avg `-0.0138` n `20`; unknown avg `0.0257` n `765`
- 4h: commodity avg `-0.0079` n `12`; crypto_alt avg `0.7155` n `229`; crypto_major avg `0.8725` n `8`; equity avg `0.0862` n `88`; fx avg `-0.0512` n `6`; index avg `0.0121` n `25`; metal avg `0.0167` n `20`; unknown avg `0.1388` n `765`
- 24h: commodity avg `0.0069` n `12`; crypto_alt avg `-0.9771` n `229`; crypto_major avg `-0.4128` n `8`; equity avg `0.2614` n `88`; fx avg `-0.0293` n `6`; index avg `0.0477` n `25`; metal avg `0.0795` n `20`; unknown avg `-1.1202` n `731`

## Correlations

- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1023`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0993`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0971`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0968`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0933`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0877`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.087`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0841`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0778`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0685`, n `668`, weak_sample_signal
