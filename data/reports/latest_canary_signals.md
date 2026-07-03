# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-03T05:07:31.342423+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.01` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0101` n `12`; crypto_alt avg `-0.0532` n `229`; crypto_major avg `0.1105` n `8`; equity avg `-0.112` n `88`; fx avg `0.0114` n `6`; index avg `-0.0101` n `25`; metal avg `0.0292` n `20`; unknown avg `-0.4867` n `765`
- 1h: commodity avg `0.0201` n `12`; crypto_alt avg `0.013` n `229`; crypto_major avg `0.1262` n `8`; equity avg `0.199` n `88`; fx avg `0.0088` n `6`; index avg `0.083` n `25`; metal avg `0.0528` n `20`; unknown avg `-0.5353` n `765`
- 4h: commodity avg `0.1758` n `12`; crypto_alt avg `0.2125` n `229`; crypto_major avg `0.24` n `8`; equity avg `1.1089` n `88`; fx avg `0.031` n `6`; index avg `0.2935` n `25`; metal avg `0.1927` n `20`; unknown avg `-0.829` n `761`
- 24h: commodity avg `0.396` n `12`; crypto_alt avg `1.4987` n `228`; crypto_major avg `2.4744` n `8`; equity avg `-0.6653` n `88`; fx avg `-0.036` n `6`; index avg `-0.0694` n `25`; metal avg `1.2857` n `20`; unknown avg `6.0428` n `737`

## Correlations

- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1229`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1112`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.086`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0842`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0751`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0749`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0719`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0668`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0622`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0599`, n `668`, weak_sample_signal
