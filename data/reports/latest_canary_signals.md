# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-10T23:07:24.624174+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0089` n `12`; crypto_alt avg `-0.0829` n `229`; crypto_major avg `-0.0871` n `8`; equity avg `-0.0169` n `92`; fx avg `0.0214` n `6`; index avg `-0.0108` n `25`; metal avg `-0.0053` n `20`; unknown avg `-0.0491` n `765`
- 1h: commodity avg `0.0173` n `12`; crypto_alt avg `-0.1119` n `229`; crypto_major avg `-0.0917` n `8`; equity avg `-0.0202` n `92`; fx avg `-0.0071` n `6`; index avg `-0.0113` n `25`; metal avg `-0.0101` n `20`; unknown avg `-0.0703` n `765`
- 4h: commodity avg `-0.0087` n `12`; crypto_alt avg `0.4704` n `229`; crypto_major avg `0.2481` n `8`; equity avg `-0.1322` n `92`; fx avg `-0.0155` n `6`; index avg `-0.0175` n `25`; metal avg `0.0875` n `20`; unknown avg `-0.4195` n `765`
- 24h: commodity avg `-0.2374` n `12`; crypto_alt avg `0.9412` n `229`; crypto_major avg `0.8719` n `8`; equity avg `-0.6964` n `92`; fx avg `-0.1826` n `6`; index avg `0.0195` n `25`; metal avg `0.1267` n `20`; unknown avg `-0.2581` n `732`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.125`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1086`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.106`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1038`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1028`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1016`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0949`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0888`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0876`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0864`, n `668`, weak_sample_signal
