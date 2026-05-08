# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-08T09:52:15.672351+00:00`
- Correlation status: `ready`
- Asset price records: `635`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.3768` n `12`; crypto_alt avg `-0.1963` n `228`; crypto_major avg `-0.1594` n `8`; equity avg `-0.144` n `65`; fx avg `0.0201` n `5`; index avg `-0.0203` n `23`; metal avg `-0.1967` n `18`; unknown avg `-0.0271` n `375`
- 1h: commodity avg `0.3148` n `12`; crypto_alt avg `-0.101` n `228`; crypto_major avg `-0.0884` n `8`; equity avg `-0.0416` n `65`; fx avg `0.013` n `5`; index avg `-0.0011` n `23`; metal avg `-0.1703` n `18`; unknown avg `-0.0096` n `375`
- 4h: commodity avg `0.2172` n `12`; crypto_alt avg `0.1783` n `228`; crypto_major avg `0.168` n `8`; equity avg `0.7319` n `65`; fx avg `0.0706` n `5`; index avg `0.1736` n `23`; metal avg `-0.2183` n `18`; unknown avg `0.3473` n `355`
- 24h: commodity avg `1.4275` n `12`; crypto_alt avg `0.9985` n `228`; crypto_major avg `-1.5249` n `8`; equity avg `-0.8418` n `65`; fx avg `0.2458` n `5`; index avg `-0.417` n `23`; metal avg `-0.714` n `18`; unknown avg `-0.2936` n `355`

## Correlations

- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1367`, n `627`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1358`, n `627`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1138`, n `631`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0987`, n `631`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0965`, n `631`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0954`, n `631`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0879`, n `627`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0864`, n `627`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0755`, n `631`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0746`, n `631`, weak_sample_signal
