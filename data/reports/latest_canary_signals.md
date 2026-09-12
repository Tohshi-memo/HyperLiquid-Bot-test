# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-12T20:22:26.479813+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0009` n `12`; crypto_alt avg `0.0535` n `233`; crypto_major avg `0.0146` n `8`; equity avg `-0.0159` n `136`; fx avg `0.0011` n `6`; index avg `-0.0077` n `26`; metal avg `-0.004` n `20`; unknown avg `10.5124` n `838`
- 1h: commodity avg `0.0062` n `12`; crypto_alt avg `-0.004` n `233`; crypto_major avg `0.0169` n `8`; equity avg `-0.2261` n `136`; fx avg `0.0029` n `6`; index avg `-0.0237` n `26`; metal avg `-0.0069` n `20`; unknown avg `0.3138` n `836`
- 4h: commodity avg `0.0707` n `12`; crypto_alt avg `-0.4229` n `233`; crypto_major avg `-0.3874` n `8`; equity avg `-0.2853` n `136`; fx avg `0.0004` n `6`; index avg `-0.0381` n `26`; metal avg `-0.0064` n `20`; unknown avg `-0.4211` n `782`
- 24h: commodity avg `-0.1694` n `12`; crypto_alt avg `0.8967` n `233`; crypto_major avg `-0.3432` n `8`; equity avg `-0.2467` n `136`; fx avg `-0.0212` n `6`; index avg `0.0083` n `26`; metal avg `-0.0014` n `20`; unknown avg `3.6099` n `722`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0771`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.068`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0666`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0645`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0622`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0573`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.056`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0539`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0484`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0432`, n `668`, weak_sample_signal
