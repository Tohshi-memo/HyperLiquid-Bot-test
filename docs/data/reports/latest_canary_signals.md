# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-24T23:37:16.854038+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-1.5011` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0172` n `12`; crypto_alt avg `0.2083` n `228`; crypto_major avg `0.1645` n `8`; equity avg `0.0936` n `67`; fx avg `-0.0061` n `6`; index avg `0.0268` n `23`; metal avg `0.1462` n `18`; unknown avg `-0.0154` n `396`
- 1h: commodity avg `-0.2342` n `12`; crypto_alt avg `0.2853` n `228`; crypto_major avg `0.4349` n `8`; equity avg `0.0992` n `67`; fx avg `0.0029` n `6`; index avg `-0.0463` n `23`; metal avg `0.66` n `18`; unknown avg `0.8506` n `396`
- 4h: commodity avg `-0.8048` n `12`; crypto_alt avg `-0.2677` n `228`; crypto_major avg `0.0442` n `8`; equity avg `0.0334` n `67`; fx avg `0.0709` n `6`; index avg `-0.0841` n `23`; metal avg `1.5453` n `18`; unknown avg `0.7164` n `396`
- 24h: commodity avg `0.4515` n `12`; crypto_alt avg `-1.6356` n `228`; crypto_major avg `0.6579` n `8`; equity avg `0.3194` n `67`; fx avg `0.0877` n `6`; index avg `-0.1157` n `23`; metal avg `1.3392` n `18`; unknown avg `1.2686` n `386`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1364`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1228`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1198`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1119`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1083`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.108`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1073`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1068`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1068`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1061`, n `668`, weak_sample_signal
