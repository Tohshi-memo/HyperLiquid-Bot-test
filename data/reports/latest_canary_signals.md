# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-18T13:52:18.609357+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.2378` n `12`; crypto_alt avg `0.4453` n `228`; crypto_major avg `0.4093` n `8`; equity avg `-0.0159` n `66`; fx avg `0.0098` n `5`; index avg `0.0332` n `23`; metal avg `0.2232` n `18`; unknown avg `0.1387` n `383`
- 1h: commodity avg `-0.2155` n `12`; crypto_alt avg `-0.3433` n `228`; crypto_major avg `-0.5018` n `8`; equity avg `-0.751` n `66`; fx avg `0.0029` n `5`; index avg `-0.2611` n `23`; metal avg `0.4481` n `18`; unknown avg `0.6312` n `383`
- 4h: commodity avg `-1.1071` n `12`; crypto_alt avg `0.7669` n `228`; crypto_major avg `0.6235` n `8`; equity avg `-0.1895` n `66`; fx avg `-0.0297` n `5`; index avg `0.1492` n `23`; metal avg `1.2288` n `18`; unknown avg `0.5012` n `383`
- 24h: commodity avg `-0.4642` n `12`; crypto_alt avg `-2.0847` n `228`; crypto_major avg `-1.1603` n `8`; equity avg `0.1007` n `65`; fx avg `0.0725` n `5`; index avg `0.2723` n `23`; metal avg `1.1661` n `18`; unknown avg `-0.1075` n `363`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1465`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1326`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1175`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1167`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1065`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0932`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0842`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0838`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0814`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.081`, n `668`, weak_sample_signal
