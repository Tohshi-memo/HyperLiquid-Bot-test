# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-20T20:37:16.590844+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0197` n `12`; crypto_alt avg `0.2734` n `228`; crypto_major avg `0.2125` n `8`; equity avg `0.2648` n `66`; fx avg `-0.0003` n `6`; index avg `0.0871` n `23`; metal avg `0.0252` n `18`; unknown avg `0.0168` n `384`
- 1h: commodity avg `-0.0667` n `12`; crypto_alt avg `-0.157` n `228`; crypto_major avg `-0.1387` n `8`; equity avg `-0.0892` n `66`; fx avg `-0.0643` n `6`; index avg `-0.0888` n `23`; metal avg `-0.1375` n `18`; unknown avg `-0.1864` n `384`
- 4h: commodity avg `-0.0995` n `12`; crypto_alt avg `0.3217` n `228`; crypto_major avg `0.2294` n `8`; equity avg `0.1774` n `66`; fx avg `-0.0475` n `6`; index avg `0.1703` n `23`; metal avg `0.2314` n `18`; unknown avg `0.2584` n `384`
- 24h: commodity avg `-2.4148` n `12`; crypto_alt avg `2.5689` n `228`; crypto_major avg `1.7315` n `8`; equity avg `1.5744` n `66`; fx avg `-0.1124` n `6`; index avg `1.2184` n `23`; metal avg `1.56` n `18`; unknown avg `0.8565` n `373`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0832`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0773`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0744`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0733`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0613`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0568`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0515`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0481`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0478`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0453`, n `668`, weak_sample_signal
