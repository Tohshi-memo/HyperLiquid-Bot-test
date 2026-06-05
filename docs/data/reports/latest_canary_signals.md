# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-05T23:22:24.467720+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `2.3515` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `2.0361` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0995` n `12`; crypto_alt avg `-0.805` n `228`; crypto_major avg `-0.6831` n `8`; equity avg `-0.1465` n `74`; fx avg `0.0` n `6`; index avg `0.0629` n `23`; metal avg `-0.0427` n `18`; unknown avg `0.1058` n `425`
- 1h: commodity avg `0.6217` n `12`; crypto_alt avg `-0.9201` n `228`; crypto_major avg `-0.581` n `8`; equity avg `-0.4114` n `74`; fx avg `-0.0091` n `6`; index avg `-0.0584` n `23`; metal avg `-0.1048` n `18`; unknown avg `-0.0646` n `425`
- 4h: commodity avg `0.4246` n `12`; crypto_alt avg `2.8787` n `228`; crypto_major avg `2.3643` n `8`; equity avg `0.3282` n `74`; fx avg `0.0162` n `6`; index avg `0.1398` n `23`; metal avg `0.0128` n `18`; unknown avg `2.1853` n `425`
- 24h: commodity avg `-1.1254` n `12`; crypto_alt avg `-6.1244` n `228`; crypto_major avg `-5.2402` n `8`; equity avg `-5.9366` n `74`; fx avg `-0.0558` n `6`; index avg `-4.0789` n `23`; metal avg `-4.4879` n `18`; unknown avg `-1.4933` n `404`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1258`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1202`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0876`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0836`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.077`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0742`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0726`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0703`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.065`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.06`, n `668`, weak_sample_signal
