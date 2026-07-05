# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-05T08:22:31.665473+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0212` n `12`; crypto_alt avg `-0.0278` n `229`; crypto_major avg `-0.0037` n `8`; equity avg `0.0131` n `88`; fx avg `0.0` n `6`; index avg `-0.0004` n `25`; metal avg `0.0125` n `20`; unknown avg `-0.0004` n `765`
- 1h: commodity avg `0.0312` n `12`; crypto_alt avg `0.2642` n `229`; crypto_major avg `0.2038` n `8`; equity avg `0.021` n `88`; fx avg `-0.0015` n `6`; index avg `-0.0008` n `25`; metal avg `0.0127` n `20`; unknown avg `0.0579` n `765`
- 4h: commodity avg `0.0191` n `12`; crypto_alt avg `0.0266` n `229`; crypto_major avg `-0.0181` n `8`; equity avg `0.0358` n `88`; fx avg `0.01` n `6`; index avg `0.0345` n `25`; metal avg `0.0063` n `20`; unknown avg `-0.0828` n `731`
- 24h: commodity avg `0.0877` n `12`; crypto_alt avg `-0.3345` n `229`; crypto_major avg `-0.7206` n `8`; equity avg `0.208` n `88`; fx avg `0.0183` n `6`; index avg `0.0562` n `25`; metal avg `0.0708` n `20`; unknown avg `-1.2709` n `725`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.105`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1005`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0978`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0941`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.091`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0894`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0891`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0756`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0669`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0651`, n `668`, weak_sample_signal
