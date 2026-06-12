# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-12T23:52:36.352423+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0118` n `12`; crypto_alt avg `0.1812` n `228`; crypto_major avg `0.1202` n `8`; equity avg `0.0349` n `74`; fx avg `-0.0013` n `6`; index avg `-0.0373` n `23`; metal avg `0.0194` n `18`; unknown avg `-0.1326` n `643`
- 1h: commodity avg `0.1107` n `12`; crypto_alt avg `0.0246` n `228`; crypto_major avg `-0.143` n `8`; equity avg `0.0397` n `74`; fx avg `0.0268` n `6`; index avg `0.0003` n `23`; metal avg `0.0181` n `18`; unknown avg `-0.0919` n `643`
- 4h: commodity avg `-0.2879` n `12`; crypto_alt avg `-0.2519` n `228`; crypto_major avg `-0.491` n `8`; equity avg `0.2475` n `74`; fx avg `0.0253` n `6`; index avg `0.2291` n `23`; metal avg `0.1901` n `18`; unknown avg `0.4795` n `643`
- 24h: commodity avg `-0.5578` n `12`; crypto_alt avg `-0.3088` n `228`; crypto_major avg `-0.1135` n `8`; equity avg `-0.5589` n `74`; fx avg `0.0107` n `6`; index avg `0.2345` n `23`; metal avg `0.3117` n `18`; unknown avg `41.2691` n `514`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1095`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0785`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0765`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0738`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0692`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0692`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0653`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0601`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0601`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.058`, n `668`, weak_sample_signal
