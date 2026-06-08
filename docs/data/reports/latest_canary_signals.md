# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-08T13:07:25.310577+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.4954` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `0.0058` n `12`; crypto_alt avg `0.3535` n `228`; crypto_major avg `0.3141` n `8`; equity avg `0.3157` n `74`; fx avg `0.0092` n `6`; index avg `0.1812` n `23`; metal avg `-0.1599` n `18`; unknown avg `0.3957` n `517`
- 1h: commodity avg `0.0591` n `12`; crypto_alt avg `1.0439` n `228`; crypto_major avg `1.1491` n `8`; equity avg `0.6553` n `74`; fx avg `-0.0139` n `6`; index avg `0.3188` n `23`; metal avg `-0.2985` n `18`; unknown avg `-1.8822` n `517`
- 4h: commodity avg `-0.9308` n `12`; crypto_alt avg `2.002` n `228`; crypto_major avg `1.5646` n `8`; equity avg `1.5808` n `74`; fx avg `0.0368` n `6`; index avg `0.9828` n `23`; metal avg `0.7893` n `18`; unknown avg `-1.5649` n `517`
- 24h: commodity avg `-0.3967` n `12`; crypto_alt avg `3.0708` n `228`; crypto_major avg `4.0237` n `8`; equity avg `2.7293` n `74`; fx avg `-0.2844` n `6`; index avg `1.3127` n `23`; metal avg `0.1708` n `18`; unknown avg `-2.7818` n `506`

## Correlations

- market_context_score -> fx_forward_1h_return_pct: corr `-0.1272`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1242`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1138`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1099`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1013`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0816`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.081`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0712`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0683`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0644`, n `668`, weak_sample_signal
