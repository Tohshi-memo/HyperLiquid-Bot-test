# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-31T18:37:24.934874+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `1.5019` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0618` n `12`; crypto_alt avg `0.1156` n `232`; crypto_major avg `0.2252` n `8`; equity avg `-0.1167` n `129`; fx avg `-0.0004` n `6`; index avg `-0.0284` n `26`; metal avg `-0.0429` n `20`; unknown avg `1.3216` n `793`
- 1h: commodity avg `0.0755` n `12`; crypto_alt avg `0.4636` n `232`; crypto_major avg `0.5272` n `8`; equity avg `-0.0278` n `129`; fx avg `0.0136` n `6`; index avg `0.007` n `26`; metal avg `-0.0414` n `20`; unknown avg `0.5344` n `791`
- 4h: commodity avg `0.2078` n `12`; crypto_alt avg `1.0399` n `232`; crypto_major avg `1.4181` n `8`; equity avg `0.0279` n `129`; fx avg `0.0097` n `6`; index avg `-0.0685` n `26`; metal avg `-0.0838` n `20`; unknown avg `-0.1103` n `791`
- 24h: commodity avg `0.618` n `12`; crypto_alt avg `-1.0835` n `231`; crypto_major avg `-1.3225` n `8`; equity avg `-0.58` n `129`; fx avg `-0.0966` n `6`; index avg `-0.2412` n `26`; metal avg `-0.6121` n `20`; unknown avg `0.1073` n `758`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1005`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0999`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0934`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0851`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0735`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.058`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0557`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0548`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0526`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0495`, n `668`, weak_sample_signal
