# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-05T06:37:27.297454+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0055` n `12`; crypto_alt avg `0.1235` n `229`; crypto_major avg `0.04` n `8`; equity avg `-0.0218` n `88`; fx avg `0.0088` n `6`; index avg `-0.0042` n `25`; metal avg `0.0042` n `20`; unknown avg `-0.0328` n `765`
- 1h: commodity avg `-0.0127` n `12`; crypto_alt avg `-0.1208` n `229`; crypto_major avg `0.0458` n `8`; equity avg `-0.0194` n `88`; fx avg `0.0086` n `6`; index avg `0.0012` n `25`; metal avg `0.0066` n `20`; unknown avg `-0.0848` n `731`
- 4h: commodity avg `-0.0187` n `12`; crypto_alt avg `-0.2964` n `229`; crypto_major avg `-0.0369` n `8`; equity avg `0.0758` n `88`; fx avg `0.0084` n `6`; index avg `0.0446` n `25`; metal avg `0.0022` n `20`; unknown avg `-0.0309` n `731`
- 24h: commodity avg `0.0433` n `12`; crypto_alt avg `-0.8032` n `229`; crypto_major avg `-0.7808` n `8`; equity avg `0.1546` n `88`; fx avg `0.0106` n `6`; index avg `0.0594` n `25`; metal avg `0.0621` n `20`; unknown avg `-1.1172` n `725`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1001`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.099`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0952`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0946`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0899`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0883`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0879`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0786`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0758`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0672`, n `668`, weak_sample_signal
