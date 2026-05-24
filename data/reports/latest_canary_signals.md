# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-24T12:37:14.949936+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0435` n `12`; crypto_alt avg `0.0364` n `228`; crypto_major avg `0.0855` n `8`; equity avg `0.071` n `67`; fx avg `0.004` n `6`; index avg `-0.0183` n `23`; metal avg `0.0112` n `18`; unknown avg `-0.0234` n `396`
- 1h: commodity avg `0.0272` n `12`; crypto_alt avg `-0.4563` n `228`; crypto_major avg `-0.2851` n `8`; equity avg `0.0372` n `67`; fx avg `-0.0074` n `6`; index avg `-0.0005` n `23`; metal avg `-0.0687` n `18`; unknown avg `0.1185` n `396`
- 4h: commodity avg `0.1162` n `12`; crypto_alt avg `-0.6023` n `228`; crypto_major avg `0.0509` n `8`; equity avg `0.2891` n `67`; fx avg `-0.011` n `6`; index avg `-0.0652` n `23`; metal avg `-0.0755` n `18`; unknown avg `-0.4697` n `396`
- 24h: commodity avg `-2.6623` n `12`; crypto_alt avg `3.4436` n `228`; crypto_major avg `4.5976` n `8`; equity avg `2.8529` n `67`; fx avg `0.0601` n `6`; index avg `1.2552` n `23`; metal avg `1.2804` n `18`; unknown avg `1.5186` n `386`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1175`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1172`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1121`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1092`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1039`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1017`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0994`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0912`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0907`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0889`, n `668`, weak_sample_signal
