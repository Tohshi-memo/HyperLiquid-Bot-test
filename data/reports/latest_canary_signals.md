# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-12T22:37:33.648625+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0024` n `12`; crypto_alt avg `-0.2576` n `228`; crypto_major avg `-0.2385` n `8`; equity avg `0.0018` n `74`; fx avg `-0.0123` n `6`; index avg `-0.1106` n `23`; metal avg `-0.0359` n `18`; unknown avg `-0.0683` n `643`
- 1h: commodity avg `-0.0686` n `12`; crypto_alt avg `-0.3761` n `228`; crypto_major avg `-0.459` n `8`; equity avg `0.0493` n `74`; fx avg `0.0064` n `6`; index avg `0.068` n `23`; metal avg `-0.0825` n `18`; unknown avg `0.0546` n `643`
- 4h: commodity avg `-0.1474` n `12`; crypto_alt avg `-0.4225` n `228`; crypto_major avg `-0.9294` n `8`; equity avg `-0.1107` n `74`; fx avg `-0.0387` n `6`; index avg `0.0291` n `23`; metal avg `-0.1835` n `18`; unknown avg `0.3158` n `643`
- 24h: commodity avg `-0.2908` n `12`; crypto_alt avg `-0.5227` n `228`; crypto_major avg `-0.0646` n `8`; equity avg `-0.5049` n `74`; fx avg `-0.0547` n `6`; index avg `0.2628` n `23`; metal avg `0.3241` n `18`; unknown avg `41.3703` n `514`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.105`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0777`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0758`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0738`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0728`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.066`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0655`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0633`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0614`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0607`, n `668`, weak_sample_signal
