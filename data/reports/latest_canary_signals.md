# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-29T10:52:31.547751+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.23` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0173` n `12`; crypto_alt avg `-0.0672` n `228`; crypto_major avg `-0.0659` n `8`; equity avg `0.0116` n `88`; fx avg `0.0018` n `6`; index avg `-0.0086` n `23`; metal avg `0.0327` n `20`; unknown avg `0.1793` n `764`
- 1h: commodity avg `-0.155` n `12`; crypto_alt avg `0.0326` n `228`; crypto_major avg `0.3965` n `8`; equity avg `0.2025` n `88`; fx avg `0.0021` n `6`; index avg `0.0212` n `23`; metal avg `0.0876` n `20`; unknown avg `0.624` n `764`
- 4h: commodity avg `-0.1551` n `12`; crypto_alt avg `0.0192` n `228`; crypto_major avg `0.2743` n `8`; equity avg `0.2454` n `88`; fx avg `0.0355` n `6`; index avg `0.0477` n `23`; metal avg `-0.3876` n `20`; unknown avg `0.1491` n `764`
- 24h: commodity avg `-0.4488` n `12`; crypto_alt avg `0.4122` n `228`; crypto_major avg `0.4398` n `8`; equity avg `0.6225` n `88`; fx avg `0.0684` n `6`; index avg `0.092` n `23`; metal avg `-0.4712` n `20`; unknown avg `0.681` n `732`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1497`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1191`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1175`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1143`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1075`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1061`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1056`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1034`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1015`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0873`, n `668`, weak_sample_signal
