# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-12T21:52:29.657131+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0437` n `12`; crypto_alt avg `-0.0874` n `230`; crypto_major avg `-0.0914` n `8`; equity avg `-0.0118` n `92`; fx avg `0.0026` n `6`; index avg `0.0016` n `25`; metal avg `-0.0188` n `20`; unknown avg `0.112` n `765`
- 1h: commodity avg `-0.0407` n `12`; crypto_alt avg `-0.2971` n `230`; crypto_major avg `-0.3917` n `8`; equity avg `-0.0386` n `92`; fx avg `-0.0172` n `6`; index avg `-0.0027` n `25`; metal avg `-0.0257` n `20`; unknown avg `0.2256` n `765`
- 4h: commodity avg `0.0206` n `12`; crypto_alt avg `-0.2902` n `230`; crypto_major avg `-0.367` n `8`; equity avg `0.0453` n `92`; fx avg `-0.1463` n `6`; index avg `-0.0194` n `25`; metal avg `-0.0226` n `20`; unknown avg `-0.0023` n `765`
- 24h: commodity avg `0.5923` n `12`; crypto_alt avg `-1.6964` n `230`; crypto_major avg `-1.0911` n `8`; equity avg `-0.2273` n `92`; fx avg `-0.033` n `6`; index avg `-0.1067` n `25`; metal avg `-0.1163` n `20`; unknown avg `0.1922` n `741`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1744`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1589`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1253`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1233`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1204`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1066`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1052`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0999`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0994`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0954`, n `668`, weak_sample_signal
