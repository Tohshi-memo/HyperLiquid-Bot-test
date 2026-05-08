# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-08T19:37:21.222297+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0612` n `12`; crypto_alt avg `0.0059` n `228`; crypto_major avg `-0.0347` n `8`; equity avg `0.0113` n `65`; fx avg `0.0034` n `5`; index avg `-0.0194` n `23`; metal avg `0.064` n `18`; unknown avg `0.1822` n `375`
- 1h: commodity avg `0.152` n `12`; crypto_alt avg `-0.0836` n `228`; crypto_major avg `0.0148` n `8`; equity avg `0.0685` n `65`; fx avg `0.0187` n `5`; index avg `0.0026` n `23`; metal avg `-0.0224` n `18`; unknown avg `-0.098` n `375`
- 4h: commodity avg `-0.1938` n `12`; crypto_alt avg `1.9134` n `228`; crypto_major avg `1.5799` n `8`; equity avg `0.6064` n `65`; fx avg `0.0452` n `5`; index avg `0.288` n `23`; metal avg `0.3833` n `18`; unknown avg `0.2324` n `375`
- 24h: commodity avg `0.0508` n `12`; crypto_alt avg `3.1663` n `228`; crypto_major avg `1.4903` n `8`; equity avg `3.3182` n `65`; fx avg `0.1938` n `5`; index avg `1.4665` n `23`; metal avg `0.8044` n `18`; unknown avg `1.1157` n `355`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1249`, n `666`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1211`, n `666`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1058`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0945`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0939`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0858`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0711`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0675`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.064`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0601`, n `668`, weak_sample_signal
