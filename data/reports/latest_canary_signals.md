# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-06T19:22:20.412562+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0585` n `12`; crypto_alt avg `-0.1917` n `228`; crypto_major avg `-0.2006` n `8`; equity avg `-0.0114` n `74`; fx avg `-0.0104` n `6`; index avg `-0.0536` n `23`; metal avg `0.0033` n `18`; unknown avg `-0.9623` n `515`
- 1h: commodity avg `-0.1219` n `12`; crypto_alt avg `0.1916` n `228`; crypto_major avg `-0.0482` n `8`; equity avg `0.1303` n `74`; fx avg `-0.1271` n `6`; index avg `-0.0607` n `23`; metal avg `0.027` n `18`; unknown avg `-0.962` n `515`
- 4h: commodity avg `0.0526` n `12`; crypto_alt avg `0.1839` n `228`; crypto_major avg `-0.251` n `8`; equity avg `0.1214` n `74`; fx avg `0.1057` n `6`; index avg `-0.0698` n `23`; metal avg `0.1468` n `18`; unknown avg `-3.0553` n `515`
- 24h: commodity avg `0.3502` n `12`; crypto_alt avg `1.2031` n `228`; crypto_major avg `0.6435` n `8`; equity avg `-0.534` n `74`; fx avg `0.0891` n `6`; index avg `0.0447` n `23`; metal avg `-0.465` n `18`; unknown avg `1.1568` n `401`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1229`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1189`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.093`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0844`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0753`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0681`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0657`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0593`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0548`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0509`, n `668`, weak_sample_signal
