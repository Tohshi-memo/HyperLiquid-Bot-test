# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-30T22:37:28.497017+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.92` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0118` n `12`; crypto_alt avg `-0.2174` n `228`; crypto_major avg `-0.2762` n `8`; equity avg `-0.0374` n `88`; fx avg `-0.0025` n `6`; index avg `-0.0001` n `23`; metal avg `0.0136` n `20`; unknown avg `-0.2672` n `765`
- 1h: commodity avg `-0.0411` n `12`; crypto_alt avg `-0.0638` n `228`; crypto_major avg `-0.1265` n `8`; equity avg `0.0546` n `88`; fx avg `-0.0064` n `6`; index avg `0.0249` n `23`; metal avg `0.0828` n `20`; unknown avg `2.1505` n `765`
- 4h: commodity avg `0.0305` n `12`; crypto_alt avg `-0.2114` n `228`; crypto_major avg `-0.0602` n `8`; equity avg `0.3549` n `88`; fx avg `-0.0092` n `6`; index avg `-0.0217` n `23`; metal avg `-0.1846` n `20`; unknown avg `3.052` n `763`
- 24h: commodity avg `0.1399` n `12`; crypto_alt avg `-2.1842` n `228`; crypto_major avg `-2.3772` n `8`; equity avg `1.2255` n `88`; fx avg `0.1016` n `6`; index avg `0.2676` n `23`; metal avg `0.0292` n `20`; unknown avg `9.706` n `735`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.113`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0941`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0916`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0839`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0732`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0707`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0707`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0682`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0536`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0494`, n `668`, weak_sample_signal
