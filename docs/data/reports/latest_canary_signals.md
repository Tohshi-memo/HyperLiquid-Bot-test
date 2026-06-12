# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-12T20:37:35.840967+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0159` n `12`; crypto_alt avg `0.0439` n `228`; crypto_major avg `0.0588` n `8`; equity avg `0.0061` n `74`; fx avg `-0.0022` n `6`; index avg `0.0151` n `23`; metal avg `-0.0274` n `18`; unknown avg `0.0095` n `643`
- 1h: commodity avg `-0.0211` n `12`; crypto_alt avg `-0.1962` n `228`; crypto_major avg `-0.2043` n `8`; equity avg `-0.0069` n `74`; fx avg `-0.0234` n `6`; index avg `0.1206` n `23`; metal avg `0.1983` n `18`; unknown avg `-0.012` n `643`
- 4h: commodity avg `-0.1702` n `12`; crypto_alt avg `-0.2908` n `228`; crypto_major avg `-0.4422` n `8`; equity avg `-0.1455` n `74`; fx avg `-0.0171` n `6`; index avg `0.1005` n `23`; metal avg `0.2763` n `18`; unknown avg `-0.4183` n `643`
- 24h: commodity avg `-0.5435` n `12`; crypto_alt avg `0.3254` n `228`; crypto_major avg `1.0322` n `8`; equity avg `-0.096` n `74`; fx avg `0.0075` n `6`; index avg `0.5696` n `23`; metal avg `0.4633` n `18`; unknown avg `40.1295` n `514`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0993`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0784`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0766`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0736`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0708`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.068`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0664`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0612`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0599`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0589`, n `668`, weak_sample_signal
