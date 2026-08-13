# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-13T12:22:24.668189+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1159` n `12`; crypto_alt avg `0.0218` n `230`; crypto_major avg `0.029` n `8`; equity avg `-0.1666` n `113`; fx avg `0.0013` n `6`; index avg `-0.0173` n `25`; metal avg `-0.0717` n `20`; unknown avg `-0.1045` n `787`
- 1h: commodity avg `0.0842` n `12`; crypto_alt avg `-0.0375` n `230`; crypto_major avg `0.0169` n `8`; equity avg `-0.1746` n `113`; fx avg `-0.0043` n `6`; index avg `-0.018` n `25`; metal avg `-0.0346` n `20`; unknown avg `-0.0987` n `787`
- 4h: commodity avg `-0.0548` n `12`; crypto_alt avg `-0.016` n `230`; crypto_major avg `-0.4281` n `8`; equity avg `-0.047` n `113`; fx avg `-0.0036` n `6`; index avg `0.0044` n `25`; metal avg `0.138` n `20`; unknown avg `-0.0462` n `787`
- 24h: commodity avg `-0.3987` n `12`; crypto_alt avg `-0.9487` n `230`; crypto_major avg `-0.9227` n `8`; equity avg `0.8247` n `113`; fx avg `0.0158` n `6`; index avg `0.1142` n `25`; metal avg `-0.4738` n `20`; unknown avg `0.0728` n `754`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2263`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1929`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1897`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1892`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1809`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1762`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1631`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.146`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1353`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1304`, n `668`, weak_sample_signal
