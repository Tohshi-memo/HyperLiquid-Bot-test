# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-04T05:52:20.521667+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0484` n `12`; crypto_alt avg `0.0547` n `228`; crypto_major avg `-0.115` n `8`; equity avg `-0.0743` n `73`; fx avg `0.0028` n `6`; index avg `-0.0081` n `23`; metal avg `-0.1167` n `18`; unknown avg `3.0032` n `420`
- 1h: commodity avg `-0.0387` n `12`; crypto_alt avg `-0.8063` n `228`; crypto_major avg `-0.8297` n `8`; equity avg `-0.1294` n `73`; fx avg `-0.0002` n `6`; index avg `-0.0921` n `23`; metal avg `-0.3684` n `18`; unknown avg `0.5703` n `420`
- 4h: commodity avg `0.0426` n `12`; crypto_alt avg `-0.3142` n `228`; crypto_major avg `1.4037` n `8`; equity avg `0.6862` n `73`; fx avg `-0.005` n `6`; index avg `0.0564` n `23`; metal avg `0.2555` n `18`; unknown avg `0.5` n `420`
- 24h: commodity avg `-0.1476` n `12`; crypto_alt avg `-4.1796` n `228`; crypto_major avg `-3.4879` n `8`; equity avg `-3.6051` n `73`; fx avg `-0.0459` n `6`; index avg `-1.0533` n `23`; metal avg `-1.4265` n `18`; unknown avg `0.7059` n `409`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.179`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1675`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1475`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1443`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1053`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0886`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0849`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0732`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0689`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0648`, n `668`, weak_sample_signal
