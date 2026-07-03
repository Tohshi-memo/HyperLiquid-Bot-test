# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-03T21:20:58.677265+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.09` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.003` n `12`; crypto_alt avg `-0.0744` n `229`; crypto_major avg `-0.1767` n `8`; equity avg `0.007` n `88`; fx avg `0.0014` n `6`; index avg `0.0007` n `25`; metal avg `0.0138` n `20`; unknown avg `-0.015` n `765`
- 1h: commodity avg `-0.0476` n `12`; crypto_alt avg `0.1216` n `229`; crypto_major avg `0.099` n `8`; equity avg `0.0809` n `88`; fx avg `-0.0073` n `6`; index avg `-0.0071` n `25`; metal avg `0.0381` n `20`; unknown avg `0.4338` n `765`
- 4h: commodity avg `-0.0982` n `12`; crypto_alt avg `0.6823` n `229`; crypto_major avg `0.9209` n `8`; equity avg `-0.0191` n `88`; fx avg `-0.004` n `6`; index avg `-0.0182` n `25`; metal avg `-0.0007` n `20`; unknown avg `0.9774` n `765`
- 24h: commodity avg `0.0802` n `12`; crypto_alt avg `3.2426` n `229`; crypto_major avg `3.2911` n `8`; equity avg `1.8723` n `88`; fx avg `-0.0837` n `6`; index avg `0.4758` n `25`; metal avg `0.5435` n `20`; unknown avg `10.4742` n `739`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.104`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1025`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.081`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0791`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0774`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0767`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.07`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0697`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0665`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0644`, n `668`, weak_sample_signal
