# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-29T21:22:26.620274+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.66` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0013` n `12`; crypto_alt avg `0.122` n `228`; crypto_major avg `0.1217` n `8`; equity avg `0.0229` n `88`; fx avg `0.0059` n `6`; index avg `0.0032` n `23`; metal avg `0.0031` n `20`; unknown avg `0.4565` n `765`
- 1h: commodity avg `-0.0014` n `12`; crypto_alt avg `-0.3149` n `228`; crypto_major avg `-0.1556` n `8`; equity avg `0.0697` n `88`; fx avg `0.0046` n `6`; index avg `0.0187` n `23`; metal avg `0.0005` n `20`; unknown avg `0.5654` n `765`
- 4h: commodity avg `-0.1748` n `12`; crypto_alt avg `-0.532` n `228`; crypto_major avg `-0.0126` n `8`; equity avg `0.5889` n `88`; fx avg `0.0` n `6`; index avg `0.1155` n `23`; metal avg `0.2277` n `20`; unknown avg `0.3758` n `765`
- 24h: commodity avg `-0.3248` n `12`; crypto_alt avg `1.7557` n `228`; crypto_major avg `3.0286` n `8`; equity avg `1.7137` n `88`; fx avg `0.1926` n `6`; index avg `0.155` n `23`; metal avg `-0.472` n `20`; unknown avg `1.7893` n `732`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1551`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1311`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1215`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1166`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1127`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.111`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1102`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1099`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1084`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1083`, n `668`, weak_sample_signal
