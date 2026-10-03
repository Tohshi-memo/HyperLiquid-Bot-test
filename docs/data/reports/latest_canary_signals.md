# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-03T16:52:29.109048+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1926` n `13`; crypto_alt avg `-0.0514` n `235`; crypto_major avg `0.0455` n `8`; equity avg `0.0047` n `143`; fx avg `-0.0038` n `6`; index avg `0.0009` n `26`; metal avg `-0.0048` n `20`; unknown avg `-0.0322` n `1078`
- 1h: commodity avg `-0.0097` n `13`; crypto_alt avg `0.0978` n `235`; crypto_major avg `0.0163` n `8`; equity avg `0.026` n `143`; fx avg `0.0125` n `6`; index avg `0.0065` n `26`; metal avg `0.001` n `20`; unknown avg `0.334` n `1070`
- 4h: commodity avg `0.2467` n `13`; crypto_alt avg `0.9535` n `235`; crypto_major avg `0.355` n `8`; equity avg `0.0592` n `143`; fx avg `-0.0041` n `6`; index avg `0.0249` n `26`; metal avg `0.0011` n `20`; unknown avg `-0.0579` n `950`
- 24h: commodity avg `0.397` n `13`; crypto_alt avg `-0.6867` n `235`; crypto_major avg `-0.4479` n `8`; equity avg `0.1702` n `143`; fx avg `-0.0404` n `6`; index avg `0.0409` n `26`; metal avg `0.0997` n `20`; unknown avg `0.2496` n `868`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.196`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1836`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1656`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.155`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1194`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.118`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.117`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.109`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1051`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0846`, n `668`, weak_sample_signal
