# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-01T11:47:43.938142+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0067` n `12`; crypto_alt avg `-0.0692` n `228`; crypto_major avg `-0.0901` n `8`; equity avg `0.0181` n `88`; fx avg `-0.0036` n `6`; index avg `0.0056` n `23`; metal avg `0.0791` n `20`; unknown avg `-0.1467` n `765`
- 1h: commodity avg `-0.023` n `12`; crypto_alt avg `0.0415` n `228`; crypto_major avg `-0.0455` n `8`; equity avg `0.0529` n `88`; fx avg `-0.0143` n `6`; index avg `0.0329` n `23`; metal avg `0.4959` n `20`; unknown avg `0.1434` n `765`
- 4h: commodity avg `-0.1757` n `12`; crypto_alt avg `0.3414` n `228`; crypto_major avg `-0.5798` n `8`; equity avg `0.2774` n `88`; fx avg `0.0197` n `6`; index avg `0.0699` n `23`; metal avg `0.6228` n `20`; unknown avg `0.1848` n `765`
- 24h: commodity avg `-0.5221` n `12`; crypto_alt avg `0.3179` n `228`; crypto_major avg `-0.965` n `8`; equity avg `0.5222` n `88`; fx avg `0.1371` n `6`; index avg `-0.0071` n `23`; metal avg `-0.3168` n `20`; unknown avg `-0.0677` n `743`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.116`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1084`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1027`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0929`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0928`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0874`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.077`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0746`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0744`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0615`, n `668`, weak_sample_signal
