# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-08T01:22:23.677694+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `2.0987` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.5688` n `12`; crypto_alt avg `-0.5545` n `228`; crypto_major avg `-0.4161` n `8`; equity avg `-0.3194` n `74`; fx avg `0.0121` n `6`; index avg `-0.1881` n `23`; metal avg `-0.3292` n `18`; unknown avg `0.0821` n `517`
- 1h: commodity avg `0.3535` n `12`; crypto_alt avg `-0.2526` n `228`; crypto_major avg `-0.264` n `8`; equity avg `-0.4349` n `74`; fx avg `-0.031` n `6`; index avg `-0.263` n `23`; metal avg `-0.7678` n `18`; unknown avg `-0.2054` n `517`
- 4h: commodity avg `0.1509` n `12`; crypto_alt avg `1.3122` n `228`; crypto_major avg `1.9293` n `8`; equity avg `0.7331` n `74`; fx avg `-0.057` n `6`; index avg `0.04` n `23`; metal avg `-0.1694` n `18`; unknown avg `0.2505` n `516`
- 24h: commodity avg `0.3482` n `12`; crypto_alt avg `0.877` n `228`; crypto_major avg `3.1706` n `8`; equity avg `1.3307` n `74`; fx avg `-0.0847` n `6`; index avg `0.3659` n `23`; metal avg `-0.0182` n `18`; unknown avg `-5.0808` n `506`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1123`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0913`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0822`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0787`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0772`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0707`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0622`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0613`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0601`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0595`, n `668`, weak_sample_signal
