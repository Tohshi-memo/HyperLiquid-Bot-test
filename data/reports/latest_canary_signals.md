# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-09T12:22:38.812483+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0339` n `12`; crypto_alt avg `-0.1682` n `228`; crypto_major avg `-0.2033` n `8`; equity avg `-0.111` n `74`; fx avg `0.0014` n `6`; index avg `-0.0043` n `23`; metal avg `-0.1154` n `18`; unknown avg `0.0129` n `547`
- 1h: commodity avg `0.1378` n `12`; crypto_alt avg `0.7231` n `228`; crypto_major avg `0.428` n `8`; equity avg `-0.0156` n `74`; fx avg `0.0178` n `6`; index avg `-0.0427` n `23`; metal avg `0.1089` n `18`; unknown avg `0.1783` n `547`
- 4h: commodity avg `-0.0968` n `12`; crypto_alt avg `0.1211` n `228`; crypto_major avg `-0.2562` n `8`; equity avg `0.1123` n `74`; fx avg `0.1553` n `6`; index avg `0.1626` n `23`; metal avg `0.2481` n `18`; unknown avg `-0.1512` n `547`
- 24h: commodity avg `-0.2002` n `12`; crypto_alt avg `-0.466` n `228`; crypto_major avg `0.1621` n `8`; equity avg `1.3109` n `74`; fx avg `0.1453` n `6`; index avg `0.6554` n `23`; metal avg `0.383` n `18`; unknown avg `-0.5084` n `503`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1154`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1058`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0984`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0976`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0941`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0833`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0829`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0817`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.068`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0588`, n `668`, weak_sample_signal
