# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-21T02:37:28.745601+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0359` n `12`; crypto_alt avg `-0.148` n `234`; crypto_major avg `-0.1859` n `8`; equity avg `-0.0509` n `140`; fx avg `-0.0047` n `6`; index avg `0.0047` n `26`; metal avg `0.0348` n `20`; unknown avg `0.8168` n `944`
- 1h: commodity avg `-0.0078` n `12`; crypto_alt avg `-0.6913` n `234`; crypto_major avg `-0.4299` n `8`; equity avg `-0.2715` n `140`; fx avg `-0.0304` n `6`; index avg `-0.0078` n `26`; metal avg `-0.0565` n `20`; unknown avg `1.6125` n `942`
- 4h: commodity avg `-0.4408` n `12`; crypto_alt avg `-0.5019` n `234`; crypto_major avg `0.3827` n `8`; equity avg `0.4006` n `140`; fx avg `-0.0609` n `6`; index avg `0.072` n `26`; metal avg `0.0079` n `20`; unknown avg `38.8045` n `935`
- 24h: commodity avg `-0.6402` n `12`; crypto_alt avg `1.0954` n `234`; crypto_major avg `1.4538` n `8`; equity avg `0.6045` n `140`; fx avg `-0.0182` n `6`; index avg `0.1229` n `26`; metal avg `0.0546` n `20`; unknown avg `3.5019` n `757`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1725`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1566`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1454`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1226`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1087`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1029`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0918`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0856`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0847`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.083`, n `668`, weak_sample_signal
