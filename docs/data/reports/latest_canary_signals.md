# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-03T23:39:24.785222+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.04` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0018` n `12`; crypto_alt avg `0.0669` n `229`; crypto_major avg `0.1111` n `8`; equity avg `-0.0098` n `88`; fx avg `-0.0076` n `6`; index avg `-0.0115` n `25`; metal avg `0.008` n `20`; unknown avg `-0.0642` n `765`
- 1h: commodity avg `-0.01` n `12`; crypto_alt avg `-0.0111` n `229`; crypto_major avg `0.1143` n `8`; equity avg `0.0389` n `88`; fx avg `-0.0147` n `6`; index avg `-0.0084` n `25`; metal avg `0.0329` n `20`; unknown avg `0.9579` n `765`
- 4h: commodity avg `-0.0334` n `12`; crypto_alt avg `0.3099` n `229`; crypto_major avg `0.4005` n `8`; equity avg `-0.0589` n `88`; fx avg `-0.0248` n `6`; index avg `-0.0439` n `25`; metal avg `0.0284` n `20`; unknown avg `0.0849` n `765`
- 24h: commodity avg `0.1406` n `12`; crypto_alt avg `3.012` n `229`; crypto_major avg `3.2362` n `8`; equity avg `1.8127` n `88`; fx avg `-0.082` n `6`; index avg `0.4014` n `25`; metal avg `0.5362` n `20`; unknown avg `5.8012` n `739`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0992`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0933`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0813`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0808`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0786`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0768`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0716`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0655`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0594`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.054`, n `668`, weak_sample_signal
