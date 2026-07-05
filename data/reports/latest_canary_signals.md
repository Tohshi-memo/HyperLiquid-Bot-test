# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-05T07:37:27.711553+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0142` n `12`; crypto_alt avg `0.1139` n `229`; crypto_major avg `0.1217` n `8`; equity avg `0.0207` n `88`; fx avg `0.0` n `6`; index avg `-0.0015` n `25`; metal avg `-0.0018` n `20`; unknown avg `-0.0115` n `765`
- 1h: commodity avg `0.0246` n `12`; crypto_alt avg `0.1667` n `229`; crypto_major avg `0.1339` n `8`; equity avg `0.0312` n `88`; fx avg `0.0031` n `6`; index avg `-0.0088` n `25`; metal avg `-0.0132` n `20`; unknown avg `-0.0576` n `765`
- 4h: commodity avg `-0.0018` n `12`; crypto_alt avg `0.0294` n `229`; crypto_major avg `0.1958` n `8`; equity avg `0.0977` n `88`; fx avg `0.013` n `6`; index avg `0.0407` n `25`; metal avg `0.0005` n `20`; unknown avg `-0.0213` n `731`
- 24h: commodity avg `0.0671` n `12`; crypto_alt avg `-0.4499` n `229`; crypto_major avg `-0.5892` n `8`; equity avg `0.264` n `88`; fx avg `0.018` n `6`; index avg `0.0847` n `25`; metal avg `0.0627` n `20`; unknown avg `-1.1861` n `725`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1023`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0998`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0973`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0946`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0905`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0896`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0888`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0757`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0741`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0665`, n `668`, weak_sample_signal
