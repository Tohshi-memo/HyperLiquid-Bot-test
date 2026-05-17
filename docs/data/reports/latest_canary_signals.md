# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-17T15:07:12.489257+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0582` n `12`; crypto_alt avg `0.0833` n `228`; crypto_major avg `0.2181` n `8`; equity avg `-0.0924` n `65`; fx avg `0.0` n `5`; index avg `0.0103` n `23`; metal avg `0.0214` n `18`; unknown avg `0.0153` n `384`
- 1h: commodity avg `0.2333` n `12`; crypto_alt avg `0.2008` n `228`; crypto_major avg `0.2324` n `8`; equity avg `-0.1743` n `65`; fx avg `0.0215` n `5`; index avg `-0.076` n `23`; metal avg `-0.0325` n `18`; unknown avg `0.0758` n `383`
- 4h: commodity avg `-0.0261` n `12`; crypto_alt avg `-0.3798` n `228`; crypto_major avg `-0.1857` n `8`; equity avg `-0.0861` n `65`; fx avg `0.0027` n `5`; index avg `0.0254` n `23`; metal avg `-0.0006` n `18`; unknown avg `-0.1178` n `383`
- 24h: commodity avg `1.761` n `12`; crypto_alt avg `-9.2053` n `228`; crypto_major avg `-2.3373` n `8`; equity avg `-2.7196` n `65`; fx avg `-0.1649` n `5`; index avg `-1.6345` n `23`; metal avg `-5.8539` n `18`; unknown avg `550.0301` n `367`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1353`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1135`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0841`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.081`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0785`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0772`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0758`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0701`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0643`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0627`, n `668`, weak_sample_signal
