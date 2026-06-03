# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-03T13:07:27.803520+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.3913` n `12`; crypto_alt avg `-0.06` n `228`; crypto_major avg `-0.1349` n `8`; equity avg `-0.1908` n `72`; fx avg `-0.0004` n `6`; index avg `-0.0251` n `23`; metal avg `0.0318` n `18`; unknown avg `0.0377` n `420`
- 1h: commodity avg `-0.317` n `12`; crypto_alt avg `0.1028` n `228`; crypto_major avg `-0.0242` n `8`; equity avg `-0.1746` n `72`; fx avg `-0.0125` n `6`; index avg `-0.1481` n `23`; metal avg `-0.0976` n `18`; unknown avg `0.0455` n `420`
- 4h: commodity avg `-0.5672` n `12`; crypto_alt avg `0.4397` n `228`; crypto_major avg `-0.0947` n `8`; equity avg `-0.1853` n `72`; fx avg `-0.0369` n `6`; index avg `-0.093` n `23`; metal avg `-0.0591` n `18`; unknown avg `-0.5163` n `420`
- 24h: commodity avg `1.4405` n `12`; crypto_alt avg `-1.1465` n `228`; crypto_major avg `-3.3088` n `8`; equity avg `0.3908` n `72`; fx avg `-0.0025` n `6`; index avg `0.7185` n `23`; metal avg `-1.4966` n `18`; unknown avg `-0.4268` n `409`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1131`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0757`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0696`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0633`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0621`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0619`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0541`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0517`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0497`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0497`, n `668`, weak_sample_signal
