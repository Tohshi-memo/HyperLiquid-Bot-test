# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-03T20:07:26.298048+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.26` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0128` n `12`; crypto_alt avg `0.2063` n `229`; crypto_major avg `0.2038` n `8`; equity avg `-0.0446` n `88`; fx avg `-0.0005` n `6`; index avg `-0.0134` n `25`; metal avg `-0.0128` n `20`; unknown avg `-0.0049` n `765`
- 1h: commodity avg `0.0009` n `12`; crypto_alt avg `0.4034` n `229`; crypto_major avg `0.4818` n `8`; equity avg `-0.0429` n `88`; fx avg `-0.0056` n `6`; index avg `-0.0178` n `25`; metal avg `-0.0162` n `20`; unknown avg `0.0167` n `765`
- 4h: commodity avg `-0.0229` n `12`; crypto_alt avg `0.6121` n `229`; crypto_major avg `0.9934` n `8`; equity avg `0.0005` n `88`; fx avg `-0.0073` n `6`; index avg `0.0374` n `25`; metal avg `0.0447` n `20`; unknown avg `1.1814` n `765`
- 24h: commodity avg `0.1336` n `12`; crypto_alt avg `2.9859` n `229`; crypto_major avg `3.0584` n `8`; equity avg `1.745` n `88`; fx avg `-0.0624` n `6`; index avg `0.5049` n `25`; metal avg `0.5685` n `20`; unknown avg `8.6083` n `739`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0996`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0993`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0821`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0818`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0759`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0751`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0688`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0665`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0598`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0532`, n `668`, weak_sample_signal
