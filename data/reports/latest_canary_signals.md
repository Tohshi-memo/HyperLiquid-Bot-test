# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-17T21:37:24.884325+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0142` n `12`; crypto_alt avg `-0.1049` n `230`; crypto_major avg `-0.141` n `8`; equity avg `0.0175` n `96`; fx avg `0.0019` n `6`; index avg `0.0022` n `25`; metal avg `0.0017` n `20`; unknown avg `0.087` n `769`
- 1h: commodity avg `0.0618` n `12`; crypto_alt avg `0.007` n `230`; crypto_major avg `0.0932` n `8`; equity avg `0.0278` n `96`; fx avg `-0.0223` n `6`; index avg `0.0035` n `25`; metal avg `0.015` n `20`; unknown avg `-0.0184` n `769`
- 4h: commodity avg `0.1164` n `12`; crypto_alt avg `-0.4605` n `230`; crypto_major avg `-0.117` n `8`; equity avg `-1.3536` n `96`; fx avg `-0.0543` n `6`; index avg `-0.1967` n `25`; metal avg `-0.053` n `20`; unknown avg `-0.2162` n `769`
- 24h: commodity avg `0.7103` n `12`; crypto_alt avg `-1.4739` n `230`; crypto_major avg `-1.3173` n `8`; equity avg `-1.5041` n `94`; fx avg `0.0549` n `6`; index avg `-0.3257` n `25`; metal avg `-0.0377` n `20`; unknown avg `-0.0636` n `736`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1347`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1088`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1005`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0923`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0894`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0884`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.088`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0879`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0863`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0835`, n `668`, weak_sample_signal
