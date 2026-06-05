# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-05T21:22:31.216409+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0498` n `12`; crypto_alt avg `0.046` n `228`; crypto_major avg `0.0106` n `8`; equity avg `0.392` n `74`; fx avg `-0.001` n `6`; index avg `0.3228` n `23`; metal avg `0.0152` n `18`; unknown avg `0.0218` n `425`
- 1h: commodity avg `0.2935` n `12`; crypto_alt avg `1.2227` n `228`; crypto_major avg `0.9527` n `8`; equity avg `0.5285` n `74`; fx avg `-0.0027` n `6`; index avg `0.3317` n `23`; metal avg `0.2765` n `18`; unknown avg `0.6216` n `425`
- 4h: commodity avg `0.4235` n `12`; crypto_alt avg `0.5274` n `228`; crypto_major avg `0.5608` n `8`; equity avg `-0.7262` n `74`; fx avg `-0.0534` n `6`; index avg `-0.9401` n `23`; metal avg `-0.721` n `18`; unknown avg `-0.0658` n `424`
- 24h: commodity avg `-1.4683` n `12`; crypto_alt avg `-6.3037` n `228`; crypto_major avg `-5.2075` n `8`; equity avg `-6.0981` n `74`; fx avg `-0.082` n `6`; index avg `-4.1848` n `23`; metal avg `-4.4724` n `18`; unknown avg `-1.796` n `404`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1274`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1229`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0918`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.086`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0795`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0784`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0749`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0685`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0661`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0617`, n `668`, weak_sample_signal
