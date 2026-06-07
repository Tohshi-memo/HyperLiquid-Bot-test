# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-07T22:07:23.727066+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.2079` n `12`; crypto_alt avg `0.5428` n `228`; crypto_major avg `0.3008` n `8`; equity avg `-0.1967` n `74`; fx avg `-0.0158` n `6`; index avg `-0.2513` n `23`; metal avg `-0.1491` n `18`; unknown avg `-0.0099` n `516`
- 1h: commodity avg `0.1616` n `12`; crypto_alt avg `0.2382` n `228`; crypto_major avg `0.1859` n `8`; equity avg `-0.0858` n `74`; fx avg `-0.0258` n `6`; index avg `-0.2588` n `23`; metal avg `-0.1377` n `18`; unknown avg `-0.044` n `516`
- 4h: commodity avg `0.3416` n `12`; crypto_alt avg `-1.0853` n `228`; crypto_major avg `-0.7252` n `8`; equity avg `-0.6131` n `74`; fx avg `-0.0395` n `6`; index avg `-0.2964` n `23`; metal avg `-0.4626` n `18`; unknown avg `-0.0178` n `516`
- 24h: commodity avg `0.4659` n `12`; crypto_alt avg `2.0536` n `228`; crypto_major avg `3.3967` n `8`; equity avg `1.1145` n `74`; fx avg `-0.0758` n `6`; index avg `0.0535` n `23`; metal avg `0.1545` n `18`; unknown avg `-4.7341` n `505`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1461`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1364`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1111`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0908`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0902`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0831`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0719`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.066`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0656`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.059`, n `668`, weak_sample_signal
